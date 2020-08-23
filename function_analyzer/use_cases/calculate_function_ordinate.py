def calculate_function_ordinate(abscissa: float, function_string: str) -> float:
    function_string = substitute_x_for_abscissa(abscissa, function_string)
    ordinate = do_operations_recursively(function_string)
    ordinate = format_ordinate(ordinate)
    return ordinate


def substitute_x_for_abscissa(abscissa: float, function_string: str) -> str:  # TODO test for many x's
    function_string = function_string.replace("x", str(abscissa))
    return function_string


def format_ordinate(ordinate: str) -> float:
    return float(ordinate)


def do_operations_recursively(function_string: str) -> str:
    if addition_found(function_string):
        function_string = do_addition(function_string)
        return function_string
    else:
        return function_string


def addition_found(function_string: str) -> bool:  # TODO make operation_found
    return function_string.find('+') >= 0


def do_addition(function_string: str) -> str:  # TODO make do_operation
    addition_sign_position = find_addition_sign_position(function_string)  # TODO different abstraction layers mixed
    left_operand_position = find_left_operand_position(function_string, addition_sign_position)
    right_operand_tail_position = find_right_operand_tail_position(function_string, addition_sign_position)
    left_operand = find_left_operand(function_string, addition_sign_position, left_operand_position)
    right_operand = find_right_operand(function_string, addition_sign_position, right_operand_tail_position)
    partial_result = calculate_partial_result(left_operand, right_operand)
    function_string = substitute_operands_and_operation_for_partial_result(function_string,
                                                                           left_operand_position,
                                                                           right_operand_tail_position,
                                                                           partial_result)
    function_string = do_operations_recursively(function_string)
    return function_string


def find_addition_sign_position(function_string: str) -> int:  # TODO make find operation sign position
    addition_position = function_string.find('+')
    return addition_position


def find_left_operand_position(function_string, sign_position):  # TODO make it into a operand_finder class?
    left_sign_or_end_position = sign_position - 1
    return left_sign_or_end_position


def find_left_sign_or_end_position(function_string, sign_position):
    left_substring = function_string[:sign_position]
    reversed_left_substring = left_substring[::-1]
    left_sign_position = 0
    character_position = sign_position
    for character in reversed_left_substring:
        character_position -= 1
        if is_operation(character):
            left_sign_position = character_position
    return left_sign_position


def is_operation(character: str):
    if character == '+':
        return True


def find_left_operand(function_string, sign_position, left_sign_or_end_position) -> int:
    left_operand = function_string[left_sign_or_end_position:sign_position]
    return left_operand


def find_right_operand_tail_position(function_string, sign_position):
    right_sign_tail_or_end_position = sign_position + 2
    return right_sign_tail_or_end_position


def find_right_operand(function_string, sign_position, right_operand_tail) -> int:
    sign_tail_position = sign_position + 1
    right_operand = function_string[sign_tail_position:right_operand_tail]
    return right_operand


def calculate_partial_result(left_operand, right_operand):
    partial_result = float(left_operand) + float(right_operand)
    return partial_result


def substitute_operands_and_operation_for_partial_result(function_string,
                                                         left_operand_position,
                                                         right_operand_tail,
                                                         partial_result):
    operands_and_operation_to_be_replaced = function_string[left_operand_position:right_operand_tail]
    function_string = function_string.replace(operands_and_operation_to_be_replaced, str(partial_result))
    return function_string
