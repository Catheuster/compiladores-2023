# Generated from IsiLanguage.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .IsiLanguageParser import IsiLanguageParser
else:
    from IsiLanguageParser import IsiLanguageParser

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


# This class defines a complete listener for a parse tree produced by IsiLanguageParser.
class IsiLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by IsiLanguageParser#prog.
    def enterProg(self, ctx:IsiLanguageParser.ProgContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#prog.
    def exitProg(self, ctx:IsiLanguageParser.ProgContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#declaration.
    def enterDeclaration(self, ctx:IsiLanguageParser.DeclarationContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#declaration.
    def exitDeclaration(self, ctx:IsiLanguageParser.DeclarationContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#tipo.
    def enterTipo(self, ctx:IsiLanguageParser.TipoContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#tipo.
    def exitTipo(self, ctx:IsiLanguageParser.TipoContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#block.
    def enterBlock(self, ctx:IsiLanguageParser.BlockContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#block.
    def exitBlock(self, ctx:IsiLanguageParser.BlockContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#cmd.
    def enterCmd(self, ctx:IsiLanguageParser.CmdContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#cmd.
    def exitCmd(self, ctx:IsiLanguageParser.CmdContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#cmdRead.
    def enterCmdRead(self, ctx:IsiLanguageParser.CmdReadContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#cmdRead.
    def exitCmdRead(self, ctx:IsiLanguageParser.CmdReadContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#cmdWrite.
    def enterCmdWrite(self, ctx:IsiLanguageParser.CmdWriteContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#cmdWrite.
    def exitCmdWrite(self, ctx:IsiLanguageParser.CmdWriteContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#cmdAssign.
    def enterCmdAssign(self, ctx:IsiLanguageParser.CmdAssignContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#cmdAssign.
    def exitCmdAssign(self, ctx:IsiLanguageParser.CmdAssignContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#cmdIf.
    def enterCmdIf(self, ctx:IsiLanguageParser.CmdIfContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#cmdIf.
    def exitCmdIf(self, ctx:IsiLanguageParser.CmdIfContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#cmdWhile.
    def enterCmdWhile(self, ctx:IsiLanguageParser.CmdWhileContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#cmdWhile.
    def exitCmdWhile(self, ctx:IsiLanguageParser.CmdWhileContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#cmdDoWhile.
    def enterCmdDoWhile(self, ctx:IsiLanguageParser.CmdDoWhileContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#cmdDoWhile.
    def exitCmdDoWhile(self, ctx:IsiLanguageParser.CmdDoWhileContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#expr.
    def enterExpr(self, ctx:IsiLanguageParser.ExprContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#expr.
    def exitExpr(self, ctx:IsiLanguageParser.ExprContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#term.
    def enterTerm(self, ctx:IsiLanguageParser.TermContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#term.
    def exitTerm(self, ctx:IsiLanguageParser.TermContext):
        pass



del IsiLanguageParser