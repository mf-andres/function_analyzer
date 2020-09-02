class Expression:
    def __init__(self, expression_string: str):
        self.expression_string = expression_string

    def substitute_x_for_abscissa(self, abscissa: float):
        self.expression_string = self.expression_string.replace("x", str(abscissa))
