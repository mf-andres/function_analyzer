from function_analyzer.domain.operation.addition import Addition
from function_analyzer.domain.operation.substraction import Substraction


class OperationFactory:
    @staticmethod
    def create(sign, expression, sign_position):
        if sign == '-':
            return Substraction(expression, sign_position)
        elif sign == '+':
            return Addition(expression, sign_position)
        else:
            raise NotImplementedError
