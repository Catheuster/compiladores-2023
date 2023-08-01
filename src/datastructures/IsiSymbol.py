from abc import ABC, abstractmethod


class IsiSymbol(ABC):
    def __init__(self, identifier):
        self.identifier = identifier

    def getID(self):
        return self.identifier

    def setID(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return f"IsiSymbol [ID={self.identifier}]"

    @abstractmethod
    def generateJavaCode(self):
        return
