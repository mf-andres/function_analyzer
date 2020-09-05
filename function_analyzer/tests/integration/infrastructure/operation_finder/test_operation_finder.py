from function_analyzer.domain.expression import Expression
from function_analyzer.infrastracture.operation_finder.operation_finder import OperationFinder


def test_finds_two_additions():
    expression_string = '1+1+1'
    operation_finder = OperationFinder()
    operation_finder.set_expression_string(expression_string)
    additions = operation_finder.find_operations()
    assert len(additions) == 2


def test_finds_two_substractions():
    expression_string = '1-1-1'
    operation_finder = OperationFinder()
    operation_finder.set_expression_string(expression_string)
    substractions = operation_finder.find_operations()
    assert len(substractions) == 2


def test_find_two_substractions_in_expression_with_negative_operand():
    expression_string = '-1-1-1'
    operation_finder = OperationFinder()
    operation_finder.set_expression_string(expression_string)
    substractions = operation_finder.find_operations()
    assert len(substractions) == 2
