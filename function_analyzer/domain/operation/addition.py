from function_analyzer.domain.operation.operation import Operation
from function_analyzer.infrastracture.operand_finder.operand_finder import find_left_operand_position, \
    find_right_operand_tail_position, find_left_operand, find_right_operand


class Addition(Operation):
    def calculate_partial_result(self, left_operand, right_operand):
        partial_result = float(left_operand) + float(right_operand)
        return partial_result

