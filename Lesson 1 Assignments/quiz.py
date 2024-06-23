# Define the quiz questions and answers
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"}
]

# Initialize the score
score = 0

# Ask the questions and keep track of the score
for question in questions:
    user_answer = input(question["question"] + " ")
    if user_answer.lower() == question["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is " + question["answer"])

# Print the final score
print("Your final score is " + str(score) + "/" + str(len(questions)))