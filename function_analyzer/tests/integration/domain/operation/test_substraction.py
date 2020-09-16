from function_analyzer.infrastracture.operand_finder.operand_finder import OperandFinder
from function_analyzer.infrastracture.operation.substraction import Substraction


def test_do_operation_with_zero_result():
    function_string = '1-1'
    operand_finder = OperandFinder()
    operation = Substraction(operand_finder, 1, 1)
    returned_function_string = operation.do_operation(function_string)
    expected_function_string = '0.0'
    assert returned_function_string == expected_function_string


def test_do_operation_with_negative_result():
    function_string = '1-2'
    operand_finder = OperandFinder()
    operation = Substraction(operand_finder, 1, 1)
    returned_function_string = operation.do_operation(function_string)
    expected_function_string = '-1.0'
    assert returned_function_string == expected_function_string


def test_do_operation_with_negative_left_operand():
    function_string = '-1-1'
    operand_finder = OperandFinder()
    operation = Substraction(operand_finder, 2, 1)
    returned_function_string = operation.do_operation(function_string)
    expected_function_string = '-2.0'
    assert returned_function_string == expected_function_string


def test_do_operation_warns_right_operation():
    class SubstractionSpy(Substraction):
        def update_positions_after_shift(self, shift_length):
            super()
            self.was_warned = True

    function_string = '1-1-1'
    operand_finder = OperandFinder()
    operation = Substraction(operand_finder, 1, 1)
    right_operation = SubstractionSpy(operand_finder, 3, 1)
    operation.set_right_operation(right_operation)
    operation.do_operation(function_string)
    assert right_operation.was_warned
