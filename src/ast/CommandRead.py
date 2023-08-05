from .AbstractCommand import AbstractCommand
from ..datastructures import IsiVariable


class CommandRead(AbstractCommand):
    def __init__(self, identifier, variable):
        self.identifier = identifier
        self.variable = variable

    def generateJavaCode(self):
        if self.variable.getType() == IsiVariable.IsiVariable.NUMBER:
            return f"{self.identifier} = scanner.nextDouble();\n"
        else:
            return f"{self.identifier} = scanner.nextLine();\n"

    def generatePythonCode(self):
        if self.variable.getType() == IsiVariable.IsiVariable.NUMBER:
            return f"{self.identifier} = double(input())\n"
        else:
            return f"{self.identifier} = input()\n"

    def generateJavaScripCode(self):
        if self.variable.getType() == IsiVariable.IsiVariable.NUMBER:
            return f"{self.identifier} = readFloat(prompt);\n"
        else:
            return f"{self.identifier} = readLine(prompt);\n"
    def __str__(self):
        return f"CommandRead [id={self.identifier}]"
