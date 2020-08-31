from function_analyzer.domain.operation.operation import Operation
from function_analyzer.domain.sign import is_sign
from function_analyzer.infrastracture.errors.errors import SignMisinterpretationError
from function_analyzer.infrastracture.operand_finder.operand_finder import find_left_operand_position, \
    find_right_operand_tail_position, find_left_operand, find_right_operand


class Substraction(Operation):
    def __init__(self, function_string, sign_position):
        self.function_string = function_string
        self.sign_position = sign_position
        self.right_operation = None
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

    def do_operation(self):
        left_operand_position = find_left_operand_position(self.function_string, self.sign_position)
        right_operand_tail_position = find_right_operand_tail_position(self.function_string, self.sign_position)
        left_operand = find_left_operand(self.function_string, self.sign_position, left_operand_position)
        right_operand = find_right_operand(self.function_string, self.sign_position, right_operand_tail_position)
        partial_result = Substraction.calculate_partial_result(left_operand, right_operand)
        function_string = Operation.substitute_operation_for_partial_result(self.function_string,
                                                                            left_operand_position,
                                                                            right_operand_tail_position,
                                                                            partial_result)
        post_substitution_shift_length = len(left_operand) + len(right_operand)
        self.right_operation.update(post_substitution_shift_length)
        return function_string

    @staticmethod
    def calculate_partial_result(left_operand, right_operand):
        partial_result = float(left_operand) - float(right_operand)
        return partial_result

    def set_right_operation(self, right_operation):
        self.right_operation = right_operation

    def update(self, shift_lenght):
        self.sign_position -= shift_lenght
