import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "libraray_app_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD")
    )
    

def get_published_posts():
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id,title,content,created_at
                FROM posts
                WHERE status = 'published'
                ORDER BY created_at DESC;
                """)

            posts = cur.fetchall()
            return posts
    finally:
        conn.close()


