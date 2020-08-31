from function_analyzer.domain.operation.addition import Addition
from function_analyzer.domain.operation.operation_factory import OperationFactory
from function_analyzer.domain.operation.substraction import Substraction
from function_analyzer.domain.sign import is_sign
from function_analyzer.infrastracture.errors.errors import SignMisinterpretationError


class OperationFinder:
    def __init__(self, function_string):  # TODO make expression object?
        self.function_string = function_string

    def find_operations(self):
        operations = list()
        for character_position, character in enumerate(self.function_string):
            if is_sign(character):
                try:
                    operation = OperationFactory.create(character, self.function_string, character_position)
                    operations.append(operation)
                except SignMisinterpretationError:
                    continue
        return operations
