from ..datastructures import IsiSymbolTable
from ..ast import AbstractCommand
import os

class IsiProgram:
    def __init__(self):
        self.variableTable = IsiSymbolTable.IsiSymbolTable
        self.commands = []
        self.programName = None

    def generateTarget(self):
        str = ""
        str += "import java.util.Scanner;\n\n"
        str += "public class MainClass {\n"
        str += "public static void main(String[] args) {\n"

        str += "\nScanner scanner = new Scanner(System.in);\n\n"

        for symbol in self.variableTable.getAll():
            str += symbol.generateJavaCode() + "\n"

        str += "\n"

        for command in self.commands:
            str += command.generateJavaCode() + "\n"
        str += "}\n"
        str += "}\n"

        str = str.replace("verdadeiro", "true").replace("falso", "false")

        try:
            with open("MainClass.java", "w") as file:
                file.write(str)
        except Exception as ex:
            print("Error:", ex)

    def getVariableTable(self):
        return self.variableTable

    def setVariableTable(self, variableTable):
        self.variableTable = variableTable

    def getCommands(self):
        return self.commands

    def setCommands(self, commands):
        self.commands = commands

    def getProgramName(self):
        return self.programName

    def setProgramName(self, programName):
        self.programName = programName
