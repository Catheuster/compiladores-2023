from .AbstractCommand import AbstractCommand
from ..datastructures import IsiVariable


class CommandWrite(AbstractCommand):
    def __init__(self, identifier):
        self.identifier = identifier

    def generateJavaCode(self):
        return "System.out.println(" + self.identifier + ");\n"

    def generatePythonCode(self):
        return "print("+self.identifier+")\n"

    def generateJavaScriptCode(self):
        return "alert("+self.identifier+");\n"

    def __str__(self):
        return f"CommandWrite [id={self.identifier}]"
