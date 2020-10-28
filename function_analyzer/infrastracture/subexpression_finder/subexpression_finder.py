from function_analyzer.domain.expression import Expression
from function_analyzer.infrastracture.operation_finder.operation_finder import OperationFinder
from function_analyzer.infrastracture.operation_sorter.operation_sorter import OperationSorter
from function_analyzer.infrastracture.subexpression_finder.subexpression_finder_interface import \
    SubexpressionFinderInterface


class SubexpressionFinder(SubexpressionFinderInterface):
    @staticmethod
    def find_subexpressions(expression_string: str):
        opening_parentheses = SubexpressionFinder.find_opening_parentheses(expression_string)
        closing_parentheses = SubexpressionFinder.find_closing_parentheses(expression_string)

        subexpressions = list()
        for opening_parenthesis, closing_parenthesis in zip(opening_parentheses, closing_parentheses):
            subexpression_string = expression_string[opening_parenthesis + 1: closing_parenthesis - 1]
            subexpression = Expression(SubexpressionFinder(), OperationFinder(), OperationSorter(), subexpression_string)
            subexpressions.append(subexpression)

        return subexpressions

    @staticmethod
    def find_closing_parentheses(expression_string):
        closing_parentheses = list()
        for character_position, character in enumerate(expression_string):
            if character == ")":
                closing_parentheses.append(character_position)
        return closing_parentheses

    @staticmethod
    def find_opening_parentheses(expression_string):
        opening_parentheses = list()
        for character_position, character in enumerate(expression_string):
            if character == "(":
                opening_parentheses.append(character_position)
        return opening_parentheses

