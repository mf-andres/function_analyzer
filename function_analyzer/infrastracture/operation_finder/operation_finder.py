from function_analyzer.domain.operation.addition import Addition
from function_analyzer.domain.operation.operation_factory import OperationFactory
from function_analyzer.domain.operation.substraction import Substraction
from function_analyzer.domain.sign import is_operation_sign


class OperationFinder:
    def __init__(self):
        self.expression = None
        self.operations = None  # TODO remove?

    def set_expression(self, expression):
        self.expression = expression

    def find_operations(self):  # TODO throw exception if expression is not set
        operations = list()
        for character_position, character in enumerate(self.expression.expression_string):
            if is_operation_sign(character_position, self.expression.expression_string):
                    operation = OperationFactory.create(character, character_position)
                    operations.append(operation)
        self.operations = operations
        return operations

    def get_substractions(self):  # TODO throw exception if operations not set / refactor
        substractions = list()
        for operation in self.operations:
            if isinstance(operation, Substraction):
                substractions.append(operation)
        return substractions

    def get_additions(self):
        additions = list()
        for operation in self.operations:
            if isinstance(operation, Addition):
                additions.append(operation)
        return additions
