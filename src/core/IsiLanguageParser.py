# Generated from IsiLanguage.g4 by ANTLR 4.13.0
# encoding: utf-8
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
        4,1,27,240,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,4,0,38,8,0,11,0,12,0,39,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,51,8,1,10,1,12,1,54,9,1,
        1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,64,8,2,1,3,1,3,4,3,68,8,3,11,
        3,12,3,69,1,4,1,4,1,4,1,4,1,4,1,4,3,4,78,8,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,94,8,6,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,107,8,7,1,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,4,8,122,8,8,11,8,12,8,123,1,8,1,8,1,8,
        1,8,1,8,1,8,4,8,132,8,8,11,8,12,8,133,1,8,1,8,1,8,3,8,139,8,8,1,
        8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,4,9,152,8,9,11,9,12,9,
        153,1,9,1,9,1,9,1,10,1,10,1,10,1,10,4,10,163,8,10,11,10,12,10,164,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,5,11,181,8,11,10,11,12,11,184,9,11,1,12,1,12,1,12,1,12,5,12,
        190,8,12,10,12,12,12,193,9,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,
        201,8,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        3,14,214,8,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,3,15,228,8,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,236,8,
        16,1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,0,0,249,0,34,1,0,0,0,2,44,1,0,0,0,4,63,1,0,0,0,6,65,1,0,0,
        0,8,77,1,0,0,0,10,79,1,0,0,0,12,87,1,0,0,0,14,99,1,0,0,0,16,111,
        1,0,0,0,18,142,1,0,0,0,20,158,1,0,0,0,22,176,1,0,0,0,24,200,1,0,
        0,0,26,202,1,0,0,0,28,213,1,0,0,0,30,227,1,0,0,0,32,235,1,0,0,0,
        34,37,5,1,0,0,35,38,3,2,1,0,36,38,3,6,3,0,37,35,1,0,0,0,37,36,1,
        0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,
        42,5,2,0,0,42,43,6,0,-1,0,43,1,1,0,0,0,44,45,3,4,2,0,45,46,5,14,
        0,0,46,52,6,1,-1,0,47,48,5,22,0,0,48,49,5,14,0,0,49,51,6,1,-1,0,
        50,47,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,55,1,
        0,0,0,54,52,1,0,0,0,55,56,5,21,0,0,56,3,1,0,0,0,57,58,5,3,0,0,58,
        64,6,2,-1,0,59,60,5,4,0,0,60,64,6,2,-1,0,61,62,5,5,0,0,62,64,6,2,
        -1,0,63,57,1,0,0,0,63,59,1,0,0,0,63,61,1,0,0,0,64,5,1,0,0,0,65,67,
        6,3,-1,0,66,68,3,8,4,0,67,66,1,0,0,0,68,69,1,0,0,0,69,67,1,0,0,0,
        69,70,1,0,0,0,70,7,1,0,0,0,71,78,3,10,5,0,72,78,3,12,6,0,73,78,3,
        14,7,0,74,78,3,16,8,0,75,78,3,18,9,0,76,78,3,20,10,0,77,71,1,0,0,
        0,77,72,1,0,0,0,77,73,1,0,0,0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,
        1,0,0,0,78,9,1,0,0,0,79,80,5,6,0,0,80,81,5,23,0,0,81,82,5,14,0,0,
        82,83,6,5,-1,0,83,84,5,24,0,0,84,85,5,21,0,0,85,86,6,5,-1,0,86,11,
        1,0,0,0,87,88,5,7,0,0,88,93,5,23,0,0,89,90,5,15,0,0,90,94,6,6,-1,
        0,91,92,5,14,0,0,92,94,6,6,-1,0,93,89,1,0,0,0,93,91,1,0,0,0,94,95,
        1,0,0,0,95,96,5,24,0,0,96,97,5,21,0,0,97,98,6,6,-1,0,98,13,1,0,0,
        0,99,100,5,14,0,0,100,101,6,7,-1,0,101,102,5,17,0,0,102,106,6,7,
        -1,0,103,107,3,22,11,0,104,107,3,24,12,0,105,107,3,26,13,0,106,103,
        1,0,0,0,106,104,1,0,0,0,106,105,1,0,0,0,107,108,1,0,0,0,108,109,
        5,21,0,0,109,110,6,7,-1,0,110,15,1,0,0,0,111,112,5,8,0,0,112,113,
        5,23,0,0,113,114,6,8,-1,0,114,115,3,24,12,0,115,116,6,8,-1,0,116,
        117,5,24,0,0,117,118,5,9,0,0,118,119,5,25,0,0,119,121,6,8,-1,0,120,
        122,3,8,4,0,121,120,1,0,0,0,122,123,1,0,0,0,123,121,1,0,0,0,123,
        124,1,0,0,0,124,125,1,0,0,0,125,126,5,26,0,0,126,138,6,8,-1,0,127,
        128,5,10,0,0,128,129,5,25,0,0,129,131,6,8,-1,0,130,132,3,8,4,0,131,
        130,1,0,0,0,132,133,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,
        135,1,0,0,0,135,136,5,26,0,0,136,137,6,8,-1,0,137,139,1,0,0,0,138,
        127,1,0,0,0,138,139,1,0,0,0,139,140,1,0,0,0,140,141,6,8,-1,0,141,
        17,1,0,0,0,142,143,5,11,0,0,143,144,5,23,0,0,144,145,6,9,-1,0,145,
        146,3,24,12,0,146,147,6,9,-1,0,147,148,5,24,0,0,148,149,5,25,0,0,
        149,151,6,9,-1,0,150,152,3,8,4,0,151,150,1,0,0,0,152,153,1,0,0,0,
        153,151,1,0,0,0,153,154,1,0,0,0,154,155,1,0,0,0,155,156,5,26,0,0,
        156,157,6,9,-1,0,157,19,1,0,0,0,158,159,5,12,0,0,159,160,5,25,0,
        0,160,162,6,10,-1,0,161,163,3,8,4,0,162,161,1,0,0,0,163,164,1,0,
        0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,166,1,0,0,0,166,167,5,26,
        0,0,167,168,5,11,0,0,168,169,5,23,0,0,169,170,6,10,-1,0,170,171,
        3,24,12,0,171,172,6,10,-1,0,172,173,5,24,0,0,173,174,6,10,-1,0,174,
        175,5,21,0,0,175,21,1,0,0,0,176,182,3,30,15,0,177,178,5,19,0,0,178,
        179,6,11,-1,0,179,181,3,30,15,0,180,177,1,0,0,0,181,184,1,0,0,0,
        182,180,1,0,0,0,182,183,1,0,0,0,183,23,1,0,0,0,184,182,1,0,0,0,185,
        191,3,28,14,0,186,187,5,20,0,0,187,188,6,12,-1,0,188,190,3,28,14,
        0,189,186,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,
        0,192,201,1,0,0,0,193,191,1,0,0,0,194,195,5,23,0,0,195,196,6,12,
        -1,0,196,197,3,24,12,0,197,198,5,24,0,0,198,199,6,12,-1,0,199,201,
        1,0,0,0,200,185,1,0,0,0,200,194,1,0,0,0,201,25,1,0,0,0,202,203,3,
        32,16,0,203,27,1,0,0,0,204,205,5,14,0,0,205,214,6,14,-1,0,206,207,
        5,13,0,0,207,214,6,14,-1,0,208,209,3,22,11,0,209,210,5,18,0,0,210,
        211,6,14,-1,0,211,212,3,22,11,0,212,214,1,0,0,0,213,204,1,0,0,0,
        213,206,1,0,0,0,213,208,1,0,0,0,214,215,1,0,0,0,215,216,6,14,-1,
        0,216,29,1,0,0,0,217,218,5,14,0,0,218,228,6,15,-1,0,219,220,5,16,
        0,0,220,228,6,15,-1,0,221,222,5,23,0,0,222,223,6,15,-1,0,223,224,
        3,22,11,0,224,225,5,24,0,0,225,226,6,15,-1,0,226,228,1,0,0,0,227,
        217,1,0,0,0,227,219,1,0,0,0,227,221,1,0,0,0,228,229,1,0,0,0,229,
        230,6,15,-1,0,230,31,1,0,0,0,231,232,5,14,0,0,232,236,6,16,-1,0,
        233,234,5,15,0,0,234,236,6,16,-1,0,235,231,1,0,0,0,235,233,1,0,0,
        0,236,237,1,0,0,0,237,238,6,16,-1,0,238,33,1,0,0,0,19,37,39,52,63,
        69,77,93,106,123,133,138,153,164,182,191,200,213,227,235
    ]

class IsiLanguageParser ( Parser ):

    grammarFileName = "IsiLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'programa'", "'fimprog.'", "'numero'", 
                     "'texto'", "'booleano'", "'leia'", "'escreva'", "'se'", 
                     "'entao'", "'senao'", "'enquanto'", "'faca'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "':='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'.'", "','", "'('", "')'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOL", "ID", "TEXT", "NUM", "ASGN", 
                      "ROP", "AOP", "BOP", "DOT", "COMMA", "LP", "RP", "LC", 
                      "RC", "WS" ]

    RULE_prog = 0
    RULE_declaration = 1
    RULE_tipo = 2
    RULE_block = 3
    RULE_cmd = 4
    RULE_cmdRead = 5
    RULE_cmdWrite = 6
    RULE_cmdAssign = 7
    RULE_cmdIf = 8
    RULE_cmdWhile = 9
    RULE_cmdDoWhile = 10
    RULE_algExpr = 11
    RULE_boolExpr = 12
    RULE_strExpr = 13
    RULE_boolTerm = 14
    RULE_algTerm = 15
    RULE_strTerm = 16

    ruleNames =  [ "prog", "declaration", "tipo", "block", "cmd", "cmdRead", 
                   "cmdWrite", "cmdAssign", "cmdIf", "cmdWhile", "cmdDoWhile", 
                   "algExpr", "boolExpr", "strExpr", "boolTerm", "algTerm", 
                   "strTerm" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    BOOL=13
    ID=14
    TEXT=15
    NUM=16
    ASGN=17
    ROP=18
    AOP=19
    BOP=20
    DOT=21
    COMMA=22
    LP=23
    RP=24
    LC=25
    RC=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
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

    def verifyID(self, identifier):
        if not self._symbolTable.exists(identifier):
            raise IsiSemanticException.IsiSemanticException("Símbolo '" + identifier + "' não declarado.\n")

    def verifyType(self, identifier, type):
        self._symbol = self._symbolTable.get(identifier)
        if self._symbol.getType() != type:
            raise IsiSemanticException.IsiSemanticException("Símbolo '" + identifier + "' tem um tipo incompatível!\n")

    def exibeComandos(self):
        for command in self._program.getCommands():
            print(command)

    def generateJavaCode(self):
        self._program.generateTarget()



    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.DeclarationContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.BlockContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.BlockContext,i)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = IsiLanguageParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(IsiLanguageParser.T__0)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 37
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4, 5]:
                    self.state = 35
                    self.declaration()
                    pass
                elif token in [6, 7, 8, 11, 12, 14]:
                    self.state = 36
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23032) != 0)):
                    break

            self.state = 41
            self.match(IsiLanguageParser.T__1)
            self._program.setVariableTable(self._symbolTable)
            self._program.setCommands(self._stack.pop())
            if self._unusedVariables:
                print(f"Warning: Variáveis declaradas, mas não usadas. {self._unusedVariables}\n")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(IsiLanguageParser.TipoContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLanguageParser.ID)
            else:
                return self.getToken(IsiLanguageParser.ID, i)

        def DOT(self):
            return self.getToken(IsiLanguageParser.DOT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLanguageParser.COMMA)
            else:
                return self.getToken(IsiLanguageParser.COMMA, i)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = IsiLanguageParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.tipo()
            self.state = 45
            self.match(IsiLanguageParser.ID)
            self._identifier = self._input.LT(-1).text;
            self._value = None
            self._symbol = IsiVariable.IsiVariable(self._identifier, self._type, self._value)
            if not self._symbolTable.exists(self._identifier):
                self._symbolTable.add(self._symbol)
                self._unusedVariables.append(self._identifier)
                print(f"Símbolo adicionado: {self._symbol}")
            else:
                raise IsiSemanticException.IsiSemanticException("Símbolo '" + self._identifier + "' já declarado.\n")
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 47
                self.match(IsiLanguageParser.COMMA)
                self.state = 48
                self.match(IsiLanguageParser.ID)
                self._identifier = self._input.LT(-1).text;
                self._value = None
                self._symbol = IsiVariable.IsiVariable(self._identifier, self._type, self._value)
                if not self._symbolTable.exists(self._identifier):
                    self._symbolTable.add(self._symbol)
                    self._unusedVariables.append(self._identifier)
                    print(f"Símbolo adicionado: {self._symbol}")
                else:
                    raise IsiSemanticException.IsiSemanticException("Símbolo '" + self._identifier + "' já declarado.\n")
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(IsiLanguageParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = IsiLanguageParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tipo)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(IsiLanguageParser.T__2)
                self._type = IsiVariable.IsiVariable.NUMBER
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(IsiLanguageParser.T__3)
                self._type = IsiVariable.IsiVariable.TEXT
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(IsiLanguageParser.T__4)
                self._type = IsiVariable.IsiVariable.BOOL
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.CmdContext,i)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = IsiLanguageParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self._currentThread = []
            self._stack.append(self._currentThread)
            self.state = 67 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 66
                    self.cmd()

                else:
                    raise NoViableAltException(self)
                self.state = 69 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmdRead(self):
            return self.getTypedRuleContext(IsiLanguageParser.CmdReadContext,0)


        def cmdWrite(self):
            return self.getTypedRuleContext(IsiLanguageParser.CmdWriteContext,0)


        def cmdAssign(self):
            return self.getTypedRuleContext(IsiLanguageParser.CmdAssignContext,0)


        def cmdIf(self):
            return self.getTypedRuleContext(IsiLanguageParser.CmdIfContext,0)


        def cmdWhile(self):
            return self.getTypedRuleContext(IsiLanguageParser.CmdWhileContext,0)


        def cmdDoWhile(self):
            return self.getTypedRuleContext(IsiLanguageParser.CmdDoWhileContext,0)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)




    def cmd(self):

        localctx = IsiLanguageParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cmd)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.cmdRead()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.cmdWrite()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.cmdAssign()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.cmdIf()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.cmdWhile()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 76
                self.cmdDoWhile()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(IsiLanguageParser.LP, 0)

        def ID(self):
            return self.getToken(IsiLanguageParser.ID, 0)

        def RP(self):
            return self.getToken(IsiLanguageParser.RP, 0)

        def DOT(self):
            return self.getToken(IsiLanguageParser.DOT, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_cmdRead

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdRead" ):
                listener.enterCmdRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdRead" ):
                listener.exitCmdRead(self)




    def cmdRead(self):

        localctx = IsiLanguageParser.CmdReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cmdRead)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(IsiLanguageParser.T__5)
            self.state = 80
            self.match(IsiLanguageParser.LP)
            self.state = 81
            self.match(IsiLanguageParser.ID)
            self.verifyID(self._input.LT(-1).text)
            self._readID = self._input.LT(-1).text
            if self._readID in self._unusedVariables:
                self._unusedVariables.remove(self._readID)
            if self._readID not in self._initializedVariables:
                self._initializedVariables.append(self._readID)
            self.state = 83
            self.match(IsiLanguageParser.RP)
            self.state = 84
            self.match(IsiLanguageParser.DOT)
            self._value = self._symbolTable.get(self._readID)
            self._cmd = CommandRead.CommandRead(self._readID, self._value)
            self._stack[-1].append(self._cmd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdWriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(IsiLanguageParser.LP, 0)

        def RP(self):
            return self.getToken(IsiLanguageParser.RP, 0)

        def DOT(self):
            return self.getToken(IsiLanguageParser.DOT, 0)

        def TEXT(self):
            return self.getToken(IsiLanguageParser.TEXT, 0)

        def ID(self):
            return self.getToken(IsiLanguageParser.ID, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_cmdWrite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdWrite" ):
                listener.enterCmdWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdWrite" ):
                listener.exitCmdWrite(self)




    def cmdWrite(self):

        localctx = IsiLanguageParser.CmdWriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cmdWrite)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(IsiLanguageParser.T__6)
            self.state = 88
            self.match(IsiLanguageParser.LP)
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.state = 89
                self.match(IsiLanguageParser.TEXT)
                self._writeInput = self._input.LT(-1).text
                pass
            elif token in [14]:
                self.state = 91
                self.match(IsiLanguageParser.ID)
                self.verifyID(self._input.LT(-1).text)
                self._writeInput = self._input.LT(-1).text
                if self._writeInput not in self._initializedVariables:
                    raise IsiSemanticException.IsiSemanticException("Símbolo '" + self._writeInput + "' não inicializado.\n")
                pass
            else:
                raise NoViableAltException(self)

            self.state = 95
            self.match(IsiLanguageParser.RP)
            self.state = 96
            self.match(IsiLanguageParser.DOT)
            self._cmd = CommandWrite.CommandWrite(self._writeInput)
            self._stack[-1].append(self._cmd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IsiLanguageParser.ID, 0)

        def ASGN(self):
            return self.getToken(IsiLanguageParser.ASGN, 0)

        def DOT(self):
            return self.getToken(IsiLanguageParser.DOT, 0)

        def algExpr(self):
            return self.getTypedRuleContext(IsiLanguageParser.AlgExprContext,0)


        def boolExpr(self):
            return self.getTypedRuleContext(IsiLanguageParser.BoolExprContext,0)


        def strExpr(self):
            return self.getTypedRuleContext(IsiLanguageParser.StrExprContext,0)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_cmdAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdAssign" ):
                listener.enterCmdAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdAssign" ):
                listener.exitCmdAssign(self)




    def cmdAssign(self):

        localctx = IsiLanguageParser.CmdAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cmdAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(IsiLanguageParser.ID)
            self._identifier = self._input.LT(-1).text
            self.verifyID(self._identifier)
            if self._identifier in self._unusedVariables:
                self._unusedVariables.remove(self._identifier)
            if self._identifier not in self._initializedVariables:
                self._initializedVariables.append(self._identifier)
            self.state = 101
            self.match(IsiLanguageParser.ASGN)
            self._exprContent = ""
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 103
                self.algExpr()
                pass

            elif la_ == 2:
                self.state = 104
                self.boolExpr()
                pass

            elif la_ == 3:
                self.state = 105
                self.strExpr()
                pass


            self.state = 108
            self.match(IsiLanguageParser.DOT)
            self.verifyType(self._identifier, self._type)
            self._cmd = CommandAssign.CommandAssign(self._identifier, self._exprContent)
            self._stack[-1].append(self._cmd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(IsiLanguageParser.LP, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(IsiLanguageParser.BoolExprContext,0)


        def RP(self):
            return self.getToken(IsiLanguageParser.RP, 0)

        def LC(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLanguageParser.LC)
            else:
                return self.getToken(IsiLanguageParser.LC, i)

        def RC(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLanguageParser.RC)
            else:
                return self.getToken(IsiLanguageParser.RC, i)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.CmdContext,i)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_cmdIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdIf" ):
                listener.enterCmdIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdIf" ):
                listener.exitCmdIf(self)




    def cmdIf(self):

        localctx = IsiLanguageParser.CmdIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cmdIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(IsiLanguageParser.T__7)
            self.state = 112
            self.match(IsiLanguageParser.LP)
            self._exprContent = ""
            self.state = 114
            self.boolExpr()
            localExprCondition = self._exprContent
            self.state = 116
            self.match(IsiLanguageParser.RP)
            self.state = 117
            self.match(IsiLanguageParser.T__8)
            self.state = 118
            self.match(IsiLanguageParser.LC)
            self._currentThread = []
            self._stack.append(self._currentThread)
            self.state = 121 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 120
                self.cmd()
                self.state = 123 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 22976) != 0)):
                    break

            self.state = 125
            self.match(IsiLanguageParser.RC)
            localTrueList = self._stack.pop()
            localFalseList = []
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 127
                self.match(IsiLanguageParser.T__9)
                self.state = 128
                self.match(IsiLanguageParser.LC)
                self._currentThread = []
                self._stack.append(self._currentThread)
                self.state = 131 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 130
                    self.cmd()
                    self.state = 133 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 22976) != 0)):
                        break

                self.state = 135
                self.match(IsiLanguageParser.RC)
                localFalseList = self._stack.pop()


            self._cmd = CommandIf.CommandIf(localExprCondition, localTrueList, localFalseList)
            self._stack[-1].append(self._cmd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(IsiLanguageParser.LP, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(IsiLanguageParser.BoolExprContext,0)


        def RP(self):
            return self.getToken(IsiLanguageParser.RP, 0)

        def LC(self):
            return self.getToken(IsiLanguageParser.LC, 0)

        def RC(self):
            return self.getToken(IsiLanguageParser.RC, 0)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.CmdContext,i)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_cmdWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdWhile" ):
                listener.enterCmdWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdWhile" ):
                listener.exitCmdWhile(self)




    def cmdWhile(self):

        localctx = IsiLanguageParser.CmdWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cmdWhile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(IsiLanguageParser.T__10)
            self.state = 143
            self.match(IsiLanguageParser.LP)
            self._exprContent=""
            self.state = 145
            self.boolExpr()
            localwhileCondition = self._exprContent
            self.state = 147
            self.match(IsiLanguageParser.RP)
            self.state = 148
            self.match(IsiLanguageParser.LC)
            self._currentThread = []
            self._stack.append(self._currentThread)
            self.state = 151 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 150
                self.cmd()
                self.state = 153 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 22976) != 0)):
                    break

            self.state = 155
            self.match(IsiLanguageParser.RC)
            self._whileList = self._stack.pop()
            self._cmd = CommandWhile.CommandWhile(localwhileCondition, self._whileList)
            self._stack[-1].append(self._cmd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdDoWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(IsiLanguageParser.LC, 0)

        def RC(self):
            return self.getToken(IsiLanguageParser.RC, 0)

        def LP(self):
            return self.getToken(IsiLanguageParser.LP, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(IsiLanguageParser.BoolExprContext,0)


        def RP(self):
            return self.getToken(IsiLanguageParser.RP, 0)

        def DOT(self):
            return self.getToken(IsiLanguageParser.DOT, 0)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.CmdContext,i)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_cmdDoWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdDoWhile" ):
                listener.enterCmdDoWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdDoWhile" ):
                listener.exitCmdDoWhile(self)




    def cmdDoWhile(self):

        localctx = IsiLanguageParser.CmdDoWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cmdDoWhile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(IsiLanguageParser.T__11)
            self.state = 159
            self.match(IsiLanguageParser.LC)
            self._currentThread = []
            self._stack.append(self._currentThread)
            self.state = 162 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 161
                self.cmd()
                self.state = 164 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 22976) != 0)):
                    break

            self.state = 166
            self.match(IsiLanguageParser.RC)
            self.state = 167
            self.match(IsiLanguageParser.T__10)
            self.state = 168
            self.match(IsiLanguageParser.LP)
            self._exprContent=""
            self.state = 170
            self.boolExpr()
            localdoWhileCondition = self._exprContent
            self.state = 172
            self.match(IsiLanguageParser.RP)
            self._doWhileList = self._stack.pop()
            self._cmd = CommandDoWhile.CommandDoWhile(localdoWhileCondition, self._doWhileList)
            self._stack[-1].append(self._cmd)
            self.state = 174
            self.match(IsiLanguageParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlgExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def algTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.AlgTermContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.AlgTermContext,i)


        def AOP(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLanguageParser.AOP)
            else:
                return self.getToken(IsiLanguageParser.AOP, i)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_algExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlgExpr" ):
                listener.enterAlgExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlgExpr" ):
                listener.exitAlgExpr(self)




    def algExpr(self):

        localctx = IsiLanguageParser.AlgExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_algExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.algTerm()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 177
                self.match(IsiLanguageParser.AOP)
                self._exprContent += self._input.LT(-1).text
                self.state = 179
                self.algTerm()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.BoolTermContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.BoolTermContext,i)


        def BOP(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLanguageParser.BOP)
            else:
                return self.getToken(IsiLanguageParser.BOP, i)

        def LP(self):
            return self.getToken(IsiLanguageParser.LP, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(IsiLanguageParser.BoolExprContext,0)


        def RP(self):
            return self.getToken(IsiLanguageParser.RP, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_boolExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)




    def boolExpr(self):

        localctx = IsiLanguageParser.BoolExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_boolExpr)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.boolTerm()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 186
                    self.match(IsiLanguageParser.BOP)
                    self._exprContent += self._input.LT(-1).text
                    print(self._exprContent)
                    self.state = 188
                    self.boolTerm()
                    self.state = 193
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(IsiLanguageParser.LP)
                self._exprContent += '('
                self.state = 196
                self.boolExpr()
                self.state = 197
                self.match(IsiLanguageParser.RP)
                self._exprContent += ')'
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def strTerm(self):
            return self.getTypedRuleContext(IsiLanguageParser.StrTermContext,0)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_strExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrExpr" ):
                listener.enterStrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrExpr" ):
                listener.exitStrExpr(self)




    def strExpr(self):

        localctx = IsiLanguageParser.StrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_strExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.strTerm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IsiLanguageParser.ID, 0)

        def BOOL(self):
            return self.getToken(IsiLanguageParser.BOOL, 0)

        def algExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.AlgExprContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.AlgExprContext,i)


        def ROP(self):
            return self.getToken(IsiLanguageParser.ROP, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_boolTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolTerm" ):
                listener.enterBoolTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolTerm" ):
                listener.exitBoolTerm(self)




    def boolTerm(self):

        localctx = IsiLanguageParser.BoolTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_boolTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 204
                self.match(IsiLanguageParser.ID)
                self.verifyID(self._input.LT(-1).text)
                self._exprContent += self._input.LT(-1).text
                self.verifyType(self._input.LT(-1).text, IsiVariable.IsiVariable.BOOL)

                pass

            elif la_ == 2:
                self.state = 206
                self.match(IsiLanguageParser.BOOL)
                self._exprContent += self._input.LT(-1).text
                self._type = IsiVariable.IsiVariable.BOOL
                pass

            elif la_ == 3:
                self.state = 208
                self.algExpr()
                self.state = 209
                self.match(IsiLanguageParser.ROP)
                self._exprContent += self._input.LT(-1).text
                self.state = 211
                self.algExpr()
                pass


            self._type = IsiVariable.IsiVariable.BOOL
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlgTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IsiLanguageParser.ID, 0)

        def NUM(self):
            return self.getToken(IsiLanguageParser.NUM, 0)

        def LP(self):
            return self.getToken(IsiLanguageParser.LP, 0)

        def algExpr(self):
            return self.getTypedRuleContext(IsiLanguageParser.AlgExprContext,0)


        def RP(self):
            return self.getToken(IsiLanguageParser.RP, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_algTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlgTerm" ):
                listener.enterAlgTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlgTerm" ):
                listener.exitAlgTerm(self)




    def algTerm(self):

        localctx = IsiLanguageParser.AlgTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_algTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 217
                self.match(IsiLanguageParser.ID)
                self.verifyID(self._input.LT(-1).text)
                self._exprContent += self._input.LT(-1).text
                self.verifyType(self._input.LT(-1).text, IsiVariable.IsiVariable.NUMBER)
                pass
            elif token in [16]:
                self.state = 219
                self.match(IsiLanguageParser.NUM)
                self._type = IsiVariable.IsiVariable.NUMBER
                self._exprContent += self._input.LT(-1).text
                pass
            elif token in [23]:
                self.state = 221
                self.match(IsiLanguageParser.LP)
                self._exprContent += '('
                self.state = 223
                self.algExpr()
                self.state = 224
                self.match(IsiLanguageParser.RP)
                self._exprContent += ')'
                pass
            else:
                raise NoViableAltException(self)

            self._type = IsiVariable.IsiVariable.NUMBER
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IsiLanguageParser.ID, 0)

        def TEXT(self):
            return self.getToken(IsiLanguageParser.TEXT, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_strTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrTerm" ):
                listener.enterStrTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrTerm" ):
                listener.exitStrTerm(self)




    def strTerm(self):

        localctx = IsiLanguageParser.StrTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_strTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 231
                self.match(IsiLanguageParser.ID)
                self.verifyID(self._input.LT(-1).text)
                self._exprContent += self._input.LT(-1).text
                self.verifyType(self._input.LT(-1).text, IsiVariable.IsiVariable.TEXT)
                pass
            elif token in [15]:
                self.state = 233
                self.match(IsiLanguageParser.TEXT)
                self._exprContent += self._input.LT(-1).text
                pass
            else:
                raise NoViableAltException(self)

            self._type = IsiVariable.IsiVariable.TEXT
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





