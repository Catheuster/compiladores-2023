from flask import Flask, request, make_response
from src.main.Main import IsiErrorListener

import traceback

from antlr4 import CommonTokenStream, InputStream
from src.core.IsiLanguageLexer import IsiLanguageLexer
from src.core.IsiLanguageParser import IsiLanguageParser
from src.exceptions.IsiException import IsiSemanticException

app = Flask(__name__)

def compile(source, choice):
    error_listener = IsiErrorListener()

    lexer = IsiLanguageLexer(InputStream(source))

    token_stream = CommonTokenStream(lexer)

    parser = IsiLanguageParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    parser.prog()

    return parser.generateCode(choice)

@app.get("/")
def test():
    return "API funcionando"

@app.post("/java")
def java():
    try:
        source = request.form.get("source", "")
        return {"target": compile(source, 1)}
    except IsiSemanticException as e:
        string = "Erro semântico:" + str(e) + "\n"
        string += traceback.format_exc()
        return make_response({"err": string}, 422)

    except Exception as e:
        string = "Erro de sintaxe:" + str(e) + "\n"
        string += traceback.format_exc()
        return make_response({"err": string}, 400)

@app.post("/python")
def python():
    try:
        source = request.form.get("source", "")
        return {"target": compile(source, 2)}
    except IsiSemanticException as e:
        string = "Erro semântico:" + str(e) + "\n"
        string += traceback.format_exc()
        return make_response({"err": string}, 422)

    except Exception as e:
        string = "Erro de sintaxe:" + str(e) + "\n"
        string += traceback.format_exc()
        return make_response({"err": string}, 400)

@app.post("/javascript")
def javascript():
    try:
        source = request.form.get("source", "")
        return {"target": compile(source, 3)}
    except IsiSemanticException as e:
        string = "Erro semântico:" + str(e) + "\n"
        string += traceback.format_exc()
        return make_response({"err": string}, 422)

    except Exception as e:
        string = "Erro de sintaxe:" + str(e) + "\n"
        string += traceback.format_exc()
        return make_response({"err": string}, 400)
    

