from function_analyzer.domain.operation.operation import Operation
from function_analyzer.domain.sign import is_sign
from function_analyzer.infrastracture.errors.errors import SignMisinterpretationError
from function_analyzer.infrastracture.operand_finder.operand_finder import find_left_operand_position, \
    find_right_operand_tail_position, find_left_operand, find_right_operand


class Substraction(Operation):
    def __init__(self, function_string, sign_position):
        super().__init__(function_string, sign_position)
        if self.created_from_sign_of_negative_operand():
            raise SignMisinterpretationError()

    def created_from_sign_of_negative_operand(self):  # TODO private and public methods
        if self.sign_position == 0:
            return True
        elif self.previous_character_is_sign(self.sign_position):
            return True
        else:
            return False

    def previous_character_is_sign(self, sign_position):  # TODO could go elsewhere
        return is_sign(self.function_string[sign_position - 1])

    def calculate_partial_result(self, left_operand, right_operand):
        partial_result = float(left_operand) - float(right_operand)
        return partial_result
