from function_analyzer.infrastracture.operation_sorter import (
    OperationSorter,
)


def test_sorts_two_operations_by_increasing_position():
    class OperationMock:  # TODO use fixtures
        def __init__(self, sign_position: int, sign_priority: int):
            self.sign_position = sign_position
            self.sign_priority = sign_priority

    first_operation = OperationMock(1, 1)
    second_operation = OperationMock(5, 1)
    operations = [first_operation, second_operation]
    operation_sorter = OperationSorter()
    sorted_operations = operation_sorter.sort_by_priority(operations)
    assert sorted_operations[0] is first_operation


def test_sorts_many_operations_by_increasing_position():
    class OperationMock:  # TODO use fixtures
        def __init__(self, sign_position: int, sign_priority: int):
            self.sign_position = sign_position
            self.sign_priority = sign_priority

    first_operation = OperationMock(1, 1)
    second_operation = OperationMock(2, 1)
    third_operation = OperationMock(3, 1)
    fourth_operation = OperationMock(4, 1)
    operations = [fourth_operation, first_operation, third_operation, second_operation]
    operation_sorter = OperationSorter()
    sorted_operations = operation_sorter.sort_by_priority(operations)
    expected_sorted_operations = [
        first_operation,
        second_operation,
        third_operation,
        fourth_operation,
    ]
    assert sorted_operations == expected_sorted_operations


def test_sort_two_operations_by_priority_first_then_position():
    class OperationMock:  # TODO use fixtures
        def __init__(self, sign_position: int, sign_priority: int):
            self.sign_position = sign_position
            self.sign_priority = sign_priority

    first_operation = OperationMock(2, 1)
    second_operation = OperationMock(1, 2)
    operations = [second_operation, first_operation]
    operation_sorter = OperationSorter()
    sorted_operations = operation_sorter.sort_by_priority(operations)
    assert sorted_operations[0] is first_operation


def test_sort_many_operations_by_priority_first_then_position():
    class OperationMock:  # TODO use fixtures
        def __init__(self, sign_position: int, sign_priority: int):
            self.sign_position = sign_position
            self.sign_priority = sign_priority

    first_operation = OperationMock(1, 1)
    second_operation = OperationMock(2, 1)
    third_operation = OperationMock(3, 2)
    fourth_operation = OperationMock(4, 2)
    operations = [third_operation, fourth_operation, second_operation, first_operation]
    operation_sorter = OperationSorter()
    sorted_operations = operation_sorter.sort_by_priority(operations)
    expected_sorted_operations = [
        first_operation,
        second_operation,
        third_operation,
        fourth_operation,
    ]
    assert sorted_operations == expected_sorted_operations
