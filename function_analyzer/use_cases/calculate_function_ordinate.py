from function_analyzer.domain.expression import Expression
from function_analyzer.infrastracture.operation_finder.operation_finder import (
    OperationFinder,
)
from function_analyzer.infrastracture.operation_sorter.operation_sorter import (
    OperationSorter,
)
from function_analyzer.infrastracture.subexpression_finder.subexpression_finder_interface import (
    SubexpressionFinderInterface,
)


def calculate_function_ordinate(
    subexpression_finder: SubexpressionFinderInterface,
    operation_finder: OperationFinder,
    operation_sorter: OperationSorter,
    abscissa: float,
    function_string: str,
) -> float:
    expression = Expression(
        subexpression_finder, operation_finder, operation_sorter, function_string
    )
    ordinate = expression.solve_for_abscissa(abscissa)
    return ordinate
