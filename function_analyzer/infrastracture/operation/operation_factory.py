from function_analyzer.domain.sign import Sign
from function_analyzer.infrastracture.operation.addition import Addition
from function_analyzer.infrastracture.operation.substraction import Substraction


class OperationFactory:
    @staticmethod
    def create(sign: str, sign_position: int):
        if sign == Sign.SUBSTRACTION_CHARACTER:
            return Substraction(sign_position, Sign.SUBSTRACTION_PRIORITY)
        elif sign == Sign.ADDITION_CHARACTER:
            return Addition(sign_position, Sign.ADDITION_PRIORITY)
        else:
            raise NotImplementedError
