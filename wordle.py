import random
import nltk

nltk.download('words')
from nltk.corpus import words

possible_guesses = [word.lower() for word in words.words() if len(word) == 5]

user_input = input("Guess: ")
solved = False
attempt = 1


not_solved_idx = [0, 1, 2, 3, 4]

guess_history = []
evaluation_history = []


while(not solved and attempt <= 6):
    check_string = input("Check String: ")
    guess_history.append(user_input)
    evaluation_history.append(check_string)

    for i in range(5):
        if i in not_solved_idx:
          if check_string[i] == "?":
            continue
          elif check_string[i] == "-":
            possible_guesses = [word for word in possible_guesses if user_input[i] not in word]
            print(str(len(possible_guesses))+ " -")
            print(possible_guesses)
          elif check_string[i] == "X":
            possible_guesses = [word for word in possible_guesses if user_input[i] in word and word[i] != user_input[i]]
            print(possible_guesses)
            print(str(len(possible_guesses))+ " X")
          elif check_string[i] == "O":
            not_solved_idx.remove(i)
            possible_guesses = [word for word in possible_guesses if word[i] == user_input[i]]
            print(possible_guesses)
            print(str(len(possible_guesses)) + " O")

    # random_num = possible_guesses.index(random.choice(possible_guesses))
    user_input = possible_guesses[0]
    print("Guess: " + user_input)
    attempt += 1
            
        

