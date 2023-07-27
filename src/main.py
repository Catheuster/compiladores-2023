from antlr4 import *
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser

if __name__ == '__main__':
    input_stream = FileStream("../testInputs/inputTestInicial.ggim")
    lexer = gramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = gramaticaParser(token_stream)
    tree = parser.programa()
    print("IT WORKS, YOU DID IT WOOOOOOOOOOOOOOOOOO")
