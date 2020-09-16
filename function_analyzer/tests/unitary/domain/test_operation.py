from function_analyzer.domain.operand import Operand
from function_analyzer.domain.operation import Operation


# as Operand is just a value object it is not worthy of faking

# TODO invert operand_finder dependency and unit test

def test_calculate_shift_length():
    left_operand = Operand(None, '123', None)
    right_operand = Operand(None, '123', None)
    partial_result = '123'
    returned_shift_length = Operation.calculate_shift_length(left_operand, partial_result, right_operand)
    expected_shift_length = 4
    assert returned_shift_length == expected_shift_length


def test_substitute_operands_and_operation_for_partial_result():
    function_string = '1+2'

    left_operand_position = 0
    left_operand_string = '1'
    left_operand_tail = 1
    left_operand = Operand(left_operand_position, left_operand_string, left_operand_tail)

    right_operand_position = 2
    right_operand_string = '2'
    right_operand_tail = 3
    right_operand = Operand(right_operand_position, right_operand_string, right_operand_tail)

    partial_result = "3"

    returned_function_string = Operation.substitute_operation_for_partial_result(
        function_string,
        left_operand,
        right_operand,
        partial_result)

    expected_function_string = '3'
    assert returned_function_string == expected_function_string
