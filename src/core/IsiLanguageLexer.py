# Generated from IsiLanguage.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from ..ast import AbstractCommand
from ..ast import CommandRead
from ..ast import CommandWrite
from ..ast import CommandAssign
from ..ast import CommandIf
from ..ast import CommandWhile
from ..ast import CommandDoWhile
from ..ast import IsiProgram
from ..datastructures import IsiSymbol
from ..datastructures import IsiSymbolTable
from ..datastructures import IsiVariable
from ..exceptions import IsiSemanticException


def serializedATN():
    return [
        4,0,29,229,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,
        1,12,3,12,146,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,3,13,163,8,13,1,14,1,14,5,14,167,8,
        14,10,14,12,14,170,9,14,1,15,1,15,4,15,174,8,15,11,15,12,15,175,
        1,15,1,15,1,16,4,16,181,8,16,11,16,12,16,182,1,16,1,16,3,16,187,
        8,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        3,18,201,8,18,1,19,1,19,1,20,1,20,1,20,1,20,3,20,209,8,20,1,21,1,
        21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,
        27,1,28,1,28,1,28,1,28,0,0,29,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,
        17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,
        39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,1,0,
        7,1,0,97,122,3,0,48,57,65,90,97,122,4,0,32,32,48,57,65,90,97,122,
        1,0,48,57,2,0,60,60,62,62,3,0,42,43,45,45,47,47,3,0,9,10,13,13,32,
        32,241,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
        0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,
        0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,
        0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,
        0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,1,59,1,0,0,
        0,3,68,1,0,0,0,5,77,1,0,0,0,7,84,1,0,0,0,9,90,1,0,0,0,11,99,1,0,
        0,0,13,104,1,0,0,0,15,112,1,0,0,0,17,115,1,0,0,0,19,121,1,0,0,0,
        21,127,1,0,0,0,23,136,1,0,0,0,25,145,1,0,0,0,27,162,1,0,0,0,29,164,
        1,0,0,0,31,171,1,0,0,0,33,180,1,0,0,0,35,188,1,0,0,0,37,200,1,0,
        0,0,39,202,1,0,0,0,41,208,1,0,0,0,43,210,1,0,0,0,45,213,1,0,0,0,
        47,215,1,0,0,0,49,217,1,0,0,0,51,219,1,0,0,0,53,221,1,0,0,0,55,223,
        1,0,0,0,57,225,1,0,0,0,59,60,5,112,0,0,60,61,5,114,0,0,61,62,5,111,
        0,0,62,63,5,103,0,0,63,64,5,114,0,0,64,65,5,97,0,0,65,66,5,109,0,
        0,66,67,5,97,0,0,67,2,1,0,0,0,68,69,5,102,0,0,69,70,5,105,0,0,70,
        71,5,109,0,0,71,72,5,112,0,0,72,73,5,114,0,0,73,74,5,111,0,0,74,
        75,5,103,0,0,75,76,5,46,0,0,76,4,1,0,0,0,77,78,5,110,0,0,78,79,5,
        117,0,0,79,80,5,109,0,0,80,81,5,101,0,0,81,82,5,114,0,0,82,83,5,
        111,0,0,83,6,1,0,0,0,84,85,5,116,0,0,85,86,5,101,0,0,86,87,5,120,
        0,0,87,88,5,116,0,0,88,89,5,111,0,0,89,8,1,0,0,0,90,91,5,98,0,0,
        91,92,5,111,0,0,92,93,5,111,0,0,93,94,5,108,0,0,94,95,5,101,0,0,
        95,96,5,97,0,0,96,97,5,110,0,0,97,98,5,111,0,0,98,10,1,0,0,0,99,
        100,5,108,0,0,100,101,5,101,0,0,101,102,5,105,0,0,102,103,5,97,0,
        0,103,12,1,0,0,0,104,105,5,101,0,0,105,106,5,115,0,0,106,107,5,99,
        0,0,107,108,5,114,0,0,108,109,5,101,0,0,109,110,5,118,0,0,110,111,
        5,97,0,0,111,14,1,0,0,0,112,113,5,115,0,0,113,114,5,101,0,0,114,
        16,1,0,0,0,115,116,5,101,0,0,116,117,5,110,0,0,117,118,5,116,0,0,
        118,119,5,97,0,0,119,120,5,111,0,0,120,18,1,0,0,0,121,122,5,115,
        0,0,122,123,5,101,0,0,123,124,5,110,0,0,124,125,5,97,0,0,125,126,
        5,111,0,0,126,20,1,0,0,0,127,128,5,101,0,0,128,129,5,110,0,0,129,
        130,5,113,0,0,130,131,5,117,0,0,131,132,5,97,0,0,132,133,5,110,0,
        0,133,134,5,116,0,0,134,135,5,111,0,0,135,22,1,0,0,0,136,137,5,102,
        0,0,137,138,5,97,0,0,138,139,5,99,0,0,139,140,5,97,0,0,140,24,1,
        0,0,0,141,146,3,39,19,0,142,146,3,41,20,0,143,146,3,37,18,0,144,
        146,3,43,21,0,145,141,1,0,0,0,145,142,1,0,0,0,145,143,1,0,0,0,145,
        144,1,0,0,0,146,26,1,0,0,0,147,148,5,118,0,0,148,149,5,101,0,0,149,
        150,5,114,0,0,150,151,5,100,0,0,151,152,5,97,0,0,152,153,5,100,0,
        0,153,154,5,101,0,0,154,155,5,105,0,0,155,156,5,114,0,0,156,163,
        5,111,0,0,157,158,5,102,0,0,158,159,5,97,0,0,159,160,5,108,0,0,160,
        161,5,115,0,0,161,163,5,111,0,0,162,147,1,0,0,0,162,157,1,0,0,0,
        163,28,1,0,0,0,164,168,7,0,0,0,165,167,7,1,0,0,166,165,1,0,0,0,167,
        170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,30,1,0,0,0,170,168,
        1,0,0,0,171,173,5,34,0,0,172,174,7,2,0,0,173,172,1,0,0,0,174,175,
        1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,178,
        5,34,0,0,178,32,1,0,0,0,179,181,7,3,0,0,180,179,1,0,0,0,181,182,
        1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,186,1,0,0,0,184,185,
        5,46,0,0,185,187,7,3,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,34,
        1,0,0,0,188,189,5,58,0,0,189,190,5,61,0,0,190,36,1,0,0,0,191,201,
        7,4,0,0,192,193,5,60,0,0,193,201,5,61,0,0,194,195,5,62,0,0,195,201,
        5,61,0,0,196,197,5,33,0,0,197,201,5,61,0,0,198,199,5,61,0,0,199,
        201,5,61,0,0,200,191,1,0,0,0,200,192,1,0,0,0,200,194,1,0,0,0,200,
        196,1,0,0,0,200,198,1,0,0,0,201,38,1,0,0,0,202,203,7,5,0,0,203,40,
        1,0,0,0,204,205,5,38,0,0,205,209,5,38,0,0,206,207,5,124,0,0,207,
        209,5,124,0,0,208,204,1,0,0,0,208,206,1,0,0,0,209,42,1,0,0,0,210,
        211,5,43,0,0,211,212,5,43,0,0,212,44,1,0,0,0,213,214,5,46,0,0,214,
        46,1,0,0,0,215,216,5,44,0,0,216,48,1,0,0,0,217,218,5,40,0,0,218,
        50,1,0,0,0,219,220,5,41,0,0,220,52,1,0,0,0,221,222,5,123,0,0,222,
        54,1,0,0,0,223,224,5,125,0,0,224,56,1,0,0,0,225,226,7,6,0,0,226,
        227,1,0,0,0,227,228,6,28,0,0,228,58,1,0,0,0,11,0,145,162,166,168,
        173,175,182,186,200,208,1,6,0,0
    ]

class IsiLanguageLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    OP = 13
    BOOL = 14
    ID = 15
    TEXT = 16
    NUM = 17
    ASGN = 18
    ROP = 19
    AOP = 20
    BOP = 21
    SOP = 22
    DOT = 23
    COMMA = 24
    LP = 25
    RP = 26
    LC = 27
    RC = 28
    WS = 29

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'programa'", "'fimprog.'", "'numero'", "'texto'", "'booleano'", 
            "'leia'", "'escreva'", "'se'", "'entao'", "'senao'", "'enquanto'", 
            "'faca'", "':='", "'++'", "'.'", "','", "'('", "')'", "'{'", 
            "'}'" ]

    symbolicNames = [ "<INVALID>",
            "OP", "BOOL", "ID", "TEXT", "NUM", "ASGN", "ROP", "AOP", "BOP", 
            "SOP", "DOT", "COMMA", "LP", "RP", "LC", "RC", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "OP", "BOOL", 
                  "ID", "TEXT", "NUM", "ASGN", "ROP", "AOP", "BOP", "SOP", 
                  "DOT", "COMMA", "LP", "RP", "LC", "RC", "WS" ]

    grammarFileName = "IsiLanguage.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


        self._type = None
        self._identifier = None
        self._value = None
        self._symbolTable = IsiSymbolTable.IsiSymbolTable()
        self._symbol = IsiSymbol.IsiSymbol
        self._program = IsiProgram.IsiProgram()
        self._readID = None
        self._writeID = None
        self._exprID = None
        self._exprContent = None
        self._stack = []
        self._unusedVariables = []
        self._initializedVariables = []
        self._exprCondition = None
        self._trueList = []
        self._falseList = []
        self._expr_stack = []
        self._typetable = ['numero','texto','booleano']

    def verifyID(self, identifier):
        if not self._symbolTable.exists(identifier):
            raise IsiSemanticException.IsiSemanticException("Símbolo '" + identifier + "' não declarado.\n")

    def verifyType(self, identifier, type):
        self._symbol = self._symbolTable.get(identifier)
        if self._symbol.getType() != type:
            raise IsiSemanticException.IsiSemanticException("Símbolo '" + identifier + "' e incompativel com o tipo " + self._typetable[type] + "\n")

    def exibeComandos(self):
        for command in self._program.getCommands():
            print(command)

    def generateCode(self, choice=1):
        self._program.generateTarget(choice)

    def stack_op(self,op):
        if op in ['<', '>', '<=', '>=', '!=', '==']:
            self._expr_stack.append("ROP")
        elif op in ['+', '-', '*', '/']:
            self._expr_stack.append("AOP")
        elif op in ['&&', '||']:
            self._expr_stack.append("BOP")
        elif op in ['++']:
            self._expr_stack.append("SOP")

    def verify_stack(self):
        print('inicio')
        print(self._expr_stack)
        right_param = self._expr_stack.pop()
        op = self._expr_stack.pop()
        left_param = self._expr_stack.pop()

        match op:
            case 'AOP':
                if (right_param != IsiVariable.IsiVariable.NUMBER) or (left_param != IsiVariable.IsiVariable.NUMBER):
                    raise IsiSemanticException.IsiSemanticException('Opercao invalida')
                self._expr_stack.append(IsiVariable.IsiVariable.NUMBER)
            case 'ROP':
                if (right_param != 0) or (left_param != 0):
                    raise IsiSemanticException.IsiSemanticException('Opercao invalida')
                self._expr_stack.append(IsiVariable.IsiVariable.BOOL)
            case 'BOP':
                if (right_param != IsiVariable.IsiVariable.BOOL) or (left_param != IsiVariable.IsiVariable.BOOL):
                    raise IsiSemanticException.IsiSemanticException('Opercao invalida')
                self._expr_stack.append(IsiVariable.IsiVariable.BOOL)
            case 'SOP':
                if (right_param != IsiVariable.IsiVariable.TEXT) or (left_param != IsiVariable.IsiVariable.TEXT):
                    raise IsiSemanticException.IsiSemanticException('Opercao invalida')
                self._expr_stack.append(IsiVariable.IsiVariable.TEXT)
        print('fim')
        print(self._expr_stack)


