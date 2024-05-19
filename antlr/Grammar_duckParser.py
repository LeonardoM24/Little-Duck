# Generated from Grammar_duck.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import sys
sys.path.insert(0, './Semantica.py') 
from Semantica import Semantica
global semantica
semantica = Semantica()

def serializedATN():
    return [
        4,1,33,302,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,1,1,1,1,1,3,1,87,8,1,1,2,1,2,3,2,91,8,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,4,3,100,8,3,11,3,12,3,101,1,4,1,4,1,4,1,4,3,4,108,8,4,1,5,
        1,5,1,5,1,5,1,6,5,6,115,8,6,10,6,12,6,118,9,6,1,7,1,7,1,7,1,7,1,
        7,3,7,125,8,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,137,8,
        9,1,10,1,10,3,10,141,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,
        1,14,3,14,165,8,14,1,15,1,15,3,15,169,8,15,1,16,1,16,1,16,1,16,1,
        17,1,17,1,17,1,17,1,17,1,17,3,17,181,8,17,1,18,1,18,1,18,1,18,1,
        18,1,18,5,18,189,8,18,10,18,12,18,192,9,18,1,19,1,19,1,19,1,19,3,
        19,198,8,19,1,20,1,20,1,20,1,20,5,20,204,8,20,10,20,12,20,207,9,
        20,1,21,1,21,1,21,1,21,1,21,1,21,5,21,215,8,21,10,21,12,21,218,9,
        21,1,22,1,22,1,22,1,22,3,22,224,8,22,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,3,23,237,8,23,1,24,1,24,1,24,1,24,3,
        24,243,8,24,1,25,1,25,1,25,3,25,248,8,25,1,26,1,26,1,26,1,26,3,26,
        254,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,28,3,28,271,8,28,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,3,29,281,8,29,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,
        1,32,1,32,1,32,3,32,294,8,32,1,33,1,33,1,33,1,33,3,33,300,8,33,1,
        33,0,0,34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,0,0,296,0,68,1,0,0,0,2,
        86,1,0,0,0,4,90,1,0,0,0,6,99,1,0,0,0,8,103,1,0,0,0,10,109,1,0,0,
        0,12,116,1,0,0,0,14,124,1,0,0,0,16,126,1,0,0,0,18,136,1,0,0,0,20,
        140,1,0,0,0,22,142,1,0,0,0,24,150,1,0,0,0,26,156,1,0,0,0,28,164,
        1,0,0,0,30,166,1,0,0,0,32,170,1,0,0,0,34,180,1,0,0,0,36,182,1,0,
        0,0,38,197,1,0,0,0,40,199,1,0,0,0,42,208,1,0,0,0,44,223,1,0,0,0,
        46,236,1,0,0,0,48,242,1,0,0,0,50,247,1,0,0,0,52,253,1,0,0,0,54,255,
        1,0,0,0,56,270,1,0,0,0,58,272,1,0,0,0,60,282,1,0,0,0,62,284,1,0,
        0,0,64,293,1,0,0,0,66,299,1,0,0,0,68,69,5,1,0,0,69,70,6,0,-1,0,70,
        71,6,0,-1,0,71,72,5,30,0,0,72,73,6,0,-1,0,73,74,5,2,0,0,74,75,3,
        4,2,0,75,76,3,2,1,0,76,77,5,3,0,0,77,78,3,10,5,0,78,79,5,4,0,0,79,
        80,6,0,-1,0,80,81,6,0,-1,0,81,82,5,0,0,1,82,1,1,0,0,0,83,84,3,54,
        27,0,84,85,3,2,1,0,85,87,1,0,0,0,86,83,1,0,0,0,86,87,1,0,0,0,87,
        3,1,0,0,0,88,89,5,5,0,0,89,91,3,6,3,0,90,88,1,0,0,0,90,91,1,0,0,
        0,91,5,1,0,0,0,92,93,6,3,-1,0,93,94,3,8,4,0,94,95,5,6,0,0,95,96,
        5,29,0,0,96,97,6,3,-1,0,97,98,5,2,0,0,98,100,1,0,0,0,99,92,1,0,0,
        0,100,101,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,7,1,0,0,0,103,
        104,5,30,0,0,104,107,6,4,-1,0,105,106,5,7,0,0,106,108,3,8,4,0,107,
        105,1,0,0,0,107,108,1,0,0,0,108,9,1,0,0,0,109,110,5,8,0,0,110,111,
        3,12,6,0,111,112,5,9,0,0,112,11,1,0,0,0,113,115,3,14,7,0,114,113,
        1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,13,1,
        0,0,0,118,116,1,0,0,0,119,125,3,22,11,0,120,125,3,26,13,0,121,125,
        3,24,12,0,122,125,3,62,31,0,123,125,3,16,8,0,124,119,1,0,0,0,124,
        120,1,0,0,0,124,121,1,0,0,0,124,122,1,0,0,0,124,123,1,0,0,0,125,
        15,1,0,0,0,126,127,5,10,0,0,127,128,3,18,9,0,128,129,5,11,0,0,129,
        130,5,2,0,0,130,17,1,0,0,0,131,137,3,20,10,0,132,133,3,20,10,0,133,
        134,5,7,0,0,134,135,3,18,9,0,135,137,1,0,0,0,136,131,1,0,0,0,136,
        132,1,0,0,0,137,19,1,0,0,0,138,141,3,30,15,0,139,141,5,33,0,0,140,
        138,1,0,0,0,140,139,1,0,0,0,141,21,1,0,0,0,142,143,5,30,0,0,143,
        144,6,11,-1,0,144,145,5,12,0,0,145,146,6,11,-1,0,146,147,3,30,15,
        0,147,148,5,2,0,0,148,149,6,11,-1,0,149,23,1,0,0,0,150,151,5,13,
        0,0,151,152,3,10,5,0,152,153,5,14,0,0,153,154,3,30,15,0,154,155,
        5,2,0,0,155,25,1,0,0,0,156,157,5,15,0,0,157,158,3,30,15,0,158,159,
        3,10,5,0,159,160,3,28,14,0,160,161,5,2,0,0,161,27,1,0,0,0,162,163,
        5,16,0,0,163,165,3,10,5,0,164,162,1,0,0,0,164,165,1,0,0,0,165,29,
        1,0,0,0,166,168,3,36,18,0,167,169,3,32,16,0,168,167,1,0,0,0,168,
        169,1,0,0,0,169,31,1,0,0,0,170,171,3,34,17,0,171,172,3,36,18,0,172,
        173,6,16,-1,0,173,33,1,0,0,0,174,175,5,17,0,0,175,181,6,17,-1,0,
        176,177,5,18,0,0,177,181,6,17,-1,0,178,179,5,19,0,0,179,181,6,17,
        -1,0,180,174,1,0,0,0,180,176,1,0,0,0,180,178,1,0,0,0,181,35,1,0,
        0,0,182,183,3,42,21,0,183,190,6,18,-1,0,184,185,3,38,19,0,185,186,
        3,42,21,0,186,187,6,18,-1,0,187,189,1,0,0,0,188,184,1,0,0,0,189,
        192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,37,1,0,0,0,192,190,
        1,0,0,0,193,194,5,20,0,0,194,198,6,19,-1,0,195,196,5,21,0,0,196,
        198,6,19,-1,0,197,193,1,0,0,0,197,195,1,0,0,0,198,39,1,0,0,0,199,
        205,3,46,23,0,200,201,3,44,22,0,201,202,3,46,23,0,202,204,1,0,0,
        0,203,200,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,
        0,206,41,1,0,0,0,207,205,1,0,0,0,208,209,3,46,23,0,209,216,6,21,
        -1,0,210,211,3,44,22,0,211,212,3,46,23,0,212,213,6,21,-1,0,213,215,
        1,0,0,0,214,210,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,
        1,0,0,0,217,43,1,0,0,0,218,216,1,0,0,0,219,220,5,22,0,0,220,224,
        6,22,-1,0,221,222,5,23,0,0,222,224,6,22,-1,0,223,219,1,0,0,0,223,
        221,1,0,0,0,224,45,1,0,0,0,225,226,5,24,0,0,226,227,6,23,-1,0,227,
        228,3,30,15,0,228,229,5,11,0,0,229,230,6,23,-1,0,230,237,1,0,0,0,
        231,232,3,48,24,0,232,233,3,50,25,0,233,234,6,23,-1,0,234,237,1,
        0,0,0,235,237,3,50,25,0,236,225,1,0,0,0,236,231,1,0,0,0,236,235,
        1,0,0,0,237,47,1,0,0,0,238,239,5,20,0,0,239,243,6,24,-1,0,240,241,
        5,21,0,0,241,243,6,24,-1,0,242,238,1,0,0,0,242,240,1,0,0,0,243,49,
        1,0,0,0,244,245,5,30,0,0,245,248,6,25,-1,0,246,248,3,52,26,0,247,
        244,1,0,0,0,247,246,1,0,0,0,248,51,1,0,0,0,249,250,5,31,0,0,250,
        254,6,26,-1,0,251,252,5,32,0,0,252,254,6,26,-1,0,253,249,1,0,0,0,
        253,251,1,0,0,0,254,53,1,0,0,0,255,256,5,25,0,0,256,257,6,27,-1,
        0,257,258,5,30,0,0,258,259,6,27,-1,0,259,260,5,24,0,0,260,261,3,
        56,28,0,261,262,5,11,0,0,262,263,5,26,0,0,263,264,3,60,30,0,264,
        265,3,10,5,0,265,266,5,27,0,0,266,267,5,2,0,0,267,268,6,27,-1,0,
        268,55,1,0,0,0,269,271,3,58,29,0,270,269,1,0,0,0,270,271,1,0,0,0,
        271,57,1,0,0,0,272,273,5,30,0,0,273,274,6,29,-1,0,274,275,5,6,0,
        0,275,276,5,29,0,0,276,277,6,29,-1,0,277,280,1,0,0,0,278,279,5,7,
        0,0,279,281,3,58,29,0,280,278,1,0,0,0,280,281,1,0,0,0,281,59,1,0,
        0,0,282,283,3,4,2,0,283,61,1,0,0,0,284,285,5,30,0,0,285,286,5,24,
        0,0,286,287,3,64,32,0,287,288,5,11,0,0,288,289,5,2,0,0,289,63,1,
        0,0,0,290,291,3,30,15,0,291,292,3,66,33,0,292,294,1,0,0,0,293,290,
        1,0,0,0,293,294,1,0,0,0,294,65,1,0,0,0,295,296,5,7,0,0,296,297,3,
        30,15,0,297,298,3,66,33,0,298,300,1,0,0,0,299,295,1,0,0,0,299,300,
        1,0,0,0,300,67,1,0,0,0,24,86,90,101,107,116,124,136,140,164,168,
        180,190,197,205,216,223,236,242,247,253,270,280,293,299
    ]

class Grammar_duckParser ( Parser ):

    grammarFileName = "Grammar_duck.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'main'", "'end'", 
                     "'var'", "':'", "','", "'{'", "'}'", "'print('", "')'", 
                     "'='", "'do'", "'while'", "'if'", "'else'", "'<'", 
                     "'>'", "'!='", "'+'", "'-'", "'*'", "'/'", "'('", "'void'", 
                     "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SKIPS", "TYPE", "ID", "CTE_INT", "CTE_FLOAT", "CTE_STRING" ]

    RULE_prog = 0
    RULE_a_funcs = 1
    RULE_vars = 2
    RULE_more_vars = 3
    RULE_list_id = 4
    RULE_body = 5
    RULE_list_statement = 6
    RULE_statement = 7
    RULE_print = 8
    RULE_list_expresion = 9
    RULE_exp_o_string = 10
    RULE_assign = 11
    RULE_cycle = 12
    RULE_condition = 13
    RULE_else = 14
    RULE_expresion = 15
    RULE_comparar = 16
    RULE_comparacion = 17
    RULE_exp = 18
    RULE_sum_rest = 19
    RULE_x = 20
    RULE_termino = 21
    RULE_mult_div = 22
    RULE_factor = 23
    RULE_positivo_negativo = 24
    RULE_id_cte = 25
    RULE_cte = 26
    RULE_funcs = 27
    RULE_params = 28
    RULE_list_params = 29
    RULE_var_no_var = 30
    RULE_f_call = 31
    RULE_f_list_expresion = 32
    RULE_f_more_expresion = 33

    ruleNames =  [ "prog", "a_funcs", "vars", "more_vars", "list_id", "body", 
                   "list_statement", "statement", "print", "list_expresion", 
                   "exp_o_string", "assign", "cycle", "condition", "else", 
                   "expresion", "comparar", "comparacion", "exp", "sum_rest", 
                   "x", "termino", "mult_div", "factor", "positivo_negativo", 
                   "id_cte", "cte", "funcs", "params", "list_params", "var_no_var", 
                   "f_call", "f_list_expresion", "f_more_expresion" ]

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
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    SKIPS=28
    TYPE=29
    ID=30
    CTE_INT=31
    CTE_FLOAT=32
    CTE_STRING=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def vars_(self):
            return self.getTypedRuleContext(Grammar_duckParser.VarsContext,0)


        def a_funcs(self):
            return self.getTypedRuleContext(Grammar_duckParser.A_funcsContext,0)


        def body(self):
            return self.getTypedRuleContext(Grammar_duckParser.BodyContext,0)


        def EOF(self):
            return self.getToken(Grammar_duckParser.EOF, 0)

        def getRuleIndex(self):
            return Grammar_duckParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = Grammar_duckParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(Grammar_duckParser.T__0)
            global semantica

            semantica.currType = "program"
            self.state = 71
            localctx._ID = self.match(Grammar_duckParser.ID)
            try:
                semantica.addFunc((None if localctx._ID is None else localctx._ID.text), semantica.currType) 
                semantica.currFunc = (None if localctx._ID is None else localctx._ID.text)
                semantica.progName = (None if localctx._ID is None else localctx._ID.text)
            except ValueError as e: 
                print(e)
                sys.exit()
            self.state = 73
            self.match(Grammar_duckParser.T__1)
            self.state = 74
            self.vars_()
            self.state = 75
            self.a_funcs()
            self.state = 76
            self.match(Grammar_duckParser.T__2)
            self.state = 77
            self.body()
            self.state = 78
            self.match(Grammar_duckParser.T__3)
            print(semantica.cuadruplos)
            del semantica
            self.state = 81
            self.match(Grammar_duckParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A_funcsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcs(self):
            return self.getTypedRuleContext(Grammar_duckParser.FuncsContext,0)


        def a_funcs(self):
            return self.getTypedRuleContext(Grammar_duckParser.A_funcsContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_a_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA_funcs" ):
                listener.enterA_funcs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA_funcs" ):
                listener.exitA_funcs(self)




    def a_funcs(self):

        localctx = Grammar_duckParser.A_funcsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_a_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 83
                self.funcs()
                self.state = 84
                self.a_funcs()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def more_vars(self):
            return self.getTypedRuleContext(Grammar_duckParser.More_varsContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)




    def vars_(self):

        localctx = Grammar_duckParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 88
                self.match(Grammar_duckParser.T__4)
                self.state = 89
                self.more_vars()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_varsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._TYPE = None # Token

        def list_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_duckParser.List_idContext)
            else:
                return self.getTypedRuleContext(Grammar_duckParser.List_idContext,i)


        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(Grammar_duckParser.TYPE)
            else:
                return self.getToken(Grammar_duckParser.TYPE, i)

        def getRuleIndex(self):
            return Grammar_duckParser.RULE_more_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMore_vars" ):
                listener.enterMore_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMore_vars" ):
                listener.exitMore_vars(self)




    def more_vars(self):

        localctx = Grammar_duckParser.More_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_more_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                semantica.tempIDS.clear()
                self.state = 93
                self.list_id()
                self.state = 94
                self.match(Grammar_duckParser.T__5)

                self.state = 95
                localctx._TYPE = self.match(Grammar_duckParser.TYPE)

                try:
                    semantica.addListVar(semantica.tempIDS,(None if localctx._TYPE is None else localctx._TYPE.text),semantica.currFunc)
                except ValueError as e:
                    print(e)
                    sys.exit()

                self.state = 97
                self.match(Grammar_duckParser.T__1)
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==30):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def list_id(self):
            return self.getTypedRuleContext(Grammar_duckParser.List_idContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_list_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_id" ):
                listener.enterList_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_id" ):
                listener.exitList_id(self)




    def list_id(self):

        localctx = Grammar_duckParser.List_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            localctx._ID = self.match(Grammar_duckParser.ID)

            semantica.addVarTempList((None if localctx._ID is None else localctx._ID.text))

            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 105
                self.match(Grammar_duckParser.T__6)
                self.state = 106
                self.list_id()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_statement(self):
            return self.getTypedRuleContext(Grammar_duckParser.List_statementContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = Grammar_duckParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(Grammar_duckParser.T__7)
            self.state = 110
            self.list_statement()
            self.state = 111
            self.match(Grammar_duckParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_duckParser.StatementContext)
            else:
                return self.getTypedRuleContext(Grammar_duckParser.StatementContext,i)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_list_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_statement" ):
                listener.enterList_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_statement" ):
                listener.exitList_statement(self)




    def list_statement(self):

        localctx = Grammar_duckParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073783808) != 0):
                self.state = 113
                self.statement()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(Grammar_duckParser.AssignContext,0)


        def condition(self):
            return self.getTypedRuleContext(Grammar_duckParser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(Grammar_duckParser.CycleContext,0)


        def f_call(self):
            return self.getTypedRuleContext(Grammar_duckParser.F_callContext,0)


        def print_(self):
            return self.getTypedRuleContext(Grammar_duckParser.PrintContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = Grammar_duckParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 122
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 123
                self.print_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_expresion(self):
            return self.getTypedRuleContext(Grammar_duckParser.List_expresionContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)




    def print_(self):

        localctx = Grammar_duckParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(Grammar_duckParser.T__9)
            self.state = 127
            self.list_expresion()
            self.state = 128
            self.match(Grammar_duckParser.T__10)
            self.state = 129
            self.match(Grammar_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_o_string(self):
            return self.getTypedRuleContext(Grammar_duckParser.Exp_o_stringContext,0)


        def list_expresion(self):
            return self.getTypedRuleContext(Grammar_duckParser.List_expresionContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_list_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_expresion" ):
                listener.enterList_expresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_expresion" ):
                listener.exitList_expresion(self)




    def list_expresion(self):

        localctx = Grammar_duckParser.List_expresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_expresion)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.exp_o_string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.exp_o_string()
                self.state = 133
                self.match(Grammar_duckParser.T__6)
                self.state = 134
                self.list_expresion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_o_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(Grammar_duckParser.ExpresionContext,0)


        def CTE_STRING(self):
            return self.getToken(Grammar_duckParser.CTE_STRING, 0)

        def getRuleIndex(self):
            return Grammar_duckParser.RULE_exp_o_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_o_string" ):
                listener.enterExp_o_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_o_string" ):
                listener.exitExp_o_string(self)




    def exp_o_string(self):

        localctx = Grammar_duckParser.Exp_o_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp_o_string)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 24, 30, 31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.expresion()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.match(Grammar_duckParser.CTE_STRING)
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


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(Grammar_duckParser.ExpresionContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = Grammar_duckParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            localctx._ID = self.match(Grammar_duckParser.ID)

            try:
                semantica.addPilaVar((None if localctx._ID is None else localctx._ID.text))
            except ValueError as e:
                print(e)
                sys.exit()

            self.state = 144
            self.match(Grammar_duckParser.T__11)

            semantica.addPilaOp(7) # 7 = "="

            self.state = 146
            self.expresion()
            self.state = 147
            self.match(Grammar_duckParser.T__1)

            op  = semantica.pilaOperadores.pop() # debe ser un 7 "="
            opD = semantica.pilaVariables.pop()  # operando derecho 
            opI = semantica.pilaVariables.pop()  # operando izquierdo
            TD  = semantica.pilaTipos.pop()      # tipo del operando derecho
            TI  = semantica.pilaTipos.pop()      # tipo del operando izquierdo
            try:
                semantica.addCuadruplo(op,opI,opD,TI,TD)
            except MemoryError() as e:
                print(e)
                sys.exit()
            except ValueError as e2:
                print(e)
                sys.exit()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(Grammar_duckParser.BodyContext,0)


        def expresion(self):
            return self.getTypedRuleContext(Grammar_duckParser.ExpresionContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)




    def cycle(self):

        localctx = Grammar_duckParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(Grammar_duckParser.T__12)
            self.state = 151
            self.body()
            self.state = 152
            self.match(Grammar_duckParser.T__13)
            self.state = 153
            self.expresion()
            self.state = 154
            self.match(Grammar_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(Grammar_duckParser.ExpresionContext,0)


        def body(self):
            return self.getTypedRuleContext(Grammar_duckParser.BodyContext,0)


        def else_(self):
            return self.getTypedRuleContext(Grammar_duckParser.ElseContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = Grammar_duckParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(Grammar_duckParser.T__14)
            self.state = 157
            self.expresion()
            self.state = 158
            self.body()
            self.state = 159
            self.else_()
            self.state = 160
            self.match(Grammar_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(Grammar_duckParser.BodyContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)




    def else_(self):

        localctx = Grammar_duckParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 162
                self.match(Grammar_duckParser.T__15)
                self.state = 163
                self.body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(Grammar_duckParser.ExpContext,0)


        def comparar(self):
            return self.getTypedRuleContext(Grammar_duckParser.CompararContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = Grammar_duckParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.exp()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0):
                self.state = 167
                self.comparar()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompararContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparacion(self):
            return self.getTypedRuleContext(Grammar_duckParser.ComparacionContext,0)


        def exp(self):
            return self.getTypedRuleContext(Grammar_duckParser.ExpContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_comparar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparar" ):
                listener.enterComparar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparar" ):
                listener.exitComparar(self)




    def comparar(self):

        localctx = Grammar_duckParser.CompararContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_comparar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.comparacion()
            self.state = 171
            self.exp()

            # terminar la comparacion
            op  = semantica.pilaOperadores.pop() # debe ser un 4,5 o 6
            opD = semantica.pilaVariables.pop()
            opI = semantica.pilaVariables.pop()
            TD  = semantica.pilaTipos.pop()
            TI  = semantica.pilaTipos.pop()
            try:
                semantica.addCuadruplo(op,opI,opD,TI,TD)
            except MemoryError() as e:
                print(e)
                sys.exit()
            except ValueError as e2:
                print(e)
                sys.exit()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_comparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)




    def comparacion(self):

        localctx = Grammar_duckParser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comparacion)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(Grammar_duckParser.T__16)
                semantica.addPilaOp(4)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(Grammar_duckParser.T__17)
                semantica.addPilaOp(5)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
                self.match(Grammar_duckParser.T__18)
                semantica.addPilaOp(6)
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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_duckParser.TerminoContext)
            else:
                return self.getTypedRuleContext(Grammar_duckParser.TerminoContext,i)


        def sum_rest(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_duckParser.Sum_restContext)
            else:
                return self.getTypedRuleContext(Grammar_duckParser.Sum_restContext,i)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = Grammar_duckParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.termino()

            if semantica.pilaOperadores[-1] == 0 or semantica.pilaOperadores[-1] == 1:
                op = semantica.pilaOperadores.pop()
                opD = semantica.pilaVariables.pop()
                opI = semantica.pilaVariables.pop()
                TD = semantica.pilaTipos.pop()
                TI = semantica.pilaTipos.pop()
                try:
                    semantica.addCuadruplo(op,opI,opD,TI,TD)
                except MemoryError() as e:
                    print(e)
                    sys.exit()
                except VelueError() as e2:
                    print(e2)
                    sys.exit()

            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 184
                self.sum_rest()
                self.state = 185
                self.termino()

                if semantica.pilaOperadores[-1] == 0 or semantica.pilaOperadores[-1] == 1:
                    op = semantica.pilaOperadores.pop()
                    opD = semantica.pilaVariables.pop()
                    opI = semantica.pilaVariables.pop()
                    TD = semantica.pilaTipos.pop()
                    TI = semantica.pilaTipos.pop()
                    try:
                        semantica.addCuadruplo(op,opI,opD,TI,TD)
                    except MemoryError() as e:
                        print(e)
                        sys.exit()
                    except VelueError() as e2:
                        print(e2)
                        sys.exit()

                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sum_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_sum_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum_rest" ):
                listener.enterSum_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum_rest" ):
                listener.exitSum_rest(self)




    def sum_rest(self):

        localctx = Grammar_duckParser.Sum_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_sum_rest)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(Grammar_duckParser.T__19)
                semantica.addPilaOp(0)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.match(Grammar_duckParser.T__20)
                semantica.addPilaOp(1)
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


    class XContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_duckParser.FactorContext)
            else:
                return self.getTypedRuleContext(Grammar_duckParser.FactorContext,i)


        def mult_div(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_duckParser.Mult_divContext)
            else:
                return self.getTypedRuleContext(Grammar_duckParser.Mult_divContext,i)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_x

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterX" ):
                listener.enterX(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitX" ):
                listener.exitX(self)




    def x(self):

        localctx = Grammar_duckParser.XContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_x)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.factor()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 200
                self.mult_div()
                self.state = 201
                self.factor()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_duckParser.FactorContext)
            else:
                return self.getTypedRuleContext(Grammar_duckParser.FactorContext,i)


        def mult_div(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Grammar_duckParser.Mult_divContext)
            else:
                return self.getTypedRuleContext(Grammar_duckParser.Mult_divContext,i)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = Grammar_duckParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.factor()

            if (semantica.pilaOperadores[-1] == 2) or (semantica.pilaOperadores[-1] == 3):
                op = semantica.pilaOperadores.pop()
                opD = semantica.pilaVariables.pop()
                opI = semantica.pilaVariables.pop()
                TD  = semantica.pilaTipos.pop()
                TI  = semantica.pilaTipos.pop()
                try:
                    semantica.addCuadruplo(op,opI,opD,TI,TD)
                except MemoryError() as e:
                    print(e)
                    sys.exit()
                except ValueError as e2:
                    print(e)
                    sys.exit()

            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 210
                self.mult_div()
                self.state = 211
                self.factor()

                if (semantica.pilaOperadores[-1] == 2) or (semantica.pilaOperadores[-1] == 3):
                    op = semantica.pilaOperadores.pop()
                    opD = semantica.pilaVariables.pop()
                    opI = semantica.pilaVariables.pop()
                    TD  = semantica.pilaTipos.pop()
                    TI  = semantica.pilaTipos.pop()
                    try:
                        semantica.addCuadruplo(op,opI,opD,TI,TD)
                    except MemoryError() as e:
                        print(e)
                        sys.exit()
                    except ValueError as e2:
                        print(e)
                        sys.exit()

                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mult_divContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_mult_div

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult_div" ):
                listener.enterMult_div(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult_div" ):
                listener.exitMult_div(self)




    def mult_div(self):

        localctx = Grammar_duckParser.Mult_divContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_mult_div)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(Grammar_duckParser.T__21)
                semantica.addPilaOp(2);
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(Grammar_duckParser.T__22)
                semantica.addPilaOp(3)
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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(Grammar_duckParser.ExpresionContext,0)


        def positivo_negativo(self):
            return self.getTypedRuleContext(Grammar_duckParser.Positivo_negativoContext,0)


        def id_cte(self):
            return self.getTypedRuleContext(Grammar_duckParser.Id_cteContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = Grammar_duckParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_factor)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(Grammar_duckParser.T__23)

                semantica.addPilaOp(-1) # meter barrera

                self.state = 227
                self.expresion()
                self.state = 228
                self.match(Grammar_duckParser.T__10)

                semantica.pilaOperadores.pop() # sacar barrera

                pass
            elif token in [20, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.positivo_negativo()
                self.state = 232
                self.id_cte()

                op  = semantica.pilaOperadores.pop() # tiene que ser un *
                opD = semantica.pilaVariables.pop() # variable o cte
                opI = semantica.pilaVariables.pop() # -1
                TD  = semantica.pilaTipos.pop()
                TI  = semantica.pilaTipos.pop()
                try:
                    semantica.addCuadruplo(op,opI,opD,TI,TD) # *, -1, var, temp = -var
                except MemoryError() as e:
                    print(e)
                    sys.exit()
                except ValueError as e2:
                    print(e)
                    sys.exit()

                pass
            elif token in [30, 31, 32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.id_cte()
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


    class Positivo_negativoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_positivo_negativo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositivo_negativo" ):
                listener.enterPositivo_negativo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositivo_negativo" ):
                listener.exitPositivo_negativo(self)




    def positivo_negativo(self):

        localctx = Grammar_duckParser.Positivo_negativoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_positivo_negativo)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(Grammar_duckParser.T__19)
                #semantica.convertirMenos = False
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(Grammar_duckParser.T__20)

                #semantica.convertirMenos = True
                semantica.addCTE(-1,"int") # agregamos -1 si no existe
                semantica.addPilaOp(2) # agregamos *
                semantica.addPilaVar(-1) # agregar -1 a pila de variables

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


    class Id_cteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(Grammar_duckParser.CteContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_id_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_cte" ):
                listener.enterId_cte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_cte" ):
                listener.exitId_cte(self)




    def id_cte(self):

        localctx = Grammar_duckParser.Id_cteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_id_cte)
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                localctx._ID = self.match(Grammar_duckParser.ID)

                try:
                    semantica.addPilaVar((None if localctx._ID is None else localctx._ID.text))
                except ValueError as e:
                    print(e)
                    sys.exit()

                pass
            elif token in [31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.cte()
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


    class CteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._CTE_INT = None # Token
            self._CTE_FLOAT = None # Token

        def CTE_INT(self):
            return self.getToken(Grammar_duckParser.CTE_INT, 0)

        def CTE_FLOAT(self):
            return self.getToken(Grammar_duckParser.CTE_FLOAT, 0)

        def getRuleIndex(self):
            return Grammar_duckParser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)




    def cte(self):

        localctx = Grammar_duckParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_cte)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                localctx._CTE_INT = self.match(Grammar_duckParser.CTE_INT)

                semantica.addCTE((None if localctx._CTE_INT is None else localctx._CTE_INT.text), 'int')
                try:
                    semantica.addPilaVar((None if localctx._CTE_INT is None else localctx._CTE_INT.text))
                except ValueError as e:
                    print(e)
                    sys.exit()

                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                localctx._CTE_FLOAT = self.match(Grammar_duckParser.CTE_FLOAT)

                semantica.addCTE((None if localctx._CTE_FLOAT is None else localctx._CTE_FLOAT.text), 'float')
                try:
                    semantica.addPilaVar((None if localctx._CTE_FLOAT is None else localctx._CTE_FLOAT.text))
                except ValueError as e:
                    print(e)
                    sys.exit()

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


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def params(self):
            return self.getTypedRuleContext(Grammar_duckParser.ParamsContext,0)


        def var_no_var(self):
            return self.getTypedRuleContext(Grammar_duckParser.Var_no_varContext,0)


        def body(self):
            return self.getTypedRuleContext(Grammar_duckParser.BodyContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)




    def funcs(self):

        localctx = Grammar_duckParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_funcs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(Grammar_duckParser.T__24)
            semantica.currType = 'void'
            self.state = 257
            localctx._ID = self.match(Grammar_duckParser.ID)
            try: 
                semantica.addFunc((None if localctx._ID is None else localctx._ID.text), semantica.currType) 
                semantica.currFunc = (None if localctx._ID is None else localctx._ID.text)
            except ValueError as e: 
                print(e)
                sys.exit()

            self.state = 259
            self.match(Grammar_duckParser.T__23)
            self.state = 260
            self.params()
            self.state = 261
            self.match(Grammar_duckParser.T__10)
            self.state = 262
            self.match(Grammar_duckParser.T__25)
            self.state = 263
            self.var_no_var()
            self.state = 264
            self.body()
            self.state = 265
            self.match(Grammar_duckParser.T__26)
            self.state = 266
            self.match(Grammar_duckParser.T__1)
            semantica.delDV(semantica.currFunc)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_params(self):
            return self.getTypedRuleContext(Grammar_duckParser.List_paramsContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = Grammar_duckParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 269
                self.list_params()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._TYPE = None # Token

        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def TYPE(self):
            return self.getToken(Grammar_duckParser.TYPE, 0)

        def list_params(self):
            return self.getTypedRuleContext(Grammar_duckParser.List_paramsContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_list_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_params" ):
                listener.enterList_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_params" ):
                listener.exitList_params(self)




    def list_params(self):

        localctx = Grammar_duckParser.List_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_list_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            localctx._ID = self.match(Grammar_duckParser.ID)
            semantica.currID = (None if localctx._ID is None else localctx._ID.text)
            self.state = 274
            self.match(Grammar_duckParser.T__5)
            self.state = 275
            localctx._TYPE = self.match(Grammar_duckParser.TYPE)

            try: 
                semantica.addVar(semantica.currID, (None if localctx._TYPE is None else localctx._TYPE.text), semantica.currFunc) 
            except ValueError as e: 
                print(e)
                sys.exit()

            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 278
                self.match(Grammar_duckParser.T__6)
                self.state = 279
                self.list_params()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_no_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self):
            return self.getTypedRuleContext(Grammar_duckParser.VarsContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_var_no_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_no_var" ):
                listener.enterVar_no_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_no_var" ):
                listener.exitVar_no_var(self)




    def var_no_var(self):

        localctx = Grammar_duckParser.Var_no_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_var_no_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.vars_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def f_list_expresion(self):
            return self.getTypedRuleContext(Grammar_duckParser.F_list_expresionContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_f_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call" ):
                listener.enterF_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call" ):
                listener.exitF_call(self)




    def f_call(self):

        localctx = Grammar_duckParser.F_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_f_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(Grammar_duckParser.ID)
            self.state = 285
            self.match(Grammar_duckParser.T__23)
            self.state = 286
            self.f_list_expresion()
            self.state = 287
            self.match(Grammar_duckParser.T__10)
            self.state = 288
            self.match(Grammar_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_list_expresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(Grammar_duckParser.ExpresionContext,0)


        def f_more_expresion(self):
            return self.getTypedRuleContext(Grammar_duckParser.F_more_expresionContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_f_list_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_list_expresion" ):
                listener.enterF_list_expresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_list_expresion" ):
                listener.exitF_list_expresion(self)




    def f_list_expresion(self):

        localctx = Grammar_duckParser.F_list_expresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_f_list_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7536115712) != 0):
                self.state = 290
                self.expresion()
                self.state = 291
                self.f_more_expresion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_more_expresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(Grammar_duckParser.ExpresionContext,0)


        def f_more_expresion(self):
            return self.getTypedRuleContext(Grammar_duckParser.F_more_expresionContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_f_more_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_more_expresion" ):
                listener.enterF_more_expresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_more_expresion" ):
                listener.exitF_more_expresion(self)




    def f_more_expresion(self):

        localctx = Grammar_duckParser.F_more_expresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_f_more_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 295
                self.match(Grammar_duckParser.T__6)
                self.state = 296
                self.expresion()
                self.state = 297
                self.f_more_expresion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





