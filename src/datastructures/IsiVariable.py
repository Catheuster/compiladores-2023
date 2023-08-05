from .IsiSymbol import IsiSymbol


class IsiVariable(IsiSymbol):
    NUMBER = 0
    TEXT = 1
    BOOL = 2

    def __init__(self, identifier, type, value):
        super().__init__(identifier)
        self.type = type
        self.value = value

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def __str__(self):
        return f"IsiVariable [name={self.identifier}, type={self.type}, value={self.value}]"

    def generateJavaCode(self):
        if self.type == IsiVariable.NUMBER:
            return f"double {self.identifier};\n"
        if self.type == IsiVariable.TEXT:
            return f"String {self.identifier};\n"
        else:
            return f"boolean {self.identifier};\n"

    def generatePythonCode(self):
        return f"{self.identifier}=None\n"

    def generateJavaScriptCode(self):
        return f"{self.identifier}=null;\n"
