import typer
import matplotlib.pyplot as plt

from function_analyzer.domain.abscissa import get_abscissas
from function_analyzer.infrastracture.operation_finder import OperationFinder
from function_analyzer.infrastracture.operation_sorter import OperationSorter
from function_analyzer.infrastracture.subexpression_finder.subexpression_finder import SubexpressionFinder
from function_analyzer.use_cases.calculate_function_ordinates import calculate_function_ordinates


def main(expression_string: str, from_domain: int = 0, to_domain: int = 100, domain_step: int = 1):
    subexpression_finder = SubexpressionFinder()
    operation_finder = OperationFinder()
    operation_sorter = OperationSorter()
    abscissas = get_abscissas(from_domain, to_domain, domain_step)
    ordinates = calculate_function_ordinates(subexpression_finder, operation_finder, operation_sorter,
                                             expression_string, abscissas)
    print_function_graph(abscissas, expression_string, ordinates)


def print_function_graph(abscissas, expression_string, ordinates):
    plt.plot(abscissas, ordinates)
    plt.title(expression_string)


if __name__ == '__main__':
    typer.run(main)
