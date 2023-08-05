import traceback

from antlr4 import CommonTokenStream, FileStream
from src.core.IsiLanguageLexer import IsiLanguageLexer
from src.core.IsiLanguageParser import IsiLanguageParser
from src.exceptions.IsiSemanticException import IsiSemanticException

if __name__ == '__main__':
    try:
        lexer = IsiLanguageLexer(FileStream("../../input.isi"))

        token_stream = CommonTokenStream(lexer)

        parser = IsiLanguageParser(token_stream)

        parser.prog()

        print("Compilation successful!")

        parser.exibeComandos()

        parser.generateCode(1)
        parser.generateCode(2)
        parser.generateCode(3)

    except IsiSemanticException as e:
        print("Erro semântico:", e)
        traceback.print_exc()

    except Exception as e:
        print("Erro genérico:", e)
        traceback.print_exc()
