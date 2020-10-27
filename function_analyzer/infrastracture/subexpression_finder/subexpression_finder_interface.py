import abc


class SubexpressionFinderInterface(abc.ABC):
    @staticmethod
    def find_subexpressions(expression_string: str):
        pass
