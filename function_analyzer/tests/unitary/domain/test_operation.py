from function_analyzer.domain.operand import Operand
from function_analyzer.domain.operation import Operation


def test_substitute_operands_and_operation_for_partial_result():
    function_string = '1+2'
    sign_position = 1
    operation = Operation(sign_position, 1)

    left_operand_position = 0
    left_operand_string = '1'
    left_operand_tail = 1

    right_operand_position = 2
    right_operand_string = '2'
    right_operand_tail = 3

    partial_result = "3"

    left_operand = Operand(left_operand_position, left_operand_string, left_operand_tail)
    right_operand = Operand(right_operand_position, right_operand_string, right_operand_tail)

    returned_function_string = operation.substitute_operation_for_partial_result(
        function_string,
        left_operand,
        right_operand,
        partial_result)

    expected_function_string = '3'
    assert returned_function_string == expected_function_string
