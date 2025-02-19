
import re
questions = ["What is the capital of NZ?",
             "What is the best number?",
             "What is the tallest mountain in NZ?"
            ]
possible_answers = {0 : ["1. Wellington", "2. Auckland", "3. Queenstown", "4. Sydney"],
                    1 : ["1. 11", "2. Eleven", "3. three", "4. None of the above"],
                    2 : ["1. Mt. Cook", "Mount Cook", "3. Mountain Cook", "4. Aoraki"]
                    }
answers = [1, 2, 2]
score = 0
var = 0

def error_detection():
    while
    try:
        var = int(input(:))
    except ValueError:
        print ("Please enter a number")


if __name__ == '__main__':
    for i in range(len(questions)):
        print(questions[i])
        var = i
        print(possible_answers[i])
        answer = input(":")
        answer = re.sub(r"\s+", "", answer)
        if answer.lower() == answers[i]:
            print("Correct")
            score += 1
        else:
            print("That is not the answer")
    print(f"Your score is {score} out of {len(questions)}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
