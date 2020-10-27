from function_analyzer.domain.expression import Expression
from function_analyzer.infrastracture.operation_finder.operation_finder import OperationFinder
from function_analyzer.infrastracture.operation_sorter.operation_sorter import OperationSorter
from function_analyzer.infrastracture.subexpression_finder.subexpression_finder_interface import \
    SubexpressionFinderInterface


class SubexpressionFinder(SubexpressionFinderInterface):
    @staticmethod
    def find_subexpressions(expression_string: str):
        opening_parentheses = list()
        closing_parentheses = list()
        for character_position, character in enumerate(expression_string):
            if character == "(":
                opening_parentheses.append(character_position)
            elif character == ")":
                closing_parentheses.append(character_position)

        subexpressions = list()
        for parentheses_par in range(len(opening_parentheses)):  # TODO doable with zip
            opening_parenthesis = opening_parentheses[parentheses_par]
            closing_parenthesis = closing_parentheses[parentheses_par]
            subexpression_string = expression_string[opening_parenthesis + 1: closing_parenthesis - 1]
            subexpression = Expression(SubexpressionFinder(), OperationFinder(), OperationSorter(), subexpression_string)
            subexpressions.append(subexpression)

        return subexpressions

