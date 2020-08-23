from function_analyzer.use_cases.calculate_function_ordinate import calculate_function_ordinate, do_addition, \
    find_left_operand, find_right_operand, \
    substitute_operands_and_operation_for_partial_result, find_left_operand_position, find_right_operand_tail_position, \
    find_left_sign_or_end_position, find_right_sign_or_end_position


def test_calculate_function_ordinate_for_two_addends_addition():
    abscissa = 1
    function_string = 'x+1'
    returned_ordinate = calculate_function_ordinate(abscissa, function_string)
    expected_ordinate = 2
    assert returned_ordinate == expected_ordinate


def test_do_addition_for_two_addends_addition():
    function_string = '1+1'
    returned_function_string = do_addition(function_string)
    expected_function_string = '2.0'
    assert returned_function_string == expected_function_string


def test_find_left_operand():
    function_string = '1+2'
    sign_position = 1
    left_operand_position = 0
    returned_operand = find_left_operand(function_string, sign_position, left_operand_position)
    expected_operand = '1'
    assert returned_operand == expected_operand


def test_find_left_operand_position():  # TODO separate tests into classes
    function_string = '1+2'
    sign_position = 1
    returned_operand_position = find_left_operand_position(function_string, sign_position)
    expected_operand_position = 0
    assert returned_operand_position == expected_operand_position


def test_find_left_sign_or_end_position_for_sum_operand():
    function_string = '1+2+3-3'
    sign_position = 3
    returned_left_sign_or_end_position = find_left_sign_or_end_position(function_string, sign_position)
    expected_left_sign_or_end_position = 1
    assert returned_left_sign_or_end_position == expected_left_sign_or_end_position


def test_find_left_sign_or_end_position_for_end():
    function_string = '1+2+3-3'
    sign_position = 1
    returned_left_sign_or_end_position = find_left_sign_or_end_position(function_string, sign_position)
    expected_left_sign_or_end_position = 0
    assert returned_left_sign_or_end_position == expected_left_sign_or_end_position


def test_find_right_sign_operand():
    function_string = "1+2"
    sign_position = 1
    right_operand_tail = 3
    returned_operand = find_right_operand(function_string, sign_position, right_operand_tail)
    expected_operand = '2'
    assert returned_operand == expected_operand


def test_find_right_operand_tail_position():
    function_string = '1+2'
    sign_position = 1
    returned_operand_tail = find_right_operand_tail_position(function_string, sign_position)
    expected_operand_tail = 3
    assert returned_operand_tail == expected_operand_tail


def test_find_right_sign_or_end_position_for_sum_operand():
    function_string = '1+2+4'
    sign_position = 1
    returned_right_sign_or_end_position = find_right_sign_or_end_position(function_string, sign_position)
    expected_right_sign_or_end_position = 3
    assert returned_right_sign_or_end_position == expected_right_sign_or_end_position


def test_substitute_operands_and_operation_for_partial_result():
    function_string = '1+2'
    left_operand_position = 0
    right_operand_tail = 3
    partial_result = 3
    returned_function_string = substitute_operands_and_operation_for_partial_result(function_string,
                                                                                    left_operand_position,
                                                                                    right_operand_tail,
                                                                                    partial_result)

    expected_function_string = '3'
    assert returned_function_string == expected_function_string
