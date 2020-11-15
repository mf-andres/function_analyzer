from function_analyzer.domain.operation import Operation


# TODO make domain services and just unit test the use cases
class OperationSorter:
    def sort_by_priority(self, operations: [Operation]):
        operations = sorted(
            operations, key=lambda x: (x.sign_priority, x.sign_position)
        )
        return operations
