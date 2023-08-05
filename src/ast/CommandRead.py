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
            return f"{self.identifier} = float(input())\n"
        else:
            return f"{self.identifier} = input()\n"

    def generateJavaScriptCode(self):
        if self.variable.getType() == IsiVariable.IsiVariable.NUMBER:
            return f"{self.identifier} = parseFloat(prompt());\n"
        else:
            return f"{self.identifier} = prompt();\n"
    def __str__(self):
        return f"CommandRead [id={self.identifier}]"
