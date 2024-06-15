print("Welcome to the quiz!")

playing = input("Do you want to play? yes/no: ")

if playing.lower() != "yes":
    quit()

print("Let's play :)")
score = 0
total_questions = 4


def ask_question(question, correct_answer):
    global score
    while True:
        answer = input(question + " ")
        if answer.lower() == correct_answer.lower():
            print("Correct Answer!!")
            score += 1
            break
        else:
            print("Wrong answer! Try again.")


def print_score():
    print(f"You got {score} questions correct!")
    print(f"You got {(score / total_questions) * 100}%.")


ask_question("What is 2+2?", "4")
ask_question("Name a red vegetable.", "tomato")
ask_question("What does RAM stand for?", "Random Access Memory")
ask_question("What is the largest planet in the solar system?", "Jupiter")

print_score()
