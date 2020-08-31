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
        function_string = self.substitute_operation_for_partial_result(left_operand_position,
                                                                       right_operand_tail_position,
                                                                       partial_result)
        post_substitution_shift_length = len(left_operand) + len(right_operand)
        self.right_operation.update(post_substitution_shift_length)
        return function_string

    def calculate_partial_result(self, left_operand, right_operand):
        pass

    def substitute_operation_for_partial_result(self,
                                                left_operand_position,
                                                right_operand_tail,
                                                partial_result):
        function_string_left_to_operation = self.function_string[:left_operand_position]
        function_string_right_to_operation = self.function_string[right_operand_tail:]
        function_string = function_string_left_to_operation \
                          + str(partial_result) \
                          + function_string_right_to_operation
        return function_string

    def set_right_operation(self, right_operation):
        self.right_operation = right_operation

    def update(self, shift_lenght):
        self.sign_position -= shift_lenght
