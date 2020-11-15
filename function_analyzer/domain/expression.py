from function_analyzer.domain.operation.operation import Operation
from function_analyzer.infrastracture.operation_finder import (
    OperationFinder,
)
from function_analyzer.infrastracture.operation_sorter import (
    OperationSorter,
)
from function_analyzer.infrastracture.subexpression_finder.subexpression_finder_interface import (
    SubexpressionFinderInterface,
)


class Expression:
    def __init__(
        self,
        subexpression_finder: SubexpressionFinderInterface,
        operation_finder: OperationFinder,
        operation_sorter: OperationSorter,
        expression_string: str,
    ):
        self.subexpression_finder = subexpression_finder
        self.operation_finder = operation_finder
        self.operation_sorter = operation_sorter
        self.expression_string = expression_string

        self.position = None
        self.tail = None
        self.right_subexpression = None

    def solve_for_abscissa(self, abscissa: float):
        self.substitute_x_for_abscissa(abscissa)

        subexpressions = self.subexpression_finder.find_subexpressions(
            self.expression_string
        )
        self.set_right_subexpressions(subexpressions)
        for subexpression in subexpressions:
            solved_subexpression = subexpression.solve_for_abscissa(abscissa)
            self.expression_string = self.substitute_subexpression(
                self.expression_string, solved_subexpression, subexpression
            )

        operations = self.operation_finder.find_operations(self.expression_string)
        self.set_right_operations(operations)
        operations = self.operation_sorter.sort_by_priority(operations)
        for operation in operations:
            self.expression_string = operation.do_operation(self.expression_string)

        ordinate = self.format_ordinate(self.expression_string)

        if self.i_am_subexpression_and_there_is_another_following():
            post_substitution_shift_length = self.calculate_shift_length()
            self.right_subexpression.update_position_after_shift(
                post_substitution_shift_length
            )

        return ordinate

    def i_am_subexpression_and_there_is_another_following(self):
        i_am_subexpression = (
            self.position is not None
            and self.tail is not None
            and self.right_subexpression is not None
        )
        return i_am_subexpression

    @staticmethod
    def set_right_subexpressions(subexpressions):
        for counter, subexpression in enumerate(subexpressions[:-1]):
            right_subexpression = subexpressions[counter + 1]
            subexpression.set_right_subexpression(right_subexpression)

    def set_right_subexpression(self, right_subexpression):
        self.right_subexpression = right_subexpression

    @staticmethod
    def substitute_subexpression(
        expression_string, solved_subexpression, subexpression
    ):
        function_string_left_to_subexpression = expression_string[
            : subexpression.position - 1
        ]
        function_string_right_to_subexpression = expression_string[
            subexpression.tail + 1 :
        ]
        expression_string = (
            function_string_left_to_subexpression
            + str(solved_subexpression)
            + function_string_right_to_subexpression
        )
        return expression_string

    def calculate_shift_length(self):
        post_substitution_shift_length = (
            2 + self.tail - self.position - len(self.expression_string)
        )
        return post_substitution_shift_length

    def substitute_x_for_abscissa(self, abscissa: float):
        self.expression_string = self.expression_string.replace("x", str(abscissa))

    @staticmethod
    def set_right_operations(operations: [Operation]):
        for counter, operation in enumerate(operations[:-1]):
            right_operation = operations[counter + 1]
            operation.set_right_operation(right_operation)

    @staticmethod
    def format_ordinate(ordinate: str) -> float:
        return float(ordinate)

    def update_position_after_shift(self, post_substitution_shift_length: int):
        self.position -= post_substitution_shift_length
        self.tail -= post_substitution_shift_length
