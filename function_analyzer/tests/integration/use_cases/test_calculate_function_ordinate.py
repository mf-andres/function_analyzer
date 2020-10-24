from function_analyzer.infrastracture.operation_finder.operation_finder import OperationFinder
from function_analyzer.infrastracture.operation_sorter.operation_sorter import OperationSorter
from function_analyzer.use_cases.calculate_function_ordinate import calculate_function_ordinate


def test_calculate_function_ordinate_for_two_addends_addition():
    abscissa = 1
    function_string = 'x+1'
    operation_finder = OperationFinder()
    operation_sorter = OperationSorter()
    returned_ordinate = calculate_function_ordinate(operation_finder, operation_sorter, abscissa, function_string)
    expected_ordinate = 2
    assert returned_ordinate == expected_ordinate


def test_calculate_function_ordinate_for_many_addends_addition():
    abscissa = 1
    function_string = 'x+x+x+1'
    operation_finder = OperationFinder()
    operation_sorter = OperationSorter()
    returned_ordinate = calculate_function_ordinate(operation_finder, operation_sorter, abscissa, function_string)
    expected_ordinate = 4
    assert returned_ordinate == expected_ordinate


def test_calculate_function_ordinate_for_two_operands_substraction():
    abscissa = 1
    function_string = 'x-1'
    operation_finder = OperationFinder()
    operation_sorter = OperationSorter()
    returned_ordinate = calculate_function_ordinate(operation_finder, operation_sorter, abscissa, function_string)
    expected_ordinate = 0
    assert returned_ordinate == expected_ordinate


def test_calculate_function_ordinate_for_many_operands_substraction():
    abscissa = 1
    function_string = 'x-x-x-1'
    operation_finder = OperationFinder()
    operation_sorter = OperationSorter()
    returned_ordinate = calculate_function_ordinate(operation_finder, operation_sorter, abscissa, function_string)
    expected_ordinate = -2
    assert returned_ordinate == expected_ordinate


def test_calculate_function_ordinate_for_two_operands_multiplication():
    abscissa = 2
    function_string = 'x*x'
    operation_finder = OperationFinder()
    operation_sorter = OperationSorter()
    returned_ordinate = calculate_function_ordinate(operation_finder, operation_sorter, abscissa, function_string)
    expected_ordinate = 4
    assert returned_ordinate == expected_ordinate


def test_calculate_function_ordinate_for_three_operands_multiplication_bug():
    abscissa = 2
    function_string = '8.0*2*1'
    operation_finder = OperationFinder()
    operation_sorter = OperationSorter()
    returned_ordinate = calculate_function_ordinate(operation_finder, operation_sorter, abscissa, function_string)
    expected_ordinate = 16
    assert returned_ordinate == expected_ordinate


def test_calculate_function_ordinate_for_many_operands_multiplication():
    abscissa = 2
    function_string = 'x*x*x*x*1'
    operation_finder = OperationFinder()
    operation_sorter = OperationSorter()
    returned_ordinate = calculate_function_ordinate(operation_finder, operation_sorter, abscissa, function_string)
    expected_ordinate = 16
    assert returned_ordinate == expected_ordinate


def test_calculate_function_ordinate_for_two_operands_division():  # TODO duplicities everywhere
    abscissa = 2
    function_string = 'x/x'
    operation_finder = OperationFinder()
    operation_sorter = OperationSorter()
    returned_ordinate = calculate_function_ordinate(operation_finder, operation_sorter, abscissa, function_string)
    expected_ordinate = 1
    assert returned_ordinate == expected_ordinate
