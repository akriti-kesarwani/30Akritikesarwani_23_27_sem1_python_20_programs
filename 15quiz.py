class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def display(self):
        print(self.text)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def is_correct(self, user_answer):
        return user_answer == self.correct_option


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def take_quiz(self, user):
        score = 0
        for question in self.questions:
            question.display()
            user_answer = int(input("Enter the number of your answer: "))
            if question.is_correct(user_answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {question.correct_option}\n")

        print(f"Quiz completed! Your score: {score}/{len(self.questions)}")
        user.add_score(self.name, score)


class User:
    def __init__(self, name):
        self.name = name
        self.scores = {}

    def add_score(self, quiz_name, score):
        self.scores[quiz_name] = score

    def display_scores(self):
        print(f"Scores for {self.name}:")
        for quiz_name, score in self.scores.items():
            print(f"{quiz_name}: {score}/{len(quizzes[quiz_name].questions)}")


# Sample data
questions1 = [
    Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3),
    Question("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], 2),
]

questions2 = [
    Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 2),
    Question("Who wrote 'Romeo and Juliet'?", ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"], 1),
]

quizzes = {
    "Geography Quiz": Quiz("Geography Quiz", questions1),
    "General Knowledge Quiz": Quiz("General Knowledge Quiz", questions2),
}

# Main program
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    user = User(user_name)

    while True:
        print("\nAvailable Quizzes:")
        for quiz_name in quizzes:
            print(quiz_name)

        selected_quiz = input("\nEnter the name of the quiz you want to take (or 'exit' to quit): ")

        if selected_quiz.lower() == 'exit':
            break

        if selected_quiz in quizzes:
            quizzes[selected_quiz].take_quiz(user)
        else:
            print("Invalid quiz name. Please try again.")

    user.display_scores()
