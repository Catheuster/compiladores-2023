# Generated from gramatica.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,86,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,4,0,24,8,0,11,0,12,0,25,1,
        0,1,0,1,1,1,1,1,1,1,1,5,1,34,8,1,10,1,12,1,37,9,1,1,1,1,1,1,2,1,
        2,1,3,1,3,1,3,3,3,46,8,3,1,4,1,4,1,4,4,4,51,8,4,11,4,12,4,52,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,3,5,62,8,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        7,1,7,1,7,1,8,1,8,5,8,76,8,8,10,8,12,8,79,9,8,1,8,1,8,1,9,1,9,1,
        9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,3,1,0,3,5,2,0,9,9,14,14,
        2,0,9,9,14,15,83,0,20,1,0,0,0,2,29,1,0,0,0,4,40,1,0,0,0,6,45,1,0,
        0,0,8,47,1,0,0,0,10,57,1,0,0,0,12,67,1,0,0,0,14,70,1,0,0,0,16,73,
        1,0,0,0,18,82,1,0,0,0,20,23,5,1,0,0,21,24,3,2,1,0,22,24,3,6,3,0,
        23,21,1,0,0,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,
        0,0,0,26,27,1,0,0,0,27,28,5,2,0,0,28,1,1,0,0,0,29,30,3,4,2,0,30,
        35,5,9,0,0,31,32,5,10,0,0,32,34,5,9,0,0,33,31,1,0,0,0,34,37,1,0,
        0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,
        5,11,0,0,39,3,1,0,0,0,40,41,7,0,0,0,41,5,1,0,0,0,42,46,3,12,6,0,
        43,46,3,8,4,0,44,46,3,10,5,0,45,42,1,0,0,0,45,43,1,0,0,0,45,44,1,
        0,0,0,46,7,1,0,0,0,47,48,5,6,0,0,48,50,5,12,0,0,49,51,7,1,0,0,50,
        49,1,0,0,0,51,52,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,
        0,54,55,5,13,0,0,55,56,5,11,0,0,56,9,1,0,0,0,57,58,5,7,0,0,58,61,
        5,12,0,0,59,60,5,14,0,0,60,62,5,10,0,0,61,59,1,0,0,0,61,62,1,0,0,
        0,62,63,1,0,0,0,63,64,5,9,0,0,64,65,5,13,0,0,65,66,5,11,0,0,66,11,
        1,0,0,0,67,68,5,9,0,0,68,69,3,14,7,0,69,13,1,0,0,0,70,71,5,8,0,0,
        71,72,3,16,8,0,72,15,1,0,0,0,73,77,7,2,0,0,74,76,3,18,9,0,75,74,
        1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,
        79,77,1,0,0,0,80,81,5,11,0,0,81,17,1,0,0,0,82,83,5,16,0,0,83,84,
        7,2,0,0,84,19,1,0,0,0,7,23,25,35,45,52,61,77
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'start'", "'stop;'", "'Int'", "'Real'", 
                     "'Logic'", "'echo'", "'take'", "'='", "<INVALID>", 
                     "','", "';'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'++'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "VG", "PV", "AP", "FP", "TEXT", 
                      "NUM", "OP", "SUM", "SUB", "MUL", "DIV", "CONCAT", 
                      "BLANK" ]

    RULE_programa = 0
    RULE_dclr = 1
    RULE_tipo = 2
    RULE_cmd = 3
    RULE_showcmd = 4
    RULE_readcmd = 5
    RULE_atrbcmd = 6
    RULE_atrbcmdL = 7
    RULE_expr = 8
    RULE_exprL = 9

    ruleNames =  [ "programa", "dclr", "tipo", "cmd", "showcmd", "readcmd", 
                   "atrbcmd", "atrbcmdL", "expr", "exprL" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    ID=9
    VG=10
    PV=11
    AP=12
    FP=13
    TEXT=14
    NUM=15
    OP=16
    SUM=17
    SUB=18
    MUL=19
    DIV=20
    CONCAT=21
    BLANK=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dclr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.DclrContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.DclrContext,i)


        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CmdContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CmdContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = gramaticaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(gramaticaParser.T__0)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 23
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4, 5]:
                    self.state = 21
                    self.dclr()
                    pass
                elif token in [6, 7, 9]:
                    self.state = 22
                    self.cmd()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 760) != 0)):
                    break

            self.state = 27
            self.match(gramaticaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DclrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(gramaticaParser.TipoContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

        def PV(self):
            return self.getToken(gramaticaParser.PV, 0)

        def VG(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.VG)
            else:
                return self.getToken(gramaticaParser.VG, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_dclr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDclr" ):
                listener.enterDclr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDclr" ):
                listener.exitDclr(self)




    def dclr(self):

        localctx = gramaticaParser.DclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dclr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.tipo()
            self.state = 30
            self.match(gramaticaParser.ID)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 31
                self.match(gramaticaParser.VG)
                self.state = 32
                self.match(gramaticaParser.ID)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(gramaticaParser.PV)
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
            return gramaticaParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = gramaticaParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def atrbcmd(self):
            return self.getTypedRuleContext(gramaticaParser.AtrbcmdContext,0)


        def showcmd(self):
            return self.getTypedRuleContext(gramaticaParser.ShowcmdContext,0)


        def readcmd(self):
            return self.getTypedRuleContext(gramaticaParser.ReadcmdContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)




    def cmd(self):

        localctx = gramaticaParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cmd)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.atrbcmd()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.showcmd()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.readcmd()
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


    class ShowcmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(gramaticaParser.AP, 0)

        def FP(self):
            return self.getToken(gramaticaParser.FP, 0)

        def PV(self):
            return self.getToken(gramaticaParser.PV, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.TEXT)
            else:
                return self.getToken(gramaticaParser.TEXT, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_showcmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShowcmd" ):
                listener.enterShowcmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShowcmd" ):
                listener.exitShowcmd(self)




    def showcmd(self):

        localctx = gramaticaParser.ShowcmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_showcmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(gramaticaParser.T__5)
            self.state = 48
            self.match(gramaticaParser.AP)
            self.state = 50 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                _la = self._input.LA(1)
                if not(_la==9 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 52 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9 or _la==14):
                    break

            self.state = 54
            self.match(gramaticaParser.FP)
            self.state = 55
            self.match(gramaticaParser.PV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadcmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(gramaticaParser.AP, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def FP(self):
            return self.getToken(gramaticaParser.FP, 0)

        def PV(self):
            return self.getToken(gramaticaParser.PV, 0)

        def TEXT(self):
            return self.getToken(gramaticaParser.TEXT, 0)

        def VG(self):
            return self.getToken(gramaticaParser.VG, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_readcmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadcmd" ):
                listener.enterReadcmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadcmd" ):
                listener.exitReadcmd(self)




    def readcmd(self):

        localctx = gramaticaParser.ReadcmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_readcmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(gramaticaParser.T__6)
            self.state = 58
            self.match(gramaticaParser.AP)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 59
                self.match(gramaticaParser.TEXT)
                self.state = 60
                self.match(gramaticaParser.VG)


            self.state = 63
            self.match(gramaticaParser.ID)
            self.state = 64
            self.match(gramaticaParser.FP)
            self.state = 65
            self.match(gramaticaParser.PV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtrbcmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def atrbcmdL(self):
            return self.getTypedRuleContext(gramaticaParser.AtrbcmdLContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_atrbcmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtrbcmd" ):
                listener.enterAtrbcmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtrbcmd" ):
                listener.exitAtrbcmd(self)




    def atrbcmd(self):

        localctx = gramaticaParser.AtrbcmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atrbcmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(gramaticaParser.ID)
            self.state = 68
            self.atrbcmdL()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtrbcmdLContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_atrbcmdL

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtrbcmdL" ):
                listener.enterAtrbcmdL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtrbcmdL" ):
                listener.exitAtrbcmdL(self)




    def atrbcmdL(self):

        localctx = gramaticaParser.AtrbcmdLContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_atrbcmdL)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(gramaticaParser.T__7)
            self.state = 71
            self.expr()
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

        def PV(self):
            return self.getToken(gramaticaParser.PV, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def NUM(self):
            return self.getToken(gramaticaParser.NUM, 0)

        def TEXT(self):
            return self.getToken(gramaticaParser.TEXT, 0)

        def exprL(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExprLContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExprLContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = gramaticaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 49664) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 74
                self.exprL()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(gramaticaParser.PV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprLContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP(self):
            return self.getToken(gramaticaParser.OP, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def NUM(self):
            return self.getToken(gramaticaParser.NUM, 0)

        def TEXT(self):
            return self.getToken(gramaticaParser.TEXT, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_exprL

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprL" ):
                listener.enterExprL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprL" ):
                listener.exitExprL(self)




    def exprL(self):

        localctx = gramaticaParser.ExprLContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exprL)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(gramaticaParser.OP)
            self.state = 83
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 49664) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





