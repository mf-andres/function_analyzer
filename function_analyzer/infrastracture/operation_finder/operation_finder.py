from function_analyzer.infrastracture.operation.operation_factory import OperationFactory
from function_analyzer.domain.sign import Sign


class OperationFinder:
    def __init__(self):
        self.expression_string = None

    def set_expression_string(self, expression_string: str):
        self.expression_string = expression_string

    def find_operations(self):  # TODO throw exception if expression is not set
        operations = list()
        for character_position, character in enumerate(self.expression_string):
            if Sign.is_operation_sign(character_position, self.expression_string):
                operation = OperationFactory.create(character, character_position)
                operations.append(operation)
        return operations
