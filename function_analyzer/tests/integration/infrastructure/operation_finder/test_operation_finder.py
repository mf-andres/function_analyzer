from function_analyzer.infrastracture.operation_finder.operation_finder import OperationFinder


def test_finds_two_additions():
    function_string = '1+1+1'
    operation_finder = OperationFinder(function_string)
    additions = operation_finder.find_additions()
    assert len(additions) == 2
