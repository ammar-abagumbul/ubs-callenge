from flask import Flask

app = Flask(__name__)

import routes.digitalColony
import routes.monster
import routes.wordle
