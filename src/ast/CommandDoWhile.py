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

    def __str__(self):
        return f"CommandDoWhile [condition={self.condition}, whileList={self.commandList}]"
