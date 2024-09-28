from flask import Flask, request, jsonify

import logging
import socket

from routes import app

logger = logging.getLogger(__name__)


####################
import nltk
nltk.download('words')
from nltk.corpus import words
possible_guesses = [word for word in words.words() if len(word) == 5 and word[0].islower()]

@app.route('/', methods=['GET'])
def default_route():
    return 'Python Template'

## Logging settings

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    logging.info("Starting application ...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    port = sock.getsockname()[1]
    sock.close()
    app.run(port=port)

