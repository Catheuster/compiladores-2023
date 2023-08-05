from ..datastructures import IsiSymbolTable
from ..ast import AbstractCommand
import os

class IsiProgram:
    def __init__(self):
        self.variableTable = IsiSymbolTable.IsiSymbolTable
        self.commands = []
        self.programName = None

    def generateJavaTarget(self):
        str = ""
        str += "import java.util.Scanner;\n\n"
        str += "public class MainClass {\n"
        str += "public static void main(String[] args) {\n"

        str += "\nScanner scanner = new Scanner(System.in);\n\n"

        for symbol in self.variableTable.getAll():
            str += symbol.generateJavaCode()

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

    def generatePythonTarget(self):
        str=""
        for symbol in self.variableTable.getAll():
            str += symbol.generatePythonCode()
        str += "\n"
        for command in self.commands:
            str += command.generatePythonCode() + "\n"
        str = str.replace("verdadeiro", "True").replace("falso", "False")
        str = str.replace(" && ", " and ").replace(" || "," or ")
        try:
            with open("MainScript.py", "w") as file:
                file.write(str)
        except Exception as ex:
            print("Error:", ex)

    def generateJavaScriptTarget(self):
        str=""
        for symbol in self.variableTable.getAll():
            str += symbol.generateJavaScriptCode()
        str += "\n"
        for command in self.commands:
            str += command.generateJavaScriptCode() + "\n"
        str = str.replace("verdadeiro", "true").replace("falso", "false")
        try:
            with open("MainScript.js", "w") as file:
                file.write(str)
        except Exception as ex:
            print("Error:", ex)

    def generateTarget(self, choice):
        if choice == 1:
            self.generateJavaTarget()
        elif choice == 2:
            self.generatePythonTarget()
        else:
            self.generateJavaScriptTarget()
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
