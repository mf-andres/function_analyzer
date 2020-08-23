from function_analyzer.infrastracture.sign_finder.sign_finder import find_left_sign_or_end_position, \
    find_right_sign_or_end_position


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


def test_find_right_sign_or_end_position_for_sum_operand():
    function_string = '1+2+4'
    sign_position = 1
    returned_right_sign_or_end_position = find_right_sign_or_end_position(function_string, sign_position)
    expected_right_sign_or_end_position = 3
    assert returned_right_sign_or_end_position == expected_right_sign_or_end_position


def test_find_right_sign_or_end_position_for_end():
    function_string = '1+2+4'
    sign_position = 3
    returned_right_sign_or_end_position = find_right_sign_or_end_position(function_string, sign_position)
    expected_right_sign_or_end_position = 5
    assert returned_right_sign_or_end_position == expected_right_sign_or_end_position
