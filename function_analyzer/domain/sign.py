def is_sign(character: str):
    if character == '+':
        return True


def contains_sign(string: str):
    answer = False
    for character in string:
        if is_sign(character):
            answer = True
    return answer
