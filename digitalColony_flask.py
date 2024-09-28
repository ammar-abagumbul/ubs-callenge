from digitalColony import weight_after_gen
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/weight_after_gen', methods=['POST'])
def weight_after_gen_route():
    data = request.get_json()
    colony = data.get('colony')
    generations = data.get('generations')
    if colony is None or generations is None:
        return jsonify({'error': 'Missing colony or generations'}), 400
    result = weight_after_gen(colony, int(generations))
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
