def calculate_function_ordinate(operations_finder, substraction, addition, abscissa: float, function_string: str) -> float:
    function_string = substitute_x_for_abscissa(abscissa, function_string)
    substractions = operations_finder.find_substractions(function_string)
    additions = operations_finder.find_additions(function_string)
    ordinate = do_operations_recursively(substraction, addition, function_string)
    ordinate = format_ordinate(ordinate)
    return ordinate


def substitute_x_for_abscissa(abscissa: float, function_string: str) -> str:
    function_string = function_string.replace("x", str(abscissa))
    return function_string


def do_operations_recursively(substraction, addition, function_string: str) -> str:  # TODO find_operations
    if substraction.operation_found(function_string):
        function_string = substraction.do_operation(function_string)
        function_string = do_operations_recursively(substraction, addition, function_string)
        return function_string
    if addition.operation_found(function_string):
        function_string = addition.do_operation(function_string)
        function_string = do_operations_recursively(substraction, addition, function_string)
        return function_string
    else:
        return function_string


def format_ordinate(ordinate: str) -> float:
    return float(ordinate)
