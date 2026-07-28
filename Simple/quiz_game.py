def load_questions():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which language is used for web apps along with HTML/CSS?",
            "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
            "answer": "B"
        },
        {
            "question": "What does 'CPU' stand for?",
            "options": ["A. Central Process Unit", "B. Central Processing Unit",
                        "C. Computer Personal Unit", "D. Central Processor Utility"],
            "answer": "B"
        },
        {
            "question": "Which data type is immutable in Python?",
            "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
            "answer": "D"
        },
        {
            "question": "What is 5 ** 2 in Python?",
            "options": ["A. 10", "B. 25", "C. 7", "D. 32"],
            "answer": "B"
        }
    ]
    return questions


def ask_question(q, index):
    print(f"\nQ{index}. {q['question']}")
    for option in q["options"]:
        print(option)

    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ("A", "B", "C", "D"):
            return answer
        print("Invalid input. Please enter A, B, C, or D.")


def run_quiz(questions):
    score = 0
    total = len(questions)

    for i, q in enumerate(questions, start=1):
        user_answer = ask_question(q, i)
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}")

    return score, total


def show_result(score, total):
    percentage = (score / total) * 100
    print("\n=== Quiz Completed ===")
    print(f"Score: {score}/{total} ({percentage:.1f}%)")

    if percentage == 100:
        print("Perfect score! Excellent!")
    elif percentage >= 60:
        print("Good job!")
    else:
        print("Keep practicing!")


def main():
    print("=== Welcome to the Quiz Game ===")
    questions = load_questions()
    score, total = run_quiz(questions)
    show_result(score, total)


if __name__ == "__main__":
    main()