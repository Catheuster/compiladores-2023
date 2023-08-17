import traceback

from antlr4 import CommonTokenStream, FileStream
from src.core.IsiLanguageLexer import IsiLanguageLexer
from src.core.IsiLanguageParser import IsiLanguageParser
from src.exceptions.IsiException import IsiSemanticException,IsiSyntaxException
from antlr4.error.ErrorListener import ErrorListener


class IsiErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise IsiSyntaxException("Erro sintático: linha %d coluna %d: %s\n" % \
                        (line, column, msg))

if __name__ == '__main__':
    try:
        error_listener = IsiErrorListener()

        lexer = IsiLanguageLexer(FileStream("input.isi"))

        token_stream = CommonTokenStream(lexer)

        parser = IsiLanguageParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        parser.prog()

        print("Compilation successful!")

        parser.exibeComandos()

        try:
            with open("MainClass.java", "w") as file:
                file.write(parser.generateCode(1))
        except Exception as ex:
            print("Error:", ex)
        
        try:
            with open("MainScript.py", "w") as file:
                file.write(parser.generateCode(2))
        except Exception as ex:
            print("Error:", ex)
        
        try:
            with open("MainScript.js", "w") as file:
                file.write(parser.generateCode(3))
        except Exception as ex:
            print("Error:", ex)
        

    except IsiSemanticException as e:
        print("Erro semântico:", e)
        traceback.print_exc()

    except Exception as e:
        print("Erro de sintaxe:", e)
        traceback.print_exc()
