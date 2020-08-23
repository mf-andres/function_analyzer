from function_analyzer.use_cases.calculate_function_ordinate import calculate_function_ordinate, do_addition, \
    substitute_operation_for_partial_result, substitute_x_for_abscissa


def test_calculate_function_ordinate_for_two_addends_addition():
    abscissa = 1
    function_string = 'x+1'
    returned_ordinate = calculate_function_ordinate(abscissa, function_string)
    expected_ordinate = 2
    assert returned_ordinate == expected_ordinate


def test_calculate_function_ordinate_for_many_addends_addition():
    abscissa = 1
    function_string = 'x+x+x+1'
    returned_ordinate = calculate_function_ordinate(abscissa, function_string)
    expected_ordinate = 4
    assert returned_ordinate == expected_ordinate


def test_substitute_x_for_abscissa_substitutes_many_xs():  # TODO this belongs elsewhere
    abscissa = 1
    function_string = 'x+x+x+x'
    returned_function_string = substitute_x_for_abscissa(abscissa, function_string)
    expected_function_string = '1+1+1+1'
    assert returned_function_string == expected_function_string


def test_do_addition_for_two_addends_addition():
    function_string = '1+1'
    returned_function_string = do_addition(function_string)
    expected_function_string = '2.0'
    assert returned_function_string == expected_function_string


def test_substitute_operands_and_operation_for_partial_result():
    function_string = '1+2'
    left_operand_position = 0
    right_operand_tail = 3
    partial_result = 3
    returned_function_string = substitute_operation_for_partial_result(function_string,
                                                                       left_operand_position,
                                                                       right_operand_tail,
                                                                       partial_result)

    expected_function_string = '3'
    assert returned_function_string == expected_function_string
