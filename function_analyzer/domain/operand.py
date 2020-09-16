class Operand:
    def __init__(self, position, operand, tail):
        self.position = position
        self.operand = operand
        self.tail = tail

    def __eq__(self, other):
        if self.position != other.position:
            return False
        elif self.operand != other.operand:
            return False
        elif self.tail != other.tail:
            return False
        else:
            return True
