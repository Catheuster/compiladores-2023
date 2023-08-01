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
        4,1,30,218,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
        5,1,43,8,1,10,1,12,1,46,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        56,8,2,1,3,1,3,4,3,60,8,3,11,3,12,3,61,1,4,1,4,1,4,1,4,1,4,1,4,3,
        4,70,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        3,6,86,8,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,99,8,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,115,
        8,8,1,8,1,8,1,8,1,8,1,8,4,8,122,8,8,11,8,12,8,123,1,8,1,8,1,8,1,
        8,1,8,1,8,4,8,132,8,8,11,8,12,8,133,1,8,1,8,1,8,3,8,139,8,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,154,8,9,1,9,
        1,9,1,9,1,9,4,9,160,8,9,11,9,12,9,161,1,9,1,9,1,9,1,10,1,10,1,10,
        1,10,4,10,171,8,10,11,10,12,10,172,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,3,10,187,8,10,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,5,11,197,8,11,10,11,12,11,200,9,11,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,
        216,8,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,0,230,0,
        26,1,0,0,0,2,36,1,0,0,0,4,55,1,0,0,0,6,57,1,0,0,0,8,69,1,0,0,0,10,
        71,1,0,0,0,12,79,1,0,0,0,14,91,1,0,0,0,16,103,1,0,0,0,18,142,1,0,
        0,0,20,166,1,0,0,0,22,192,1,0,0,0,24,215,1,0,0,0,26,29,5,1,0,0,27,
        30,3,2,1,0,28,30,3,6,3,0,29,27,1,0,0,0,29,28,1,0,0,0,30,31,1,0,0,
        0,31,29,1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,0,33,34,5,2,0,0,34,35,
        6,0,-1,0,35,1,1,0,0,0,36,37,3,4,2,0,37,38,5,14,0,0,38,44,6,1,-1,
        0,39,40,5,25,0,0,40,41,5,14,0,0,41,43,6,1,-1,0,42,39,1,0,0,0,43,
        46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,
        0,47,48,5,24,0,0,48,3,1,0,0,0,49,50,5,3,0,0,50,56,6,2,-1,0,51,52,
        5,4,0,0,52,56,6,2,-1,0,53,54,5,5,0,0,54,56,6,2,-1,0,55,49,1,0,0,
        0,55,51,1,0,0,0,55,53,1,0,0,0,56,5,1,0,0,0,57,59,6,3,-1,0,58,60,
        3,8,4,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,
        62,7,1,0,0,0,63,70,3,10,5,0,64,70,3,12,6,0,65,70,3,14,7,0,66,70,
        3,16,8,0,67,70,3,18,9,0,68,70,3,20,10,0,69,63,1,0,0,0,69,64,1,0,
        0,0,69,65,1,0,0,0,69,66,1,0,0,0,69,67,1,0,0,0,69,68,1,0,0,0,70,9,
        1,0,0,0,71,72,5,6,0,0,72,73,5,26,0,0,73,74,5,14,0,0,74,75,6,5,-1,
        0,75,76,5,27,0,0,76,77,5,24,0,0,77,78,6,5,-1,0,78,11,1,0,0,0,79,
        80,5,7,0,0,80,85,5,26,0,0,81,82,5,15,0,0,82,86,6,6,-1,0,83,84,5,
        14,0,0,84,86,6,6,-1,0,85,81,1,0,0,0,85,83,1,0,0,0,86,87,1,0,0,0,
        87,88,5,27,0,0,88,89,5,24,0,0,89,90,6,6,-1,0,90,13,1,0,0,0,91,92,
        5,14,0,0,92,93,6,7,-1,0,93,94,5,17,0,0,94,98,6,7,-1,0,95,96,5,14,
        0,0,96,99,6,7,-1,0,97,99,3,22,11,0,98,95,1,0,0,0,98,97,1,0,0,0,99,
        100,1,0,0,0,100,101,5,24,0,0,101,102,6,7,-1,0,102,15,1,0,0,0,103,
        104,5,8,0,0,104,105,5,26,0,0,105,106,3,22,11,0,106,107,6,8,-1,0,
        107,108,5,18,0,0,108,114,6,8,-1,0,109,110,5,14,0,0,110,115,6,8,-1,
        0,111,112,3,22,11,0,112,113,6,8,-1,0,113,115,1,0,0,0,114,109,1,0,
        0,0,114,111,1,0,0,0,115,116,1,0,0,0,116,117,5,27,0,0,117,118,5,9,
        0,0,118,119,5,28,0,0,119,121,6,8,-1,0,120,122,3,8,4,0,121,120,1,
        0,0,0,122,123,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,125,1,
        0,0,0,125,126,5,29,0,0,126,138,6,8,-1,0,127,128,5,10,0,0,128,129,
        5,28,0,0,129,131,6,8,-1,0,130,132,3,8,4,0,131,130,1,0,0,0,132,133,
        1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,136,
        5,29,0,0,136,137,6,8,-1,0,137,139,1,0,0,0,138,127,1,0,0,0,138,139,
        1,0,0,0,139,140,1,0,0,0,140,141,6,8,-1,0,141,17,1,0,0,0,142,143,
        5,11,0,0,143,153,5,26,0,0,144,145,5,13,0,0,145,154,6,9,-1,0,146,
        147,3,24,12,0,147,148,6,9,-1,0,148,149,5,18,0,0,149,150,6,9,-1,0,
        150,151,3,24,12,0,151,152,6,9,-1,0,152,154,1,0,0,0,153,144,1,0,0,
        0,153,146,1,0,0,0,154,155,1,0,0,0,155,156,5,27,0,0,156,157,5,28,
        0,0,157,159,6,9,-1,0,158,160,3,8,4,0,159,158,1,0,0,0,160,161,1,0,
        0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,163,1,0,0,0,163,164,5,29,
        0,0,164,165,6,9,-1,0,165,19,1,0,0,0,166,167,5,12,0,0,167,168,5,28,
        0,0,168,170,6,10,-1,0,169,171,3,8,4,0,170,169,1,0,0,0,171,172,1,
        0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,174,1,0,0,0,174,175,5,
        29,0,0,175,176,5,11,0,0,176,186,5,26,0,0,177,178,5,13,0,0,178,187,
        6,10,-1,0,179,180,3,24,12,0,180,181,6,10,-1,0,181,182,5,18,0,0,182,
        183,6,10,-1,0,183,184,3,24,12,0,184,185,6,10,-1,0,185,187,1,0,0,
        0,186,177,1,0,0,0,186,179,1,0,0,0,187,188,1,0,0,0,188,189,5,27,0,
        0,189,190,6,10,-1,0,190,191,5,24,0,0,191,21,1,0,0,0,192,198,3,24,
        12,0,193,194,5,19,0,0,194,195,6,11,-1,0,195,197,3,24,12,0,196,193,
        1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,23,1,
        0,0,0,200,198,1,0,0,0,201,202,5,14,0,0,202,216,6,12,-1,0,203,204,
        5,16,0,0,204,216,6,12,-1,0,205,206,5,15,0,0,206,216,6,12,-1,0,207,
        208,5,13,0,0,208,216,6,12,-1,0,209,210,5,26,0,0,210,211,6,12,-1,
        0,211,212,3,22,11,0,212,213,5,27,0,0,213,214,6,12,-1,0,214,216,1,
        0,0,0,215,201,1,0,0,0,215,203,1,0,0,0,215,205,1,0,0,0,215,207,1,
        0,0,0,215,209,1,0,0,0,216,25,1,0,0,0,18,29,31,44,55,61,69,85,98,
        114,123,133,138,153,161,172,186,198,215
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
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'.'", "','", 
                     "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOL", "ID", "TEXT", "NUM", "ASGN", 
                      "ROP", "AOP", "ADD", "SUB", "MULT", "DIV", "DOT", 
                      "COMMA", "LP", "RP", "LC", "RC", "WS" ]

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
    RULE_expr = 11
    RULE_term = 12

    ruleNames =  [ "prog", "declaration", "tipo", "block", "cmd", "cmdRead", 
                   "cmdWrite", "cmdAssign", "cmdIf", "cmdWhile", "cmdDoWhile", 
                   "expr", "term" ]

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
    ADD=20
    SUB=21
    MULT=22
    DIV=23
    DOT=24
    COMMA=25
    LP=26
    RP=27
    LC=28
    RC=29
    WS=30

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
            self.state = 26
            self.match(IsiLanguageParser.T__0)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 29
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4, 5]:
                    self.state = 27
                    self.declaration()
                    pass
                elif token in [6, 7, 8, 11, 12, 14]:
                    self.state = 28
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23032) != 0)):
                    break

            self.state = 33
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
            self.state = 36
            self.tipo()
            self.state = 37
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
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 39
                self.match(IsiLanguageParser.COMMA)
                self.state = 40
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
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
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
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(IsiLanguageParser.T__2)
                self._type = IsiVariable.IsiVariable.NUMBER
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(IsiLanguageParser.T__3)
                self._type = IsiVariable.IsiVariable.TEXT
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
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
            self.state = 59 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 58
                    self.cmd()

                else:
                    raise NoViableAltException(self)
                self.state = 61 
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
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.cmdRead()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.cmdWrite()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.cmdAssign()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.cmdIf()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.cmdWhile()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 68
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
            self.state = 71
            self.match(IsiLanguageParser.T__5)
            self.state = 72
            self.match(IsiLanguageParser.LP)
            self.state = 73
            self.match(IsiLanguageParser.ID)
            self.verifyID(self._input.LT(-1).text)
            self._readID = self._input.LT(-1).text
            if self._readID in self._unusedVariables:
                self._unusedVariables.remove(self._readID)
            self._initializedVariables.append(self._identifier)
            self.state = 75
            self.match(IsiLanguageParser.RP)
            self.state = 76
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
            self.state = 79
            self.match(IsiLanguageParser.T__6)
            self.state = 80
            self.match(IsiLanguageParser.LP)
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.state = 81
                self.match(IsiLanguageParser.TEXT)
                self._writeInput = self._input.LT(-1).text
                pass
            elif token in [14]:
                self.state = 83
                self.match(IsiLanguageParser.ID)
                self.verifyID(self._input.LT(-1).text)
                self._writeInput = self._input.LT(-1).text
                if self._writeInput not in self._initializedVariables:
                    raise IsiSemanticException.IsiSemanticException("Símbolo '" + self._writeInput + "' não inicializado.\n")
                pass
            else:
                raise NoViableAltException(self)

            self.state = 87
            self.match(IsiLanguageParser.RP)
            self.state = 88
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLanguageParser.ID)
            else:
                return self.getToken(IsiLanguageParser.ID, i)

        def ASGN(self):
            return self.getToken(IsiLanguageParser.ASGN, 0)

        def DOT(self):
            return self.getToken(IsiLanguageParser.DOT, 0)

        def expr(self):
            return self.getTypedRuleContext(IsiLanguageParser.ExprContext,0)


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
            self.state = 91
            self.match(IsiLanguageParser.ID)
            self._identifier = self._input.LT(-1).text
            self.verifyID(self._identifier)
            if self._identifier in self._unusedVariables:
                self._unusedVariables.remove(self._identifier)
            self._initializedVariables.append(self._identifier)
            self.state = 93
            self.match(IsiLanguageParser.ASGN)
            self._exprContent = ""
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 95
                self.match(IsiLanguageParser.ID)
                self._rID = self._input.LT(-1).text
                if self._rID not in self._initializedVariables:
                    raise IsiSemanticException.IsiSemanticException("Símbolo '" + self._rID + "' não inicializado.\n")
                pass

            elif la_ == 2:
                self.state = 97
                self.expr()
                pass


            self.state = 100
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.ExprContext,i)


        def ROP(self):
            return self.getToken(IsiLanguageParser.ROP, 0)

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

        def ID(self):
            return self.getToken(IsiLanguageParser.ID, 0)

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
            self.state = 103
            self.match(IsiLanguageParser.T__7)
            self.state = 104
            self.match(IsiLanguageParser.LP)
            self.state = 105
            self.expr()
            self._exprCondition = self._input.LT(-1).text
            self.state = 107
            self.match(IsiLanguageParser.ROP)
            self._exprCondition += self._input.LT(-1).text
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 109
                self.match(IsiLanguageParser.ID)
                self._ID = self._input.LT(-1).text
                if self._ID not in self._initializedVariables:
                    raise IsiSemanticException.IsiSemanticException("Símbolo '" + self._ID + "' não inicializado.\n")
                self._exprCondition += self._input.LT(-1).text
                pass

            elif la_ == 2:
                self.state = 111
                self.expr()
                self._exprCondition += self._input.LT(-1).text
                pass


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
            self._trueList = self._stack.pop()
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
                self._falseList = self._stack.pop()


            self._cmd = CommandIf.CommandIf(self._exprCondition, self._trueList, self._falseList)
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

        def RP(self):
            return self.getToken(IsiLanguageParser.RP, 0)

        def LC(self):
            return self.getToken(IsiLanguageParser.LC, 0)

        def RC(self):
            return self.getToken(IsiLanguageParser.RC, 0)

        def BOOL(self):
            return self.getToken(IsiLanguageParser.BOOL, 0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.TermContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.TermContext,i)


        def ROP(self):
            return self.getToken(IsiLanguageParser.ROP, 0)

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
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 144
                self.match(IsiLanguageParser.BOOL)
                self._whileCondition = self._input.LT(-1).text
                pass

            elif la_ == 2:
                self.state = 146
                self.term()
                self._whileCondition = self._input.LT(-1).text
                self.state = 148
                self.match(IsiLanguageParser.ROP)
                self._whileCondition += self._input.LT(-1).text
                self.state = 150
                self.term()
                self._whileCondition += self._input.LT(-1).text
                pass


            self.state = 155
            self.match(IsiLanguageParser.RP)
            self.state = 156
            self.match(IsiLanguageParser.LC)
            self._currentThread = []
            self._stack.append(self._currentThread)
            self.state = 159 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 158
                self.cmd()
                self.state = 161 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 22976) != 0)):
                    break

            self.state = 163
            self.match(IsiLanguageParser.RC)
            self._whileList = self._stack.pop()
            self._cmd = CommandWhile.CommandWhile(self._whileCondition, self._whileList)
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

        def RP(self):
            return self.getToken(IsiLanguageParser.RP, 0)

        def DOT(self):
            return self.getToken(IsiLanguageParser.DOT, 0)

        def BOOL(self):
            return self.getToken(IsiLanguageParser.BOOL, 0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.TermContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.TermContext,i)


        def ROP(self):
            return self.getToken(IsiLanguageParser.ROP, 0)

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
            self.state = 166
            self.match(IsiLanguageParser.T__11)
            self.state = 167
            self.match(IsiLanguageParser.LC)
            self._currentThread = []
            self._stack.append(self._currentThread)
            self.state = 170 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 169
                self.cmd()
                self.state = 172 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 22976) != 0)):
                    break

            self.state = 174
            self.match(IsiLanguageParser.RC)
            self.state = 175
            self.match(IsiLanguageParser.T__10)
            self.state = 176
            self.match(IsiLanguageParser.LP)
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 177
                self.match(IsiLanguageParser.BOOL)
                self._doWhileCondition = self._input.LT(-1).text
                pass

            elif la_ == 2:
                self.state = 179
                self.term()
                self._doWhileCondition = self._input.LT(-1).text
                self.state = 181
                self.match(IsiLanguageParser.ROP)
                self._doWhileCondition += self._input.LT(-1).text
                self.state = 183
                self.term()
                self._doWhileCondition += self._input.LT(-1).text
                pass


            self.state = 188
            self.match(IsiLanguageParser.RP)
            self._doWhileList = self._stack.pop()
            self._cmd = CommandDoWhile.CommandDoWhile(self._doWhileCondition, self._doWhileList)
            self._stack[-1].append(self._cmd)
            self.state = 190
            self.match(IsiLanguageParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.TermContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.TermContext,i)


        def AOP(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLanguageParser.AOP)
            else:
                return self.getToken(IsiLanguageParser.AOP, i)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = IsiLanguageParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.term()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 193
                self.match(IsiLanguageParser.AOP)
                self._exprContent += self._input.LT(-1).text
                self.state = 195
                self.term()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IsiLanguageParser.ID, 0)

        def NUM(self):
            return self.getToken(IsiLanguageParser.NUM, 0)

        def TEXT(self):
            return self.getToken(IsiLanguageParser.TEXT, 0)

        def BOOL(self):
            return self.getToken(IsiLanguageParser.BOOL, 0)

        def LP(self):
            return self.getToken(IsiLanguageParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(IsiLanguageParser.ExprContext,0)


        def RP(self):
            return self.getToken(IsiLanguageParser.RP, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = IsiLanguageParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_term)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(IsiLanguageParser.ID)
                self.verifyID(self._input.LT(-1).text)
                self._type = self._symbolTable.get(self._input.LT(-1).text).getType()
                self._exprContent += self._input.LT(-1).text
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(IsiLanguageParser.NUM)
                self._type = IsiVariable.IsiVariable.NUMBER
                self._exprContent += self._input.LT(-1).text
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.match(IsiLanguageParser.TEXT)
                self._type = IsiVariable.IsiVariable.TEXT
                self._exprContent += self._input.LT(-1).text
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 207
                self.match(IsiLanguageParser.BOOL)
                self._type = IsiVariable.IsiVariable.BOOL
                self._exprContent += self._input.LT(-1).text
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 5)
                self.state = 209
                self.match(IsiLanguageParser.LP)
                self._exprContent += '('
                self.state = 211
                self.expr()
                self.state = 212
                self.match(IsiLanguageParser.RP)
                self._exprContent += ')'
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





