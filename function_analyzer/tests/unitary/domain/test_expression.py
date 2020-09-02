from function_analyzer.domain.expression import Expression


def test_substitute_x_for_abscissa_substitutes_many_xs():
    abscissa = 1
    function_string = 'x+x+x+x'
    expression = Expression(function_string)
    expression.substitute_x_for_abscissa(abscissa)
    returned_function_string = expression.expression_string
    expected_function_string = '1+1+1+1'
    assert returned_function_string == expected_function_string
