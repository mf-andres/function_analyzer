import pytest

from function_analyzer.domain.sign import Sign


@pytest.mark.parametrize("sign", [Sign.ADDITION_CHARACTER, Sign.SUBSTRACTION_CHARACTER])
def test_is_sign_when_sign_given(sign):
    assert Sign.is_sign(sign) is True


# TODO parametrize after adding more signs
# @pytest.mark.parametrize("sign_position, expression_string", [(0, '-1'), (2, '1*-1')])
def test_is_operation_sign_returns_false_for_negative_operand_sign():
    sign_position = 0
    expression_string = '-1'
    assert Sign.is_operation_sign(sign_position, expression_string) is False
