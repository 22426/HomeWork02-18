
import re

questions = ["What is the capital of NZ?", "What is the best number?", "What is the tallest mountain in NZ?"]
answers = ["wellington", "eleven", "mountcook"]
score = 0

if __name__ == '__main__':
    for i in range(0, len(questions)):
        print(questions[i])
        answer = input(":")
        answer = re.sub(r"\s+", "", answer)
        if answer.lower() == answers[i]:
            print("Correct")
            score += 1
        else:
            print("That is not the answer")
    print(f"Your score is {score} out of {len(questions)}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
