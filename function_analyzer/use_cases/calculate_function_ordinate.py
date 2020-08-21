def calculate_function_ordinate(abscissa: float, function_string: str) -> float:
    function_string = substitute_x_for_abscissa(abscissa, function_string)  # TODO this seems to be low level
    ordinate = do_operations(function_string)
    return float(ordinate)


def substitute_x_for_abscissa(abscissa: float, function_string: str) -> str:  # TODO test for many x's
    function_string = function_string.replace("x", str(abscissa))
    return function_string


def do_operations(function_string: str) -> str:
    if addition_found(function_string):
        function_string = do_addition(function_string)
        return function_string
    else:
        return function_string


def addition_found(function_string: str) -> bool:
    return function_string.find('+') >= 0


def do_addition(function_string: str) -> str:
    addition_sign_position = find_addition_sign_position(function_string)  # TODO different abstraction layers mixed
    left_operand_position = find_left_operand_position(function_string, addition_sign_position)
    right_operand_tail_position = find_right_operand_tail_position(function_string, addition_sign_position)
    left_operand = find_left_operand(function_string, addition_sign_position, left_operand_position)
    right_operand = find_right_operand(function_string, addition_sign_position, right_operand_tail_position)
    partial_result = float(left_operand) + float(right_operand)
    function_string = substitute_operation_for_partial_result(function_string,
                                                              left_operand_position,
                                                              right_operand_tail_position,
                                                              partial_result)
    function_string = do_operations(function_string)
    return function_string


def find_addition_sign_position(function_string: str) -> int:
    addition_position = function_string.find('+')
    return addition_position


def find_left_operand_position(function_string, sign_position):
    left_sign_or_end_position = find_left_sign_or_end_position(function_string, sign_position)
    return left_sign_or_end_position


def find_left_operand(function_string, sign_position, left_sign_or_end_position) -> int:  # TODO duplicity
    left_operand = function_string[left_sign_or_end_position:sign_position]
    return left_operand


def find_right_operand_tail_position(function_string, sign_position):
    right_sign_tail_or_end_position = find_right_sign_tail_or_end_position(function_string, sign_position)
    return right_sign_tail_or_end_position


def find_right_operand(function_string, sign_position, right_sign_tail_or_end_position) -> int:
    sign_tail_position = sign_position + 1
    right_operand = function_string[sign_tail_position:right_sign_tail_or_end_position]
    return right_operand


def find_left_sign_or_end_position(function_string: str, sign_position: int) -> int:
    return sign_position - 1  # TODO test and complete


def find_right_sign_tail_or_end_position(function_string: str, sign_position: int) -> int:
    return sign_position + 2  # TODO test and complete


def substitute_operation_for_partial_result(function_string,
                                            left_operand_position,
                                            right_operand_tail,
                                            partial_result):
    operation_to_be_replaced = function_string[left_operand_position:right_operand_tail]
    function_string = function_string.replace(operation_to_be_replaced, str(partial_result))
    return function_string
