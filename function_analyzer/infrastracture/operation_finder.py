from function_analyzer.domain.operation.operation_factory import (
    OperationFactory,
)
from function_analyzer.domain.sign import Sign


class OperationFinder:
    @staticmethod
    def find_operations(expression_string):
        operations = list()
        for character_position, character in enumerate(expression_string):
            if Sign.is_operation_sign(character_position, expression_string):
                operation = OperationFactory.create(character, character_position)
                operations.append(operation)
        return operations
