import math

import pytest

from function_analyzer.domain.domain import get_domain_len
from function_analyzer.infrastracture.operation_finder.operation_finder import OperationFinder
from function_analyzer.infrastracture.operation_sorter.operation_sorter import OperationSorter
from function_analyzer.infrastracture.subexpression_finder.subexpression_finder import SubexpressionFinder
from function_analyzer.use_cases.calculate_function_ordinates import calculate_function_ordinates, get_abscissas


@pytest.mark.parametrize("from_domain, to_domain, domain_step, expected_abscissas",
                         [
                             (0, 3, 1, [0, 1, 2]),
                             (0, 6, 2, [0, 2, 4]),
                             (0, 9, 3, [0, 3, 6]),
                         ])
def test_get_abscissas_returns_correct_abscissas(from_domain, to_domain, domain_step, expected_abscissas):
    abscissas = get_abscissas(from_domain, to_domain, domain_step)
    assert abscissas == expected_abscissas


def test_returns_as_many_ordinates_as_domain_len():
    subexpression_finder = SubexpressionFinder()
    operation_finder = OperationFinder()
    operation_sorter = OperationSorter()
    from_domain = 0
    to_domain = 100
    domain_step = 1
    expression_string = "x*(x-1)"
    ordinates = calculate_function_ordinates(subexpression_finder, operation_finder, operation_sorter,
                                             expression_string,
                                             from_domain, to_domain, domain_step)
    domain_len = get_domain_len(from_domain, to_domain, domain_step)
    assert len(ordinates) == domain_len

