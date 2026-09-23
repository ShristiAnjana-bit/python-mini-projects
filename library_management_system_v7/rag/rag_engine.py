import sqlite3

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

#Load environement variables
from dotenv import load_dotenv
import os

#Gemini API
from google import genai

#load environment variables from LMS root .env file
load_dotenv()

#check whether the parent folder contains .env
print("ENV exists:", os.path.exists("../.env"))


#Get Gemini API key from .env
api_key = os.getenv("GEMINI_API_KEY")

#check whether Gemini API key was loaded
print("API key loaded:", api_key is not None)


#Create Gemini client
client = genai.Client(api_key=api_key)

def get_books():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("SELECT title, author, edition, publisher FROM books")
    books = cursor.fetchall()

    conn.close()

    return books

def create_book_chunks(books):
    chunks = []

    for book in books:
        title,author,edition,publisher = book

        chunk = f"""
Title: {title}
Author: {author}
Edition: {edition}
Publisher: {publisher}
"""

        chunks.append(chunk)

    return chunks

model = SentenceTransformer("all-MiniLM-L6-v2")

#Create function for the Library AI Assistant
def ask_library_assistant(query):
    #get books from database
    books = get_books()
    chunks = create_book_chunks(books)
    print(chunks)

    #create embeddings for all books
    embeddings = []

    for chunk in chunks:
        embedding = model.encode(chunk)
        embeddings.append(embedding)

    print(len(embeddings))
       
    #convert the user's question into an embedding
    query_embedding = model.encode(query)


    #calculate similarity between the question and each book
    scores = []

    for embedding in embeddings:
        score = cosine_similarity([query_embedding], [embedding])
        scores.append(score)

    #find the most relevent book
    highest = max(scores)
    highest_index = scores.index(highest)

    #Retrieve most relevant chunk
    retrieved_chunk = chunks[highest_index]
    print(retrieved_chunk)

    #Create prompt using the user's question and retrived book info
    prompt = f"""
    Question: {query}

    Context:
    {retrieved_chunk}

    Answer the question using the context above.
    """
    #Send the Rag prompt to Gemini
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    #return Gemini's final answer
    return response.text

