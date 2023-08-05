from .AbstractCommand import AbstractCommand
from ..datastructures import IsiVariable


class CommandWhile(AbstractCommand):
    def __init__(self, condition, commandList):
        self.condition = condition
        self.commandList = commandList

    def generateJavaCode(self):
        str = ""
        str = f"while ({self.condition})" + " {\n"
        for command in self.commandList:
            str += command.generateJavaCode()
        str += "}\n"
        return str

    def generatePythonCode(self):
        str = ""
        str = f"while {self.condition}:\n"
        strhelp = ""
        for command in self.commandList:
            strhelp += command.generatePythonCode()
        strhelp = strhelp.replace("\n", "\n\t")
        strhelp = strhelp[:-1]  # deleting last \t
        str += "\t"+strhelp
        return str

    def generateJavaScriptCode(self):
        str = ""
        str = f"while ({self.condition})" + " {\n"
        for command in self.commandList:
            str += command.generateJavaScriptCode()
        str += "}\n"
        return str
    def __str__(self):
        return f"CommandWhile [condition={self.condition}, whileList={self.commandList}]"
