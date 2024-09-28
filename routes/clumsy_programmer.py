def differs_by_one_char(word1, word2):
    diff_count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1

def correct_mistypes(dictionary, mistypes):
    corrections = []
    for mistyped_word in mistypes:
        for correct_word in dictionary:
            if differs_by_one_char(mistyped_word, correct_word):
                corrections.append(correct_word)
                break
    return corrections

dictionary = ["purple", "rocket", "silver", "gadget", "window", "dragon"]
mistypes = ["purqle", "gadgat", "socket", "salver"]
corrections = correct_mistypes(dictionary, mistypes)
print({"corrections": corrections})