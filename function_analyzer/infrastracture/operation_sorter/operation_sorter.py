from function_analyzer.domain.operation import Operation


class OperationSorter:
    def sort_by_priority(self, operations: [Operation]):
        operations = sorted(operations, key=lambda x: (x.sign_priority, x.sign_position))
        return operations
