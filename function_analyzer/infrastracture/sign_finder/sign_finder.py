from function_analyzer.domain.sign import Sign


class SignFinder:
    @staticmethod
    def find_left_sign_or_end_position(function_string, sign_position):
        left_substring = function_string[:sign_position]
        if Sign.contains_sign(left_substring):
            reversed_left_substring = left_substring[::-1]
            first_sign_position_in_reversed_left_substring = SignFinder.find_first_sign_position_in_string(
                reversed_left_substring)
            left_sign_position = SignFinder.get_string_position_from_left_substring_position(
                first_sign_position_in_reversed_left_substring, sign_position)
            return left_sign_position
        else:
            end_position = 0
            return end_position

    @staticmethod
    def find_right_sign_or_end_position(function_string, sign_position):
        sign_position_tail = sign_position + 1
        right_substring = function_string[sign_position_tail:]
        if Sign.contains_operation_sign(right_substring):
            first_operation_sign_position_in_right_substring = SignFinder.find_first_operation_sign_position_in_string(
                right_substring
            )
            right_sign_position = SignFinder.get_string_position_from_right_substring_position(
                first_operation_sign_position_in_right_substring, sign_position)
            return right_sign_position
        else:
            end_position = len(function_string)
            return end_position

    @staticmethod
    def get_string_position_from_left_substring_position(first_sign_position_in_reversed_left_substring, sign_position):
        left_sign_or_end_position = sign_position - 1 - first_sign_position_in_reversed_left_substring
        return left_sign_or_end_position

    @staticmethod
    def get_string_position_from_right_substring_position(first_sign_position_in_right_substring, sign_position):
        right_sign_or_end_position = sign_position + 1 + first_sign_position_in_right_substring
        return right_sign_or_end_position

    @staticmethod
    def find_first_sign_position_in_string(string):
        character_position = 0
        for character in string:
            if Sign.is_sign(character):
                return character_position
            else:
                character_position += 1
        raise ValueError("No sign in string")

    @staticmethod
    def find_first_operation_sign_position_in_string(function_string):
        for character_position, character in enumerate(function_string):
            if Sign.is_operation_sign(character_position, function_string):
                return character_position
        raise ValueError("No sign in string")
