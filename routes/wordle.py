import json
import logging
import random

import nltk
from flask import jsonify, request
from routes import app

logger = logging.getLogger(__name__)
nltk.download("words")
from nltk.corpus import words

@app.route('/wordle-game', methods=['POST'])
def wordle_game():
    data = request.get_json()
    guessHistory = data.get("guessHistory")
    evaluationHistory = data.get("evaluationHistory")
    try:
        guess = playWordle(guessHistory, evaluationHistory)
        return jsonify({'guess': guess})
    except Exception as e:
        return jsonify({"error": e})

def playWordle(guess_history, evaluation_history):
    
    possible_guesses = [
        word for word in words.words() if len(word) == 5 and word[0].islower()
    ]
    
    if len(guess_history) == 0:
        return jsonify({'guess': possible_guesses[0]})
    
    not_solved_idx = [0, 1, 2, 3, 4]
    correct_letters = []

    for i in range(len(guess_history)):
        user_input = guess_history[i]
        check_string = evaluation_history[i]

        for i in range(5):
            if i in not_solved_idx:
                if check_string[i] == "?":
                    continue
                elif check_string[i] == "-":
                    if user_input[i] in correct_letters:
                        possible_guesses = [
                            word
                            for word in possible_guesses
                            if user_input[i] != word[i]
                        ]
                        print(str(len(possible_guesses)) + " -")
                        print(possible_guesses)
                    else:
                        possible_guesses = [
                            word
                            for word in possible_guesses
                            if user_input[i] not in word
                        ]
                        print(str(len(possible_guesses)) + " -")
                        print(possible_guesses)
                elif check_string[i] == "X":
                    possible_guesses = [
                        word
                        for word in possible_guesses
                        if user_input[i] in word and word[i] != user_input[i]
                    ]
                    print(possible_guesses)
                    print(str(len(possible_guesses)) + " X")
                elif check_string[i] == "O":
                    correct_letters.append(user_input[i])
                    not_solved_idx.remove(i)
                    possible_guesses = [
                        word for word in possible_guesses if word[i] == user_input[i]
                    ]
                    print(possible_guesses)
                    print(str(len(possible_guesses)) + " O")

    return possible_guesses[0]
