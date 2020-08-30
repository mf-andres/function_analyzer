from function_analyzer.domain.operation.operation import Operation
from function_analyzer.infrastracture.operand_finder.operand_finder import find_left_operand_position, \
    find_right_operand_tail_position, find_left_operand, find_right_operand


class Addition(Operation):
    def __init__(self, function_string, sign_position):
        self.function_string = function_string
        self.sign_position = sign_position

    def do_operation(self):
        left_operand_position = find_left_operand_position(self.function_string, self.sign_position)
        right_operand_tail_position = find_right_operand_tail_position(self.function_string, self.sign_position)
        left_operand = find_left_operand(self.function_string, self.sign_position, left_operand_position)
        right_operand = find_right_operand(self.function_string, self.sign_position, right_operand_tail_position)
        partial_result = Addition.calculate_partial_result(left_operand, right_operand)
        function_string = Operation.substitute_operation_for_partial_result(self.function_string,
                                                                            left_operand_position,
                                                                            right_operand_tail_position,
                                                                            partial_result)
        return function_string

    @staticmethod
    def calculate_partial_result(left_operand, right_operand):
        partial_result = float(left_operand) + float(right_operand)
        return partial_result
