from operator import attrgetter

from function_analyzer.domain.operation.operation import Operation


class OperationSorter:
    def sort_by_priority(self, operations: [Operation]):
        operations = sorted(operations, key=attrgetter('sign_position'))
        return operations
