import time
import json
import os

# Define the quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Oxygen", "C. Hydrogen", "D. Iron"],
        "answer": "B"
    }
]

high_scores_file = 'high_scores.json'

def load_high_scores():
    if os.path.exists(high_scores_file):
        with open(high_scores_file, 'r') as file:
            return json.load(file)
    return []

def save_high_scores(high_scores):
    with open(high_scores_file, 'w') as file:
        json.dump(high_scores, file)

def display_high_scores():
    high_scores = load_high_scores()
    if high_scores:
        print("\nHigh Scores: ")
        for idx, score in enumerate(high_scores):
            print(f"{idx+1}. {score['name']} - {score['score']}")
    else:
        print("\nNo high scores found.")

def save_high_score(name, score):
    high_scores = load_high_scores()
    high_scores.append({"name": name, "score": score})
    high_scores.sort(key=lambda x: x["score"], reverse=True)
    save_high_scores(high_scores[:10])  # Only keep the top 10 high scores

def quiz_game():
    score = 0
    total_questions = len(questions)
    time_limit = 10  # seconds
    
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}/{total_questions}")  # Similar like Question 1/10 to the User interface
        print(question['question'])  # Under question list, iterate over question
        for option in question['options']:  # creating an instance named option from options under question dict
            print(option)
        
        start_time = time.time()
        user_answer = input("Enter your answer (A, B, C, D): ").upper()
        elapsed_time = time.time() - start_time
        
        if elapsed_time > time_limit:
            print("TIme's up!")
            continue   # to the next question
        
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}")

    print(f"\nYour final score is: {score}/{total_questions}")  # like 7/10
    
    name = input("Enter your name: ")
    save_high_score(name, score)
    display_high_scores()

if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    display_high_scores()
    quiz_game()
    print("Thank you for playing!")