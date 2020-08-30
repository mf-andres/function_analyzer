def calculate_function_ordinate(operations_finder, abscissa: float, function_string: str) -> float:
    function_string = substitute_x_for_abscissa(abscissa, function_string)
    # TODO substitute x for abscissa should be also update the function_string under operations_finder object
    operations_finder.function_string = function_string
    substractions = operations_finder.find_substractions()
    additions = operations_finder.find_additions()
    for substraction in substractions:
        function_string = substraction.do_operation()
    for addition in additions:
        function_string = addition.do_operation()
    ordinate = format_ordinate(function_string)
    return ordinate


def substitute_x_for_abscissa(abscissa: float, function_string: str) -> str:
    function_string = function_string.replace("x", str(abscissa))
    return function_string


def format_ordinate(ordinate: str) -> float:
    return float(ordinate)
