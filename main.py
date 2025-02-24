
import re
questions = ["What is the capital of NZ?",
             "What is the best number?",
             "What is the tallest mountain in NZ?"
            ]
possible_answers = {0 : ["1. Wellington", "2. Auckland", "3. Queenstown", "4. Sydney"],
                    1 : ["1. 11", "2. Eleven", "3. three", "4. None of the above"],
                    2 : ["1. Mt. Cook", "3. Mount Cook", "3. Mountain Cook", "4. Aoraki"]
                    }
answers = [1, 2, 2]
score = 0
var = 0

def error_detection():
    while True:
        try:
            var = int(input(":"))
            break
        except ValueError:
            print ("Please enter a number")
    return var


if __name__ == '__main__':
    for i in range(len(questions)):
        print(questions[i])
        for u in range(0, len(possible_answers[i])):
            print(possible_answers[i][u])
        answer = error_detection()
        if answer == answers[i]:
            print("Correct")
            score += 1
        else:
            print("That is not the answer")
    print(f"Your score is {score} out of {len(questions)}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
