from function_analyzer.domain.expression import Expression
from function_analyzer.infrastracture.operation_finder.operation_finder import OperationFinder
from function_analyzer.infrastracture.operation_sorter.operation_sorter import OperationSorter


def calculate_function_ordinate(operation_finder: OperationFinder, operation_sorter: OperationSorter,
                                abscissa: float, function_string: str) -> float:
    expression = Expression(function_string)
    expression.substitute_x_for_abscissa(abscissa)
    operation_finder.set_expression(expression)
    operations = operation_finder.find_operations()
    set_right_operations(operations)
    operations = operation_sorter.sort_by_priority(operations)
    function_string = expression.expression_string  # TODO do it all under expression
    for operation in operations:
        function_string = operation.do_operation(function_string)
    ordinate = format_ordinate(function_string)
    return ordinate


def set_right_operations(operations):
    for counter, operation in enumerate(operations[:-1]):
        right_operation = operations[counter + 1]
        operation.set_right_operation(right_operation)


def format_ordinate(ordinate: str) -> float:
    return float(ordinate)
