from function_analyzer.domain.operation.addition import Addition
from function_analyzer.domain.operation.substraction import Substraction


class OperationFinder:
    def __init__(self, function_string):
        self._function_string = function_string

    def __find_operation(self, operation_sign, operation_class):
        operations = list()
        for character_position, character in enumerate(self._function_string):
            if character == operation_sign:
                operation = operation_class(self._function_string, character_position)
                operations.append(operation)
        return operations

    def find_substractions(self):
        substractions = self.__find_operation('-', Substraction)  # TODO remove literal
        return substractions

    def find_additions(self):
        additions = self.__find_operation('+', Addition)  # TODO remove literal
        return additions