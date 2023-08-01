from .AbstractCommand import AbstractCommand
from ..datastructures import IsiVariable


class CommandAssign(AbstractCommand):
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def generateJavaCode(self):
        return f"{self.identifier} = {self.expression};\n"

    def __str__(self):
        return f"CommandAssign [id={self.identifier}, expr={self.expression}]"