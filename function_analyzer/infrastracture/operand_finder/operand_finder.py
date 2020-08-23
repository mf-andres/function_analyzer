from function_analyzer.infrastracture.sign_finder.sign_finder import find_left_sign_or_end_position, \
    find_right_sign_or_end_position


def find_left_operand_position(function_string, sign_position):
    left_sign_or_end_position = find_left_sign_or_end_position(function_string, sign_position)
    return left_sign_or_end_position


def find_left_operand(function_string, sign_position, left_sign_or_end_position) -> int:
    left_operand = function_string[left_sign_or_end_position:sign_position]
    return left_operand


def find_right_operand_tail_position(function_string, sign_position):
    right_sign_or_end_position = find_right_sign_or_end_position(function_string, sign_position)
    right_operand_tail_position = right_sign_or_end_position
    return right_operand_tail_position


def find_right_operand(function_string, sign_position, right_operand_tail) -> int:
    sign_tail_position = sign_position + 1
    right_operand = function_string[sign_tail_position:right_operand_tail]
    return right_operand
