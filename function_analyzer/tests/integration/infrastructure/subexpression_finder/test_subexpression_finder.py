from function_analyzer.infrastracture.subexpression_finder.subexpression_finder import SubexpressionFinder


def test_finds_one_subexpression():  # TODO refactor things under here
    expression_string = "x*(x-1)"
    subexpressions = SubexpressionFinder.find_subexpressions(expression_string)
    assert len(subexpressions) == 1


def test_finds_many_subexpressions():
    expression_string = "x*(x-1)*(x+1)*(x+1)"
    subexpressions = SubexpressionFinder.find_subexpressions(expression_string)
    assert len(subexpressions) == 3


def test_finds_one_subexpression_with_subexpressions():
    expression_string = "x*((x+1)*(x+2))"
    subexpressions = SubexpressionFinder.find_subexpressions(expression_string)
    assert len(subexpressions) == 1
