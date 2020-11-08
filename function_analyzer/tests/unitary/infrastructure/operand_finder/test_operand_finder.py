import pytest

from function_analyzer.domain.operand import Operand
from function_analyzer.infrastracture.operand_finder.operand_finder import OperandFinder


def test_find_left_operand():
    function_string = '1+2'
    sign_position = 1
    returned_operand = OperandFinder.find_left_operand(function_string, sign_position)
    expected_operand = Operand(0, '1', 1)
    assert returned_operand == expected_operand


def test_find_left_operand_position():
    function_string = '1+2'
    sign_position = 1
    returned_operand_position = OperandFinder.find_left_operand_position(function_string, sign_position)
    expected_operand_position = 0
    assert returned_operand_position == expected_operand_position


def test_find_left_operand_position_():
    function_string = '1+2+3'
    sign_position = 3
    returned_operand_position = OperandFinder.find_left_operand_position(function_string, sign_position)
    expected_operand_position = 2
    assert returned_operand_position == expected_operand_position


def test_find_right_sign_operand():
    function_string = "1+2"
    sign_position = 1
    returned_operand = OperandFinder.find_right_operand(function_string, sign_position)
    expected_operand = Operand(2, '2', 3)
    assert returned_operand == expected_operand


def test_find_right_operand_tail_position():
    function_string = '1+2'
    sign_position = 1
    returned_operand_tail = OperandFinder.find_right_operand_tail(function_string, sign_position)
    expected_operand_tail = 3
    assert returned_operand_tail == expected_operand_tail


@pytest.mark.parametrize("function_string, sign_position, expected_right_operand_string",
                         [
                             ('0+-1.0', 1, '-1.0'),
                             ('0+-1.0-2.0', 1, '-1.0'),
                         ])
def test_find_right_negative_operand(function_string, sign_position, expected_right_operand_string):
    right_operand = OperandFinder.find_right_operand(function_string, sign_position)
    assert right_operand.operand == expected_right_operand_string
