from function_analyzer.use_cases.calculate_function_ordinate import calculate_function_ordinate, do_addition, \
    find_left_operand, find_left_sign_or_end_position, find_right_operand, find_right_sign_tail_or_end_position


def test_calculate_function_ordinate_for_two_addends_addition():
    abscissa = 1
    function_string = 'x+1'
    returned_ordinate = calculate_function_ordinate(abscissa, function_string)
    expected_ordinate = 4
    assert expected_ordinate == returned_ordinate


def test_do_adittion_for_two_addends_addition():
    function_string = '1+1'
    returned_function_string = do_addition(function_string)
    expected_function_string = '2'
    assert returned_function_string == expected_function_string


def test_find_left_operand():
    function_string = '1+2'
    sign_position = 1
    returned_operand = find_left_operand(function_string, sign_position)
    expected_operand = '1'
    assert returned_operand == expected_operand


def test_find_left_sign_or_end_position():
    function_string = '1+2'
    sign_position = 1
    returned_sign_position = find_left_sign_or_end_position(function_string, sign_position)
    expected_sign_position = 0
    assert returned_sign_position == expected_sign_position


def test_find_right_sign_operand():
    function_string = "1+2"
    sign_position = 1
    returned_operand = find_right_operand(function_string, sign_position)
    expected_operand = '2'
    assert returned_operand == expected_operand


def test_find_right_sign_tail_or_end_position():
    function_string = '1+2'
    sign_position = 1
    returned_sign_tail_or_end_position = find_right_sign_tail_or_end_position(function_string, sign_position)
    expected_sign_tail_or_end_position = 3
    assert returned_sign_tail_or_end_position == expected_sign_tail_or_end_position
