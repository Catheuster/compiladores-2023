from .AbstractCommand import AbstractCommand
from ..datastructures import IsiVariable


class CommandIf(AbstractCommand):
    def __init__(self, condition, trueList, falseList):
        self.condition = condition
        self.trueList = trueList
        self.falseList = falseList

    def generateJavaCode(self):
        str = ""
        str = f"if ({self.condition})" + " {\n"
        for command in self.trueList:
            str += command.generateJavaCode()
        str += "}"
        if self.falseList:
            str += "else {\n"
            for command in self.falseList:
                str += command.generateJavaCode()
            str += "}"
        else:
            str += "\n"
        return str

    def __str__(self):
        return f"CommandIf [condition={self.condition}, trueList={self.trueList}, falseList={self.falseList}]"
