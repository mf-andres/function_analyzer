from function_analyzer.domain.domain import get_domain_len
from function_analyzer.use_cases.calculate_function_ordinate import calculate_function_ordinate  # TODO domain service


def calculate_function_ordinates(subexpression_finder, operation_finder, operation_sorter,
                                 expression_string: str,
                                 from_domain: int = 0, to_domain: int = 100, domain_step: int = 1):
    assert to_domain > from_domain  # TODO domain exception

    ordinates = list()
    abscissas = get_abscissas(from_domain, to_domain, domain_step)
    for abscissa in abscissas:
        ordinate = calculate_function_ordinate(subexpression_finder, operation_finder, operation_sorter,
                                               abscissa, expression_string)
        ordinates.append(ordinate)
    return ordinates


def get_abscissas(from_domain: int, to_domain: int, domain_step: int):
    abscissas = list()
    domain_len = get_domain_len(from_domain, to_domain, domain_step)
    abscissa = from_domain
    abscissas.append(abscissa)
    for _ in range(domain_len - 1):
        abscissa += domain_step
        abscissas.append(abscissa)
    return abscissas


# TODO when numbers are too great (100e+6) scientific notation breaks the program
