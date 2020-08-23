from function_analyzer.infrastracture.operand_finder.operand_finder import find_left_operand_position, \
    find_right_operand_tail_position, find_left_operand, find_right_operand
from function_analyzer.infrastracture.sign_finder.sign_finder import find_addition_sign_position


def calculate_function_ordinate(abscissa: float, function_string: str) -> float:
    function_string = substitute_x_for_abscissa(abscissa, function_string)
    ordinate = do_operations_recursively(function_string)
    ordinate = format_ordinate(ordinate)
    return ordinate


def substitute_x_for_abscissa(abscissa: float, function_string: str) -> str:
    function_string = function_string.replace("x", str(abscissa))
    return function_string


def do_operations_recursively(function_string: str) -> str:
    if addition_found(function_string):
        function_string = do_addition(function_string)
        return function_string
    else:
        return function_string


def addition_found(function_string: str) -> bool:  # TODO make operation_found <- operation classes
    return function_string.find('+') >= 0


def do_addition(function_string: str) -> str:  # TODO make do_operation <- operation classes
    addition_sign_position = find_addition_sign_position(function_string)
    left_operand_position = find_left_operand_position(function_string, addition_sign_position)
    right_operand_tail_position = find_right_operand_tail_position(function_string, addition_sign_position)
    left_operand = find_left_operand(function_string, addition_sign_position, left_operand_position)
    right_operand = find_right_operand(function_string, addition_sign_position, right_operand_tail_position)
    partial_result = calculate_partial_result(left_operand, right_operand)
    function_string = substitute_operation_for_partial_result(function_string,
                                                              left_operand_position,
                                                              right_operand_tail_position,
                                                              partial_result)
    function_string = do_operations_recursively(function_string)
    return function_string


def calculate_partial_result(left_operand, right_operand):  # TODO <- operation classes
    partial_result = float(left_operand) + float(right_operand)
    return partial_result


def substitute_operation_for_partial_result(function_string,
                                            left_operand_position,
                                            right_operand_tail,
                                            partial_result):
    operands_and_operation_to_be_replaced = function_string[left_operand_position:right_operand_tail]
    function_string = function_string.replace(operands_and_operation_to_be_replaced, str(partial_result))
    return function_string


def format_ordinate(ordinate: str) -> float:
    return float(ordinate)
