from function_analyzer.domain.expression import Expression
from function_analyzer.infrastracture.operation_finder.operation_finder import OperationFinder
from function_analyzer.infrastracture.operation_sorter.operation_sorter import OperationSorter


def calculate_function_ordinate(operation_finder: OperationFinder, operation_sorter: OperationSorter,
                                abscissa: float, function_string: str) -> float:
    expression = Expression(operation_finder, operation_sorter, function_string)
    ordinate = expression.solve_for_abscissa(abscissa)
    return ordinate
