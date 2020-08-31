from function_analyzer.infrastracture.operand_finder.operand_finder import find_left_operand_position, \
    find_right_operand_tail_position, find_left_operand, find_right_operand


class Operation:
    def __init__(self, function_string, sign_position):
        self.function_string = function_string
        self.sign_position = sign_position
        # TODO left operation
        self.right_operation = None
        # TODO left operand
        # TODO right operand

    def do_operation(self):
        left_operand_position = find_left_operand_position(self.function_string, self.sign_position)
        right_operand_tail_position = find_right_operand_tail_position(self.function_string, self.sign_position)
        left_operand = find_left_operand(self.function_string, self.sign_position, left_operand_position)
        right_operand = find_right_operand(self.function_string, self.sign_position, right_operand_tail_position)
        partial_result = self.calculate_partial_result(left_operand, right_operand)
        modified_function_string = self.substitute_operation_for_partial_result(left_operand_position,
                                                                                right_operand_tail_position,
                                                                                partial_result)
        if self.right_operation is not None:
            post_substitution_shift_length = len(left_operand) + len(right_operand) + 1 - len(partial_result)
            self.right_operation.update_positions_after_shift(post_substitution_shift_length)
        return modified_function_string

    def calculate_partial_result(self, left_operand, right_operand) -> str:
        pass

    def substitute_operation_for_partial_result(self,
                                                left_operand_position,
                                                right_operand_tail,
                                                partial_result):
        function_string_left_to_operation = self.function_string[:left_operand_position]
        function_string_right_to_operation = self.function_string[right_operand_tail:]
        function_string = function_string_left_to_operation \
                          + partial_result \
                          + function_string_right_to_operation
        return function_string

    def set_right_operation(self, right_operation):
        self.right_operation = right_operation

    def update_positions_after_shift(self, shift_length):
        self.sign_position -= shift_length
