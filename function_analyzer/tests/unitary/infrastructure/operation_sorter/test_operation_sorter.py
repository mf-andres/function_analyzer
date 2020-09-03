from function_analyzer.infrastracture.operation_sorter.operation_sorter import OperationSorter


def test_sorts_two_operations_by_increasing_position():
    class OperationMock:
        def __init__(self, sign_position: int):
            self.sign_position = sign_position

    first_operation = OperationMock(1)
    second_operation = OperationMock(5)
    operations = [first_operation, second_operation]
    operation_sorter = OperationSorter()
    sorted_operations = operation_sorter.sort_by_priority(operations)
    assert sorted_operations[0] is first_operation


def test_sorts_many_operations_by_increasing_position():
    class OperationMock:  # TODO use fixtures
        def __init__(self, sign_position: int):
            self.sign_position = sign_position

    first_operation = OperationMock(1)
    second_operation = OperationMock(2)
    third_operation = OperationMock(3)
    fourth_operation = OperationMock(4)
    operations = [fourth_operation, first_operation, third_operation, second_operation]
    operation_sorter = OperationSorter()
    sorted_operations = operation_sorter.sort_by_priority(operations)
    assert sorted_operations[3] is fourth_operation
