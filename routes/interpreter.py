variables = dict()


def set(var, value):
    variables[var] = value


def substring(string, start, end):
    string = string.strip().strip('"')
    start = int(start)
    end = int(end)
    return string[start:end]


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if float(a) != int(a) and float(b) != int(b):
        return float(a) / float(b)
    else:
        return int(a) // int(b)


def greaterThan(a, b):
    return float(a) > float(b)


def lowerThan(a, b):
    return float(a) < float(b)


def equal(a, b):
    return a == b


def not_equal(a, b):
    return a != b


def concat(a, b):
    return str(a) + str(b)


def printl(string):
    string = string.strip().strip('"')
    return string


interpreterFunctions = {
    "puts": printl,
    "set": set,
    "concat": concat,
    "lowercase": str.lower,
    "uppercase": str.upper,
    "replace": str.replace,
    "substring": substring,
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "abs": abs,
    "max": max,
    "min": min,
    "gt": greaterThan,
    "lt": lowerThan,
    "equal": equal,
    "not_equal": not_equal,
    "str": str,
}


def parseLine(line):

    cmd = extract_arguments(line)
    if len(cmd) == 1:
        print("func: ", cmd[0])
        func, *args = cmd[0].split()
        return execute(line, func, *args)
    elif cmd is literal:
        return literal
    else:
        args = []
        print("func: ", cmd[0])
        print("args: ", cmd[1:])
        for subcmd in cmd[1:]:
            args.append(parseLine(subcmd))
        return execute(line, cmd[0], *args)


def execute(line, func, *args):
    return interpreterFunctions[func](*args)


def find_outer_expressions(s):
    stack = []
    result = []

    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            open_index = stack.pop()
            if not stack:
                result.append((open_index, i))  # Add the pair (open, close)

    return result


def extract_arguments(s):
    parts = []
    s = s[1:-1]
    idx = find_outer_expressions(s)
    end = 0
    for r in idx:
        parts.append(s[end : r[0]].strip())
        parts.append(s[r[0] : r[1] + 1].strip())
        end = r[1] + 2
    if s[end : len(s)]:
        parts.append(s[end : len(s)])

    return parts


while True:
    usr = input()
    # print(extract_arguments(usr))
    print(parseLine(usr))
