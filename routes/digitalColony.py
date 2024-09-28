import json
from flask import jsonify, request
from routes import app
from flask import make_response


def cal_weight(colony):
    return sum(int(digit) for digit in colony)

def calculate_signature(digit1, digit2):
    difference = abs(int(digit1) - int(digit2))
    return difference if int(digit1) > int(digit2) else 10 - difference

def next_generation(colony):
    weight = cal_weight(colony)
    new_colony = colony[0]
    for i in range(len(colony) - 1):
        signature = calculate_signature(colony[i], colony[i+1])
        new_digit = (weight + signature) % 10
        new_colony += str(new_digit) + colony[i+1]
    return new_colony

@app.route('/digital-colony', methods=['POST'])
def evaluate():
    if request.content_type != 'application/json':
        return jsonify({"error": "Request Content-Type must be application/json"}), 400

    data = request.get_json()
    result = []
    for i in data:
        colony = i.get("colony")
        generations = i.get("generations")
        for _ in range(generations):
            colony = next_generation(colony)
        result.append(str(cal_weight(colony)))
        return jsonify(result)
    response = make_response(jsonify(result))
    response.headers['Content-Type'] = 'application/json'
    return response
