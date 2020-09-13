from function_analyzer.domain.sign import Sign
from function_analyzer.infrastracture.sign_finder.sign_finder import find_left_sign_or_end_position, \
    find_right_sign_or_end_position


def find_left_operand_position(function_string, sign_position):
    left_sign_or_end_position = find_left_sign_or_end_position(function_string, sign_position)
    # TODO refactor negative sign case
    left_operand = find_left_operand(function_string, sign_position, left_sign_or_end_position)
    if left_operand == '-':
        if left_sign_or_end_position == 0 or Sign.is_sign(function_string[left_sign_or_end_position - 1]):
            left_sign_or_end_position -= 1
    return left_sign_or_end_position


def find_left_operand(function_string, sign_position, left_sign_or_end_position) -> str:
    left_operand = function_string[left_sign_or_end_position:sign_position]
    return left_operand


def find_right_operand_tail_position(function_string, sign_position):
    right_sign_or_end_position = find_right_sign_or_end_position(function_string, sign_position)
    right_operand_tail_position = right_sign_or_end_position
    return right_operand_tail_position


def find_right_operand(function_string, sign_position, right_operand_tail) -> str:
    sign_tail_position = sign_position + 1
    right_operand = function_string[sign_tail_position:right_operand_tail]
    return right_operand
