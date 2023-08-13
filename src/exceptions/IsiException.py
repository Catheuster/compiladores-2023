class IsiSemanticException(RuntimeError):
    def __init__(self, msg):
        super().__init__(msg)

class IsiSyntaxException(IsiSemanticException):
    def __init__(self, msg):
        super().__init__(msg)