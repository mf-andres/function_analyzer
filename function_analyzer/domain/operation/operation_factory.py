from function_analyzer.domain.operation.addition import Addition
from function_analyzer.domain.operation.substraction import Substraction


class OperationFactory:
    @staticmethod
    def create(sign: str, sign_position: int):
        if sign == '-':  # TODO remove literals
            return Substraction(sign_position, 1)  # TODO deal better with the priority
        elif sign == '+':
            return Addition(sign_position, 2)
        else:
            raise NotImplementedError
