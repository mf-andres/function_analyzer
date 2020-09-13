from function_analyzer.domain.operation import Operation
from function_analyzer.infrastracture.operation_finder.operation_finder import OperationFinder
from function_analyzer.infrastracture.operation_sorter.operation_sorter import OperationSorter


class Expression:
    def __init__(self, operation_finder: OperationFinder, operation_sorter: OperationSorter, expression_string: str):
        self.operation_finder = operation_finder
        self.operation_sorter = operation_sorter
        self.expression_string = expression_string

    def solve_for_abscissa(self, abscissa: float):
        self.substitute_x_for_abscissa(abscissa)
        self.operation_finder.set_expression_string(self.expression_string)
        operations = self.operation_finder.find_operations()
        self.set_right_operations(operations)
        operations = self.operation_sorter.sort_by_priority(operations)
        for operation in operations:
            self.expression_string = operation.do_operation(self.expression_string)
        ordinate = self.format_ordinate(self.expression_string)
        return ordinate

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
