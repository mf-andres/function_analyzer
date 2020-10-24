class Sign:
    DIVISION_CHARACTER = '/'
    MULTIPLICATION_CHARACTER = '*'
    SUBSTRACTION_CHARACTER = '-'
    ADDITION_CHARACTER = '+'

    DIVISION_PRIORITY = 1
    MULTIPLICATION_PRIORITY = 2
    SUBSTRACTION_PRIORITY = 3
    ADDITION_PRIORITY = 4

    SIGNS = [DIVISION_CHARACTER, MULTIPLICATION_CHARACTER, SUBSTRACTION_CHARACTER, ADDITION_CHARACTER]

    @staticmethod
    def is_sign(character: str):
        if character in Sign.SIGNS:
            return True
        else:
            return False

    @staticmethod
    def contains_sign(string: str):
        answer = False
        for character in string:
            if Sign.is_sign(character):
                answer = True
        return answer

    @staticmethod
    def is_operation_sign(sign_position, function_string):
        sign = function_string[sign_position]
        if not Sign.is_sign(sign):
            return False
        elif Sign.is_sign_of_negative_operand(sign_position, function_string):
            return False
        else:
            return True

    @staticmethod
    def is_sign_of_negative_operand(sign_position, function_string):
        if sign_position == 0:
            return True
        elif Sign.__previous_character_is_sign(sign_position, function_string):
            return True
        else:
            return False

    @staticmethod
    def __previous_character_is_sign(sign_position, function_string):
        return Sign.is_sign(function_string[sign_position - 1])
