from function_analyzer.domain.operation.addition import Addition


def test_do_addition_for_two_addends_addition():
    function_string = '1+1'
    returned_function_string = Addition.do_operation(function_string)
    expected_function_string = '2.0'
    assert returned_function_string == expected_function_string

