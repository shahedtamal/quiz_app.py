class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
                "answer": "C"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
                "answer": "B"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
                "answer": "D"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Jane Austen"],
                "answer": "C"
            },
            {
                "question": "What is the chemical symbol for water?",
                "options": ["A) O2", "B) H2O", "C) CO2", "D) NaCl"],
                "answer": "B"
            },
        ]
        self.score = 0

    def take_quiz(self):
        for idx, question in enumerate(self.questions):
            print(f"Question {idx + 1}: {question['question']}")
            for option in question['options']:
                print(option)

            answer = input("Your answer (A/B/C/D): ").upper()
            if answer == question['answer']:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['answer']}.\n")

        self.show_score()

    def show_score(self):
        print(f"Your final score is {self.score} out of {len(self.questions)}.")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.take_quiz()
