from ..datastructures import IsiSymbolTable


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
        str = str.replace("++", '+')

        return str

    def generatePythonTarget(self):
        str=""
        for symbol in self.variableTable.getAll():
            str += symbol.generatePythonCode()
        str += "\n"
        for command in self.commands:
            str += command.generatePythonCode() + "\n"
        str = str.replace("verdadeiro", "True").replace("falso", "False")
        str = str.replace("&&", " and ").replace("||"," or ")
        str = str.replace("++", '+')

        return str

    def generateJavaScriptTarget(self):
        str=""
        for symbol in self.variableTable.getAll():
            str += symbol.generateJavaScriptCode()
        str += "\n"
        for command in self.commands:
            str += command.generateJavaScriptCode() + "\n"
        str = str.replace("verdadeiro", "true").replace("falso", "false")
        str = str.replace("++", '+')

        return str

    def generateTarget(self, choice):
        if choice == 1:
            return self.generateJavaTarget()
        elif choice == 2:
            return self.generatePythonTarget()
        else:
            return self.generateJavaScriptTarget()

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
