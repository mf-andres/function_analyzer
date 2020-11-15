from typing import List

from function_analyzer.use_cases.calculate_function_ordinate import calculate_function_ordinate


def calculate_function_ordinates(subexpression_finder, operation_finder, operation_sorter,
                                 expression_string: str, abscissas: List[float]):
    ordinates = list()
    for abscissa in abscissas:
        ordinate = calculate_function_ordinate(subexpression_finder, operation_finder, operation_sorter,
                                               abscissa, expression_string)
        ordinates.append(ordinate)
    return ordinates

# TODO when numbers are too great (100e+6) scientific notation breaks the program
