from function_analyzer.domain.expression import Expression
from function_analyzer.domain.operation.addition import Addition


# TODO make all this tests unitary
def test_do_operation():
    function_string = '1+1'
    operation = Addition(1)
    returned_function_string = operation.do_operation(function_string)
    expected_function_string = '2.0'
    assert returned_function_string == expected_function_string


def test_do_operation_with_negative_left_operand():
    function_string = '-1+1'
    operation = Addition(2)
    returned_function_string = operation.do_operation(function_string)
    expected_function_string = '0.0'
    assert returned_function_string == expected_function_string


def test_do_operation_warns_right_operation():
    class AdditionSpy(Addition):
        def update_positions_after_shift(self, shift_length):
            super()
            self.was_warned = True

    function_string = '1+1+1'
    operation = Addition(1)
    right_operation = AdditionSpy(3)
    operation.set_right_operation(right_operation)
    operation.do_operation(function_string)
    assert right_operation.was_warned
