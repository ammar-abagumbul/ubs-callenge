from digitalColony import weight_after_gen
from wordle import playWordle
from flask import Flask, request, jsonify

####################
import nltk
nltk.download('words')
from nltk.corpus import words
possible_guesses = [word for word in words.words() if len(word) == 5 and word[0].islower()]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Home Page"

@app.route('/wordle-game', methods=['POST'])
def weight_after_gen_route():
    data = request.get_json()
    colony = data.get('colony')
    generations = data.get('generations')
    if colony is None or generations is None:
        return jsonify({'error': 'Missing colony or generations'}), 400
    result = weight_after_gen(colony, int(generations))
    return jsonify({'result': result})


@app.route('/wordle-game', methods=['POST'])
def wordle_game():
    data = request.get_json()
    guessHistory = data.get("guessHistory")
    evaluationHistory = data.get("evaluationHistory")

    guess = playWordle(guessHistory, evaluationHistory)
    return jsonify({'guess': guess})

if __name__ == '__main__':
    app.run(debug=True)
