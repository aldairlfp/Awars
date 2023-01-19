class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass

class FloatStringException(Exception):
    pass

class InvalidArgumentsException(Exception):
    pass

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value
