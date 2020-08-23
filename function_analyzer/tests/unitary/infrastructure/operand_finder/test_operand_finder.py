from function_analyzer.infrastracture.operand_finder.operand_finder import find_left_operand, \
    find_left_operand_position, find_right_operand, find_right_operand_tail_position


def test_find_left_operand():
    function_string = '1+2'
    sign_position = 1
    left_operand_position = 0
    returned_operand = find_left_operand(function_string, sign_position, left_operand_position)
    expected_operand = '1'
    assert returned_operand == expected_operand


def test_find_left_operand_position():
    function_string = '1+2'
    sign_position = 1
    returned_operand_position = find_left_operand_position(function_string, sign_position)
    expected_operand_position = 0
    assert returned_operand_position == expected_operand_position


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
