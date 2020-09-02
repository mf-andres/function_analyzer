from function_analyzer.domain.expression import Expression


def calculate_function_ordinate(operations_finder, abscissa: float, function_string: str) -> float:
    # TODO this substitution could go into expression
    function_string = substitute_x_for_abscissa(abscissa, function_string)
    expression = Expression(function_string)
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


def substitute_x_for_abscissa(abscissa: float, function_string: str) -> str:
    function_string = function_string.replace("x", str(abscissa))
    return function_string


def format_ordinate(ordinate: str) -> float:
    return float(ordinate)
