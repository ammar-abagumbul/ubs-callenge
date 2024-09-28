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

def weight_after_gen(colony, generations):
    for _ in range(generations):
        colony = next_generation(colony)
    return cal_weight(colony)
print(weight_after_gen("914", 10))
