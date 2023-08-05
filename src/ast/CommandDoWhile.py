from .AbstractCommand import AbstractCommand
from ..datastructures import IsiVariable


class CommandDoWhile(AbstractCommand):
    def __init__(self, condition, commandList):
        self.condition = condition
        self.commandList = commandList

    def generateJavaCode(self):
        str = ""
        str = "do {\n"
        for command in self.commandList:
            str += command.generateJavaCode()
        str += "} " + f"while ({self.condition});\n"
        return str

    def generatePythonCode(self):
        str = "while (True):\n"
        strhelp = ""
        for command in self.commandList:
            strhelp += command.generateJavaCode()
        strhelp = strhelp.replace("\n", "\n\t")
        strhelp = strhelp[:-2] #removing last \t
        str += "\t"+strhelp
        str += f"\tif {self.condition}:\n"
        str += "\t\t continue\n"
        str += "\telse:\n"
        str += "\t\tbreak\n"

        return str
    def generateJavaScriptCode(self):
        str = ""
        str = "do {\n"
        for command in self.commandList:
            str += command.generateJavaScriptCode()
        str += "} " + f"while ({self.condition});\n"
        return str

    def __str__(self):
        return f"CommandDoWhile [condition={self.condition}, whileList={self.commandList}]"
