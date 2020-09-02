from function_analyzer.domain.expression import Expression
from function_analyzer.domain.operation.substraction import Substraction


def test_do_operation_with_zero_result():
    function_string = '1-1'
    expression = Expression(function_string)
    operation = Substraction(expression, 1)
    returned_function_string = operation.do_operation()
    expected_function_string = '0.0'
    assert returned_function_string == expected_function_string


def test_do_operation_with_negative_result():
    function_string = '1-2'
    expression = Expression(function_string)
    operation = Substraction(expression, 1)
    returned_function_string = operation.do_operation()
    expected_function_string = '-1.0'
    assert returned_function_string == expected_function_string


def test_do_operation_with_negative_left_operand():
    function_string = '-1-1'
    expression = Expression(function_string)
    operation = Substraction(expression, 2)
    returned_function_string = operation.do_operation()
    expected_function_string = '-2.0'
    assert returned_function_string == expected_function_string


def test_do_operation_warns_right_operation():
    class SubstractionSpy(Substraction):
        def update_positions_after_shift(self, shift_length):
            super()
            self.was_warned = True

    function_string = '1-1-1'
    expression = Expression(function_string)
    operation = Substraction(expression, 1)
    right_operation = SubstractionSpy(expression, 3)
    operation.set_right_operation(right_operation)
    operation.do_operation()
    assert right_operation.was_warned
