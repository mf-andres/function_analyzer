from function_analyzer.domain.operation.operation import Operation
from function_analyzer.infrastracture.operand_finder.operand_finder import find_left_operand_position, \
    find_right_operand_tail_position, find_left_operand, find_right_operand
from function_analyzer.infrastracture.sign_finder.sign_finder import find_sign_position
from function_analyzer.use_cases.calculate_function_ordinate import do_operations_recursively


class Substraction(Operation):
    SUBSTRACTION_SIGN = '-'

    @staticmethod
    def operation_found(function_string):
        return function_string.find('-') >= 0

    @staticmethod
    def do_operation(function_string):
        sign_position = find_sign_position(function_string, Substraction.SUBSTRACTION_SIGN)
        left_operand_position = find_left_operand_position(function_string, sign_position)
        right_operand_tail_position = find_right_operand_tail_position(function_string, sign_position)
        left_operand = find_left_operand(function_string, sign_position, left_operand_position)
        right_operand = find_right_operand(function_string, sign_position, right_operand_tail_position)
        partial_result = Substraction.calculate_partial_result(left_operand, right_operand)
        function_string = Operation.substitute_operation_for_partial_result(function_string,
                                                                            left_operand_position,
                                                                            right_operand_tail_position,
                                                                            partial_result)
        return function_string

    @staticmethod
    def calculate_partial_result(left_operand, right_operand):
        partial_result = float(left_operand) - float(right_operand)
        return partial_result

