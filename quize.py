question = [
    {
        "question" : "what is the capital of Uttarakhand?",
        "answer" : "Dehradun"

    },
    {
        "question" : "what is the state animal of Uttarakhand?",
        "answer" : "Musk Dear",

    },
    {
        "question" : "what is state flower of Uttarakhand?",
        "answer" : "Brahma kamal"
    }
]
score = 0

print("--- Welcome to the Uttarakhand State Quiz! ---")

# The loop matches each dictionary block to the variable 'item'
for item in question:
    print(f"\nQuestion: {item['question']}")
    
    # Take user input and clean it up (.strip removes accidental trailing spaces)
    user_guess = input("Your Answer: ").strip().lower()
    
    # Compare user input to the correct answer (lowercased for safe matching)
    if user_guess == item["answer"].lower():
        print("Correct! 🎉")
        score += 1
    else:
        print(f"Wrong! The correct answer was: {item['answer']}")

# --- Final Results ---
print("\n=============================")
print(f"Quiz Complete! Your Final Score: {score}/{len(question)}")
print("=============================")