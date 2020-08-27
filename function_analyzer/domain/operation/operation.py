from abc import ABC, abstractmethod


class Operation(ABC):
    @staticmethod
    @abstractmethod
    def operation_found(function_string):
        pass

    @staticmethod
    @abstractmethod
    def do_operation(function_string):
        pass

    @staticmethod
    @abstractmethod
    def calculate_partial_result(left_operand, right_operand):
        pass

    @staticmethod
    def substitute_operation_for_partial_result(function_string,
                                                left_operand_position,
                                                right_operand_tail,
                                                partial_result):
        function_string_left_to_operation = function_string[:left_operand_position]
        function_string_right_to_operation = function_string[right_operand_tail:]
        function_string = function_string_left_to_operation \
                          + str(partial_result) \
                          + function_string_right_to_operation
        return function_string
