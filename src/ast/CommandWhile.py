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

    def __str__(self):
        return f"CommandWhile [condition={self.condition}, whileList={self.commandList}]"
