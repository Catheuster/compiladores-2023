from typing import Dict
from .IsiSymbol import IsiSymbol

class IsiSymbolTable:
    def __init__(self):
        self.symbolTable: Dict[str, IsiSymbol] = {}

    def add(self, symbol):
        self.symbolTable[symbol.getID()] = symbol

    def exists(self, symbol: str) -> bool:
        return symbol in self.symbolTable

    def get(self, symbol: str) -> IsiSymbol:
        return self.symbolTable.get(symbol)

    def getAll(self):
        return self.symbolTable.values()
