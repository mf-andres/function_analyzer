# TODO make a class
def is_sign(character: str):
    if character == '-':  # TODO make signs array (character in sign_collection?)
        return True
    if character == '+':
        return True


def contains_sign(string: str):
    answer = False
    for character in string:
        if is_sign(character):
            answer = True
    return answer


def is_operation_sign(sign_position, function_string):  # TODO test
    sign = function_string[sign_position]
    if not is_sign(sign):
        return False
    elif is_sign_of_negative_operand(sign_position, function_string):
        return False
    else:
        return True


def is_sign_of_negative_operand(sign_position, function_string):
    if sign_position == 0:
        return True
    elif previous_character_is_sign(sign_position, function_string):
        return True
    else:
        return False


def previous_character_is_sign(sign_position, function_string):
    return is_sign(function_string[sign_position - 1])
