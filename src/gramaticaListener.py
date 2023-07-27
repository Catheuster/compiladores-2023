# Generated from gramatica.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#programa.
    def enterPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#programa.
    def exitPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#dclr.
    def enterDclr(self, ctx:gramaticaParser.DclrContext):
        pass

    # Exit a parse tree produced by gramaticaParser#dclr.
    def exitDclr(self, ctx:gramaticaParser.DclrContext):
        pass


    # Enter a parse tree produced by gramaticaParser#tipo.
    def enterTipo(self, ctx:gramaticaParser.TipoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#tipo.
    def exitTipo(self, ctx:gramaticaParser.TipoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmd.
    def enterCmd(self, ctx:gramaticaParser.CmdContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmd.
    def exitCmd(self, ctx:gramaticaParser.CmdContext):
        pass


    # Enter a parse tree produced by gramaticaParser#showcmd.
    def enterShowcmd(self, ctx:gramaticaParser.ShowcmdContext):
        pass

    # Exit a parse tree produced by gramaticaParser#showcmd.
    def exitShowcmd(self, ctx:gramaticaParser.ShowcmdContext):
        pass


    # Enter a parse tree produced by gramaticaParser#readcmd.
    def enterReadcmd(self, ctx:gramaticaParser.ReadcmdContext):
        pass

    # Exit a parse tree produced by gramaticaParser#readcmd.
    def exitReadcmd(self, ctx:gramaticaParser.ReadcmdContext):
        pass


    # Enter a parse tree produced by gramaticaParser#atrbcmd.
    def enterAtrbcmd(self, ctx:gramaticaParser.AtrbcmdContext):
        pass

    # Exit a parse tree produced by gramaticaParser#atrbcmd.
    def exitAtrbcmd(self, ctx:gramaticaParser.AtrbcmdContext):
        pass


    # Enter a parse tree produced by gramaticaParser#atrbcmdL.
    def enterAtrbcmdL(self, ctx:gramaticaParser.AtrbcmdLContext):
        pass

    # Exit a parse tree produced by gramaticaParser#atrbcmdL.
    def exitAtrbcmdL(self, ctx:gramaticaParser.AtrbcmdLContext):
        pass


    # Enter a parse tree produced by gramaticaParser#expr.
    def enterExpr(self, ctx:gramaticaParser.ExprContext):
        pass

    # Exit a parse tree produced by gramaticaParser#expr.
    def exitExpr(self, ctx:gramaticaParser.ExprContext):
        pass


    # Enter a parse tree produced by gramaticaParser#exprL.
    def enterExprL(self, ctx:gramaticaParser.ExprLContext):
        pass

    # Exit a parse tree produced by gramaticaParser#exprL.
    def exitExprL(self, ctx:gramaticaParser.ExprLContext):
        pass



del gramaticaParser