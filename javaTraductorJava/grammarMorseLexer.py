# Generated from grammarMorse.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("k\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\6\16H\n\16\r\16\16\16I\3\16\3\16")
        buf.write("\3\17\6\17O\n\17\r\17\16\17P\3\20\3\20\7\20U\n\20\f\20")
        buf.write("\16\20X\13\20\3\21\3\21\7\21\\\n\21\f\21\16\21_\13\21")
        buf.write("\3\21\3\21\3\21\7\21d\n\21\f\21\16\21g\13\21\3\21\5\21")
        buf.write("j\n\21\4]e\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22\3\2\6\5\2\13")
        buf.write("\f\17\17\"\"\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\2p\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5%\3")
        buf.write("\2\2\2\7\'\3\2\2\2\t-\3\2\2\2\13\61\3\2\2\2\r8\3\2\2\2")
        buf.write("\17:\3\2\2\2\21<\3\2\2\2\23>\3\2\2\2\25@\3\2\2\2\27B\3")
        buf.write("\2\2\2\31D\3\2\2\2\33G\3\2\2\2\35N\3\2\2\2\37R\3\2\2\2")
        buf.write("!i\3\2\2\2#$\7}\2\2$\4\3\2\2\2%&\7\177\2\2&\6\3\2\2\2")
        buf.write("\'(\7r\2\2()\7t\2\2)*\7k\2\2*+\7p\2\2+,\7v\2\2,\b\3\2")
        buf.write("\2\2-.\7f\2\2./\7g\2\2/\60\7h\2\2\60\n\3\2\2\2\61\62\7")
        buf.write("t\2\2\62\63\7g\2\2\63\64\7v\2\2\64\65\7w\2\2\65\66\7t")
        buf.write("\2\2\66\67\7p\2\2\67\f\3\2\2\289\7*\2\29\16\3\2\2\2:;")
        buf.write("\7+\2\2;\20\3\2\2\2<=\7<\2\2=\22\3\2\2\2>?\7.\2\2?\24")
        buf.write("\3\2\2\2@A\7,\2\2A\26\3\2\2\2BC\7/\2\2C\30\3\2\2\2DE\7")
        buf.write("?\2\2E\32\3\2\2\2FH\t\2\2\2GF\3\2\2\2HI\3\2\2\2IG\3\2")
        buf.write("\2\2IJ\3\2\2\2JK\3\2\2\2KL\b\16\2\2L\34\3\2\2\2MO\t\3")
        buf.write("\2\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\36\3\2\2")
        buf.write("\2RV\t\4\2\2SU\t\5\2\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2V")
        buf.write("W\3\2\2\2W \3\2\2\2XV\3\2\2\2Y]\7$\2\2Z\\\13\2\2\2[Z\3")
        buf.write("\2\2\2\\_\3\2\2\2]^\3\2\2\2][\3\2\2\2^`\3\2\2\2_]\3\2")
        buf.write("\2\2`j\7$\2\2ae\7)\2\2bd\13\2\2\2cb\3\2\2\2dg\3\2\2\2")
        buf.write("ef\3\2\2\2ec\3\2\2\2fh\3\2\2\2ge\3\2\2\2hj\7)\2\2iY\3")
        buf.write("\2\2\2ia\3\2\2\2j\"\3\2\2\2\t\2IPV]ei\3\b\2\2")
        return buf.getvalue()


class grammarMorseLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    PRINT = 3
    DEF = 4
    RETURN = 5
    LPAREN = 6
    RPAREN = 7
    COLON = 8
    COMMA = 9
    STAR = 10
    MINUS = 11
    EQUALS = 12
    WS = 13
    NUMBER = 14
    ID = 15
    STRING = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'print'", "'def'", "'return'", "'('", "')'", 
            "':'", "','", "'*'", "'-'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "PRINT", "DEF", "RETURN", "LPAREN", "RPAREN", "COLON", "COMMA", 
            "STAR", "MINUS", "EQUALS", "WS", "NUMBER", "ID", "STRING" ]

    ruleNames = [ "T__0", "T__1", "PRINT", "DEF", "RETURN", "LPAREN", "RPAREN", 
                  "COLON", "COMMA", "STAR", "MINUS", "EQUALS", "WS", "NUMBER", 
                  "ID", "STRING" ]

    grammarFileName = "grammarMorse.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


