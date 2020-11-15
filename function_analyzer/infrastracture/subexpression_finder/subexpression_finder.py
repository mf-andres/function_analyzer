from typing import List

from function_analyzer.domain.expression import Expression
from function_analyzer.infrastracture.operation_finder import (
    OperationFinder,
)
from function_analyzer.infrastracture.operation_sorter import (
    OperationSorter,
)
from function_analyzer.infrastracture.subexpression_finder.subexpression_finder_interface import (
    SubexpressionFinderInterface,
)


class SubexpressionFinder(SubexpressionFinderInterface):   # TODO refactor subexpression finding
    @staticmethod
    def find_subexpressions(expression_string: str) -> List[Expression]:
        (
            opening_parentheses,
            closing_parentheses,
        ) = SubexpressionFinder.find_parentheses_pairs(expression_string)

        subexpressions = list()
        for opening_parenthesis, closing_parenthesis in zip(
            opening_parentheses, closing_parentheses
        ):
            subexpression_string = expression_string[
                opening_parenthesis + 1 : closing_parenthesis
            ]
            subexpression = Expression(
                SubexpressionFinder(),
                OperationFinder(),
                OperationSorter(),
                subexpression_string,
            )
            subexpression.position = opening_parenthesis + 1
            subexpression.tail = closing_parenthesis
            subexpressions.append(subexpression)

        return subexpressions

    @staticmethod
    def find_parentheses_pairs(expression_string):
        opening_parentheses = list()
        closing_parentheses = list()
        parenthesis_yet_to_be_close = 0
        for character_position, character in enumerate(expression_string):
            if character == "(":
                parenthesis_yet_to_be_close += 1
                if parenthesis_yet_to_be_close == 1:
                    opening_parentheses.append(character_position)
            if character == ")":
                parenthesis_yet_to_be_close -= 1
                if parenthesis_yet_to_be_close == 0:
                    closing_parentheses.append(character_position)
        return opening_parentheses, closing_parentheses
