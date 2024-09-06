
# ? Welcome message
def welcome():
    print("\n Test Your Knowledge!\n")

# ? Questions
questions = {
    1: {
        'question': 'What is the capital of Britain?',
        'choices': ['a) Munich', 'b) London', 'c) England', 'd) Manchester'],
        'answer': 'b) London'
    },
    2: {
        'question': 'Why did the chicken cross the road?',
        'choices': ['a) Because they felt like it', 'b) There was food', 'c) To get to the other side', 'd) She saw a rooster'],
        'answer': 'c) To get to the other side'
    },
    3: {
        'question': 'What comes down but never goes up?',
        'choices': ['a) Rain', 'b) Cake', 'c) Spaceship', 'd) Sunshine'],
        'answer': 'a) Rain'
    },
    4: {
        'question': 'Who said "the truth is out there"?',
        'choices': ['a) Skinner', 'b) Homer', 'c) Scully', 'd) Mulder'],
        'answer': 'd) Mulder'
    },
    5: {
        'question': 'Why did Joel do what he did?',
        'choices': ['a) Love', 'b) Hate', 'c) Likes mushrooms too much', 'd) He hates doctors'],
        'answer': 'a) Love'
    }
}

# ? USER INPUT
def play_quiz():

    score = 0
    
    welcome()
    
    print("Question 1: ", questions[1]['question'], "\n\n", questions[1]['choices'], "\n")
    guess = input("a, b, c, or d: ")
    if guess == 'b':
        print(f"Answer is : ", questions[1]['answer'], "\nCorrect!")
        score += 1
        print(f"Score: {score}")
    else:
        print("Better luck on the next question...")
        print(f"Score: {score}")

    print("Question 2: ", questions[2]['question'], "\n\n", questions[2]['choices'], "\n")
    guess = input("a, b, c, or d: ")
    if guess == 'c':
        print(f"Answer is : ", questions[2]['answer'], "\nCorrect!")
        score += 1
        print(f"Score: {score}")
    else:
        print("Better luck on the next question...")
        print(f"Score: {score}")

    print("Question 3: ", questions[3]['question'], "\n\n", questions[3]['choices'], "\n")
    guess = input("a, b, c, or d: ")
    if guess == 'a':
        print(f"Answer is : ", questions[3]['answer'], "\nCorrect!")
        score += 1
        print(f"Score: {score}")
    else:
        print("Better luck on the next question...")
        print(f"Score: {score}")

    print("Question 4: ", questions[4]['question'], "\n\n", questions[4]['choices'], "\n")
    guess = input("a, b, c, or d: ")
    if guess == 'd':
        print(f"Answer is : ", questions[4]['answer'], "\nCorrect!")
        score += 1
        print(f"Score: {score}")
    else:
        print("Better luck on the next question...")
        print(f"Score: {score}")

    print("Question 5: ", questions[5]['question'], "\n\n", questions[5]['choices'], "\n")
    guess = input("a, b, c, or d: ")
    if guess == 'a':
        print(f"Answer is : ", questions[5]['answer'], "\nCorrect!")
        score += 1
        print(f"Score: {score}")
    else:
        print("Better luck on the next question...")
        print(f"Score: {score}")

    print(f"Total score is: {score} / 5.\n\nThank you for playing!")


play_quiz()






# def modded_dict():
#   print(str(questions).replace("[", "").replace("]", ""))


# * TUTOR CODE ----------

    # for q_num, details in questions.items():
    #     question = details['artist']
    #     genre = info['genre']
    #     print(f'Title: {title}, Artist: {artist}, Genre: {genre}')


# def show_questions():
    
#     for key, value in questions.items():
#         # str(questions[value]).replace("[", "").replace("]", "")
#         print(f"\nQuestion {key}: \n" , value['question'], "\n\n", value['choices'], "\n")

# * ---------------------

# print(f"\n1) {questions[1]['question']}: \n\n{questions[1]['answer']}\n")