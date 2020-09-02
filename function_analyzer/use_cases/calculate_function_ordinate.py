from function_analyzer.domain.expression import Expression


def calculate_function_ordinate(operations_finder, abscissa: float, function_string: str) -> float:
    expression = Expression(function_string)
    expression.substitute_x_for_abscissa(abscissa)
    operations_finder.set_expression(expression)
    operations = operations_finder.find_operations()
    set_right_operations(operations)
    substractions = operations_finder.get_substractions()
    additions = operations_finder.get_additions()
    for substraction in substractions:
        substraction.do_operation()
    for addition in additions:
        addition.do_operation()
    ordinate = format_ordinate(expression.expression_string)
    return ordinate


def set_right_operations(operations):
    for counter, operation in enumerate(operations[:-1]):
        right_operation = operations[counter + 1]
        operation.set_right_operation(right_operation)


def format_ordinate(ordinate: str) -> float:
    return float(ordinate)
