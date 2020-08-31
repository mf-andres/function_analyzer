from function_analyzer.domain.operation.addition import Addition
from function_analyzer.domain.operation.substraction import Substraction


class OperationFactory:
    @staticmethod
    def create(sign, function_string, sign_position):
        if sign == '-':
            return Substraction(function_string, sign_position)
        elif sign == '+':
            return Addition(function_string, sign_position)
        else:
            raise NotImplementedError
