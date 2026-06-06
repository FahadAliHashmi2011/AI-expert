import requests
import random
import html
AMOUNT = 10
DIFFICULTY = "easy"
TYPE = "multiple"
CATEGORY = 9
API_URL = f"https://opentdb.com/api.php?amount={AMOUNT}&category={CATEGORY}&difficulty={DIFFICULTY}&type={TYPE}"

def get_educational_questions():
    response = requests.get(API_URL)
    data = response.json()
    questions = data["results"]
    print(questions)
    return

    score = 0
    print("welcome to the Ultimate Quiz Game!\n")
    for number, q in enumerate(questions,1):
        question_text = html.unescape(q["question"])
        right_answer = html.unescape(q["correct_answer"])
        wrong_answers = [html.unescape(a)for a in q["incorrect_answers"]]

        all_choices = wrong_answers + [right_answer]
        random.shuffle(all_choices)


        print(f"Question{number}: {question_text}")
        print(f"1.{all_choices[0]}")
        print(f"2.{all_choices[1]}")
        print(f"3.{all_choices[2]}")
        print(f"4.{all_choices[3]}")

        while True :
            try:
                guess = input(input("your answer(1,2,3 or 4): "))
                if 1 <=guess <= 4:
                    break
                else:
                    print("please eter a number from 1 to 4")
            except ValueError:
                print("that is not a number please enter a number from 1 to 4")
        
        
        player_choice = all_choices[guess - 1]

        if player_choice == right_answer:
            print("correct answer!")
        else:
            print(f"not quite the correct answer was:{right_answer}\n")
    
    print(f"game over your score was {score} out of 5")

if __name__  == "__main___":
    get_educational_questions()

                