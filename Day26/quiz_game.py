def quiz_game():
    # Questions and answers stored in a dictionary
    questions = {
        "What is the capital of France?": "Paris",
        "Which language is used for web development?": "HTML",
        "What is 5 + 7?": "12",
        "Who developed Python?": "Guido van Rossum"
    }

    score = 0
    print("Welcome to the Quiz Game!\n")

    # Loop through questions
    for i, (question, answer) in enumerate(questions.items(), start=1):
        print(f"Q{i}: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == answer.lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {answer}\n")

    # Final score
    print(f"Your final score is {score}/{len(questions)}")

    # Feedback
    if score == len(questions):
        print("🎉 Excellent! You got all correct.")
    elif score >= len(questions)//2:
        print("👍 Good job, keep practicing!")
    else:
        print("📚 Better luck next time, keep learning!")

# Run the game
quiz_game()
