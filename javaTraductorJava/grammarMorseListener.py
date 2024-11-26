# Generated from grammarMorse.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grammarMorseParser import grammarMorseParser
else:
    from grammarMorseParser import grammarMorseParser

# This class defines a complete listener for a parse tree produced by grammarMorseParser.
class grammarMorseListener(ParseTreeListener):

    # Enter a parse tree produced by grammarMorseParser#morse_line.
    def enterMorse_line(self, ctx:grammarMorseParser.Morse_lineContext):
        pass

    # Exit a parse tree produced by grammarMorseParser#morse_line.
    def exitMorse_line(self, ctx:grammarMorseParser.Morse_lineContext):
        pass


    # Enter a parse tree produced by grammarMorseParser#statement.
    def enterStatement(self, ctx:grammarMorseParser.StatementContext):
        pass

    # Exit a parse tree produced by grammarMorseParser#statement.
    def exitStatement(self, ctx:grammarMorseParser.StatementContext):
        pass


    # Enter a parse tree produced by grammarMorseParser#func_def.
    def enterFunc_def(self, ctx:grammarMorseParser.Func_defContext):
        pass

    # Exit a parse tree produced by grammarMorseParser#func_def.
    def exitFunc_def(self, ctx:grammarMorseParser.Func_defContext):
        pass


    # Enter a parse tree produced by grammarMorseParser#print_stmt.
    def enterPrint_stmt(self, ctx:grammarMorseParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by grammarMorseParser#print_stmt.
    def exitPrint_stmt(self, ctx:grammarMorseParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by grammarMorseParser#return_stmt.
    def enterReturn_stmt(self, ctx:grammarMorseParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by grammarMorseParser#return_stmt.
    def exitReturn_stmt(self, ctx:grammarMorseParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by grammarMorseParser#assign_stmt.
    def enterAssign_stmt(self, ctx:grammarMorseParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by grammarMorseParser#assign_stmt.
    def exitAssign_stmt(self, ctx:grammarMorseParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by grammarMorseParser#param_list.
    def enterParam_list(self, ctx:grammarMorseParser.Param_listContext):
        pass

    # Exit a parse tree produced by grammarMorseParser#param_list.
    def exitParam_list(self, ctx:grammarMorseParser.Param_listContext):
        pass


    # Enter a parse tree produced by grammarMorseParser#block.
    def enterBlock(self, ctx:grammarMorseParser.BlockContext):
        pass

    # Exit a parse tree produced by grammarMorseParser#block.
    def exitBlock(self, ctx:grammarMorseParser.BlockContext):
        pass


    # Enter a parse tree produced by grammarMorseParser#expression.
    def enterExpression(self, ctx:grammarMorseParser.ExpressionContext):
        pass

    # Exit a parse tree produced by grammarMorseParser#expression.
    def exitExpression(self, ctx:grammarMorseParser.ExpressionContext):
        pass


    # Enter a parse tree produced by grammarMorseParser#primary.
    def enterPrimary(self, ctx:grammarMorseParser.PrimaryContext):
        pass

    # Exit a parse tree produced by grammarMorseParser#primary.
    def exitPrimary(self, ctx:grammarMorseParser.PrimaryContext):
        pass


    # Enter a parse tree produced by grammarMorseParser#func_call.
    def enterFunc_call(self, ctx:grammarMorseParser.Func_callContext):
        pass

    # Exit a parse tree produced by grammarMorseParser#func_call.
    def exitFunc_call(self, ctx:grammarMorseParser.Func_callContext):
        pass


    # Enter a parse tree produced by grammarMorseParser#expr_op.
    def enterExpr_op(self, ctx:grammarMorseParser.Expr_opContext):
        pass

    # Exit a parse tree produced by grammarMorseParser#expr_op.
    def exitExpr_op(self, ctx:grammarMorseParser.Expr_opContext):
        pass


