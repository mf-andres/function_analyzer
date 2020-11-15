from function_analyzer.domain.operand import Operand
from function_analyzer.domain.sign import Sign
from function_analyzer.infrastracture.sign_finder import SignFinder


class OperandFinder:
    @staticmethod
    def find_left_operand(function_string, sign_position) -> Operand:
        left_operand_position = OperandFinder.find_left_operand_position(
            function_string, sign_position
        )
        left_operand_tail = sign_position
        left_operand_string = function_string[left_operand_position:sign_position]
        left_operand_string = Operand(
            left_operand_position, left_operand_string, left_operand_tail
        )
        return left_operand_string

    @staticmethod
    def find_right_operand(function_string, sign_position) -> Operand:
        right_operand_position = sign_position + 1
        right_operand_tail = OperandFinder.find_right_operand_tail(
            function_string, sign_position
        )
        right_operand = function_string[right_operand_position:right_operand_tail]
        right_operand = Operand(
            right_operand_position, right_operand, right_operand_tail
        )
        return right_operand

    @staticmethod
    def find_left_operand_position(function_string, sign_position):
        left_sign_or_end_position = SignFinder.find_left_sign_or_end_position(
            function_string, sign_position
        )

        if left_sign_or_end_position == 0:
            return left_sign_or_end_position

        if Sign.is_sign_of_negative_operand(left_sign_or_end_position, function_string):
            return left_sign_or_end_position

        return left_sign_or_end_position + 1

    @staticmethod
    def find_right_operand_tail(function_string, sign_position):
        right_sign_or_end_position = SignFinder.find_right_sign_or_end_position(
            function_string, sign_position
        )
        right_operand_tail_position = right_sign_or_end_position
        return right_operand_tail_position
