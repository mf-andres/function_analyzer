from function_analyzer.domain.operation.substraction import Substraction


def test_do_operation_with_zero_result():
    function_string = '1-1'
    operation = Substraction(function_string, 1)
    returned_function_string = operation.do_operation()
    expected_function_string = '0.0'
    assert returned_function_string == expected_function_string


def test_do_operation_with_negative_result():
    function_string = '1-2'
    operation = Substraction(function_string, 1)
    returned_function_string = operation.do_operation()
    expected_function_string = '-1.0'
    assert returned_function_string == expected_function_string


def test_do_operation_with_negative_left_operand():
    function_string = '-1-1'
    operation = Substraction(function_string, 2)
    returned_function_string = operation.do_operation()
    expected_function_string = '-2.0'
    assert returned_function_string == expected_function_string
