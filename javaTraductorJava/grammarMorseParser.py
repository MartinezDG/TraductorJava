# Generated from grammarMorse.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("k\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\6\2")
        buf.write("\34\n\2\r\2\16\2\35\3\3\3\3\3\3\3\3\5\3$\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\7\b=\n\b\f\b\16\b@\13\b\5")
        buf.write("\bB\n\b\3\t\3\t\6\tF\n\t\r\t\16\tG\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\7\nP\n\n\f\n\16\nS\13\n\3\13\3\13\3\13\3\13\5\13")
        buf.write("Y\n\13\3\f\3\f\3\f\3\f\3\f\7\f`\n\f\f\f\16\fc\13\f\5\f")
        buf.write("e\n\f\3\f\3\f\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\2\3\3\2\f\r\2k\2\33\3\2\2\2\4#\3\2\2\2\6%\3")
        buf.write("\2\2\2\b-\3\2\2\2\n\62\3\2\2\2\f\65\3\2\2\2\16A\3\2\2")
        buf.write("\2\20C\3\2\2\2\22K\3\2\2\2\24X\3\2\2\2\26Z\3\2\2\2\30")
        buf.write("h\3\2\2\2\32\34\5\4\3\2\33\32\3\2\2\2\34\35\3\2\2\2\35")
        buf.write("\33\3\2\2\2\35\36\3\2\2\2\36\3\3\2\2\2\37$\5\6\4\2 $\5")
        buf.write("\b\5\2!$\5\n\6\2\"$\5\f\7\2#\37\3\2\2\2# \3\2\2\2#!\3")
        buf.write("\2\2\2#\"\3\2\2\2$\5\3\2\2\2%&\7\6\2\2&\'\7\21\2\2\'(")
        buf.write("\7\b\2\2()\5\16\b\2)*\7\t\2\2*+\7\n\2\2+,\5\20\t\2,\7")
        buf.write("\3\2\2\2-.\7\5\2\2./\7\b\2\2/\60\5\22\n\2\60\61\7\t\2")
        buf.write("\2\61\t\3\2\2\2\62\63\7\7\2\2\63\64\5\22\n\2\64\13\3\2")
        buf.write("\2\2\65\66\7\21\2\2\66\67\7\16\2\2\678\5\22\n\28\r\3\2")
        buf.write("\2\29>\7\21\2\2:;\7\13\2\2;=\7\21\2\2<:\3\2\2\2=@\3\2")
        buf.write("\2\2><\3\2\2\2>?\3\2\2\2?B\3\2\2\2@>\3\2\2\2A9\3\2\2\2")
        buf.write("AB\3\2\2\2B\17\3\2\2\2CE\7\3\2\2DF\5\4\3\2ED\3\2\2\2F")
        buf.write("G\3\2\2\2GE\3\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\7\4\2\2J\21")
        buf.write("\3\2\2\2KQ\5\24\13\2LM\5\30\r\2MN\5\24\13\2NP\3\2\2\2")
        buf.write("OL\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\23\3\2\2\2S")
        buf.write("Q\3\2\2\2TY\7\21\2\2UY\7\20\2\2VY\7\22\2\2WY\5\26\f\2")
        buf.write("XT\3\2\2\2XU\3\2\2\2XV\3\2\2\2XW\3\2\2\2Y\25\3\2\2\2Z")
        buf.write("[\7\21\2\2[d\7\b\2\2\\a\5\22\n\2]^\7\13\2\2^`\5\22\n\2")
        buf.write("_]\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2be\3\2\2\2ca\3")
        buf.write("\2\2\2d\\\3\2\2\2de\3\2\2\2ef\3\2\2\2fg\7\t\2\2g\27\3")
        buf.write("\2\2\2hi\t\2\2\2i\31\3\2\2\2\13\35#>AGQXad")
        return buf.getvalue()


class grammarMorseParser ( Parser ):

    grammarFileName = "grammarMorse.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'print'", "'def'", "'return'", 
                     "'('", "')'", "':'", "','", "'*'", "'-'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "PRINT", "DEF", 
                      "RETURN", "LPAREN", "RPAREN", "COLON", "COMMA", "STAR", 
                      "MINUS", "EQUALS", "WS", "NUMBER", "ID", "STRING" ]

    RULE_morse_line = 0
    RULE_statement = 1
    RULE_func_def = 2
    RULE_print_stmt = 3
    RULE_return_stmt = 4
    RULE_assign_stmt = 5
    RULE_param_list = 6
    RULE_block = 7
    RULE_expression = 8
    RULE_primary = 9
    RULE_func_call = 10
    RULE_expr_op = 11

    ruleNames =  [ "morse_line", "statement", "func_def", "print_stmt", 
                   "return_stmt", "assign_stmt", "param_list", "block", 
                   "expression", "primary", "func_call", "expr_op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    PRINT=3
    DEF=4
    RETURN=5
    LPAREN=6
    RPAREN=7
    COLON=8
    COMMA=9
    STAR=10
    MINUS=11
    EQUALS=12
    WS=13
    NUMBER=14
    ID=15
    STRING=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Morse_lineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarMorseParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammarMorseParser.StatementContext,i)


        def getRuleIndex(self):
            return grammarMorseParser.RULE_morse_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMorse_line" ):
                listener.enterMorse_line(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMorse_line" ):
                listener.exitMorse_line(self)




    def morse_line(self):

        localctx = grammarMorseParser.Morse_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_morse_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.statement()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammarMorseParser.PRINT) | (1 << grammarMorseParser.DEF) | (1 << grammarMorseParser.RETURN) | (1 << grammarMorseParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_def(self):
            return self.getTypedRuleContext(grammarMorseParser.Func_defContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(grammarMorseParser.Print_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(grammarMorseParser.Return_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(grammarMorseParser.Assign_stmtContext,0)


        def getRuleIndex(self):
            return grammarMorseParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = grammarMorseParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarMorseParser.DEF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.func_def()
                pass
            elif token in [grammarMorseParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.print_stmt()
                pass
            elif token in [grammarMorseParser.RETURN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.return_stmt()
                pass
            elif token in [grammarMorseParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.assign_stmt()
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

    class Func_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(grammarMorseParser.DEF, 0)

        def ID(self):
            return self.getToken(grammarMorseParser.ID, 0)

        def LPAREN(self):
            return self.getToken(grammarMorseParser.LPAREN, 0)

        def param_list(self):
            return self.getTypedRuleContext(grammarMorseParser.Param_listContext,0)


        def RPAREN(self):
            return self.getToken(grammarMorseParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(grammarMorseParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(grammarMorseParser.BlockContext,0)


        def getRuleIndex(self):
            return grammarMorseParser.RULE_func_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_def" ):
                listener.enterFunc_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_def" ):
                listener.exitFunc_def(self)




    def func_def(self):

        localctx = grammarMorseParser.Func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(grammarMorseParser.DEF)
            self.state = 36
            self.match(grammarMorseParser.ID)
            self.state = 37
            self.match(grammarMorseParser.LPAREN)
            self.state = 38
            self.param_list()
            self.state = 39
            self.match(grammarMorseParser.RPAREN)
            self.state = 40
            self.match(grammarMorseParser.COLON)
            self.state = 41
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Print_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(grammarMorseParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(grammarMorseParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarMorseParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(grammarMorseParser.RPAREN, 0)

        def getRuleIndex(self):
            return grammarMorseParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)




    def print_stmt(self):

        localctx = grammarMorseParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(grammarMorseParser.PRINT)
            self.state = 44
            self.match(grammarMorseParser.LPAREN)
            self.state = 45
            self.expression()
            self.state = 46
            self.match(grammarMorseParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(grammarMorseParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarMorseParser.ExpressionContext,0)


        def getRuleIndex(self):
            return grammarMorseParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)




    def return_stmt(self):

        localctx = grammarMorseParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(grammarMorseParser.RETURN)
            self.state = 49
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammarMorseParser.ID, 0)

        def EQUALS(self):
            return self.getToken(grammarMorseParser.EQUALS, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarMorseParser.ExpressionContext,0)


        def getRuleIndex(self):
            return grammarMorseParser.RULE_assign_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)




    def assign_stmt(self):

        localctx = grammarMorseParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(grammarMorseParser.ID)
            self.state = 52
            self.match(grammarMorseParser.EQUALS)
            self.state = 53
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(grammarMorseParser.ID)
            else:
                return self.getToken(grammarMorseParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarMorseParser.COMMA)
            else:
                return self.getToken(grammarMorseParser.COMMA, i)

        def getRuleIndex(self):
            return grammarMorseParser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)




    def param_list(self):

        localctx = grammarMorseParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==grammarMorseParser.ID:
                self.state = 55
                self.match(grammarMorseParser.ID)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==grammarMorseParser.COMMA:
                    self.state = 56
                    self.match(grammarMorseParser.COMMA)
                    self.state = 57
                    self.match(grammarMorseParser.ID)
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarMorseParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammarMorseParser.StatementContext,i)


        def getRuleIndex(self):
            return grammarMorseParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = grammarMorseParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(grammarMorseParser.T__0)
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.statement()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammarMorseParser.PRINT) | (1 << grammarMorseParser.DEF) | (1 << grammarMorseParser.RETURN) | (1 << grammarMorseParser.ID))) != 0)):
                    break

            self.state = 71
            self.match(grammarMorseParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarMorseParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(grammarMorseParser.PrimaryContext,i)


        def expr_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarMorseParser.Expr_opContext)
            else:
                return self.getTypedRuleContext(grammarMorseParser.Expr_opContext,i)


        def getRuleIndex(self):
            return grammarMorseParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = grammarMorseParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.primary()
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==grammarMorseParser.STAR or _la==grammarMorseParser.MINUS:
                self.state = 74
                self.expr_op()
                self.state = 75
                self.primary()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammarMorseParser.ID, 0)

        def NUMBER(self):
            return self.getToken(grammarMorseParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(grammarMorseParser.STRING, 0)

        def func_call(self):
            return self.getTypedRuleContext(grammarMorseParser.Func_callContext,0)


        def getRuleIndex(self):
            return grammarMorseParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = grammarMorseParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_primary)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(grammarMorseParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(grammarMorseParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.match(grammarMorseParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammarMorseParser.ID, 0)

        def LPAREN(self):
            return self.getToken(grammarMorseParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(grammarMorseParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarMorseParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grammarMorseParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarMorseParser.COMMA)
            else:
                return self.getToken(grammarMorseParser.COMMA, i)

        def getRuleIndex(self):
            return grammarMorseParser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)




    def func_call(self):

        localctx = grammarMorseParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(grammarMorseParser.ID)
            self.state = 89
            self.match(grammarMorseParser.LPAREN)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammarMorseParser.NUMBER) | (1 << grammarMorseParser.ID) | (1 << grammarMorseParser.STRING))) != 0):
                self.state = 90
                self.expression()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==grammarMorseParser.COMMA:
                    self.state = 91
                    self.match(grammarMorseParser.COMMA)
                    self.state = 92
                    self.expression()
                    self.state = 97
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 100
            self.match(grammarMorseParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(grammarMorseParser.STAR, 0)

        def MINUS(self):
            return self.getToken(grammarMorseParser.MINUS, 0)

        def getRuleIndex(self):
            return grammarMorseParser.RULE_expr_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_op" ):
                listener.enterExpr_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_op" ):
                listener.exitExpr_op(self)




    def expr_op(self):

        localctx = grammarMorseParser.Expr_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not(_la==grammarMorseParser.STAR or _la==grammarMorseParser.MINUS):
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





