from function_analyzer.domain.operation.addition import Addition
from function_analyzer.domain.operation.substraction import Substraction
from function_analyzer.use_cases.calculate_function_ordinate import calculate_function_ordinate, \
    substitute_x_for_abscissa


def test_calculate_function_ordinate_for_two_addends_addition():
    abscissa = 1
    function_string = 'x+1'
    returned_ordinate = calculate_function_ordinate(Substraction, Addition, abscissa, function_string)
    expected_ordinate = 2
    assert returned_ordinate == expected_ordinate


def test_calculate_function_ordinate_for_many_addends_addition():
    abscissa = 1
    function_string = 'x+x+x+1'
    returned_ordinate = calculate_function_ordinate(Substraction, Addition, abscissa, function_string)
    expected_ordinate = 4
    assert returned_ordinate == expected_ordinate


def test_calculate_function_ordinate_for_two_operands_substraction():
    abscissa = 1
    function_string = 'x-1'
    returned_ordinate = calculate_function_ordinate(Substraction, Addition, abscissa, function_string)
    expected_ordinate = 0
    assert returned_ordinate == expected_ordinate


def test_substitute_x_for_abscissa_substitutes_many_xs():  # TODO this belongs elsewhere
    abscissa = 1
    function_string = 'x+x+x+x'
    returned_function_string = substitute_x_for_abscissa(abscissa, function_string)
    expected_function_string = '1+1+1+1'
    assert returned_function_string == expected_function_string

