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
        4,1,33,299,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,3,
        1,84,8,1,1,2,1,2,3,2,88,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,4,3,97,8,
        3,11,3,12,3,98,1,4,1,4,1,4,1,4,3,4,105,8,4,1,5,1,5,1,5,1,5,1,6,5,
        6,112,8,6,10,6,12,6,115,9,6,1,7,1,7,1,7,1,7,1,7,3,7,122,8,7,1,8,
        1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,136,8,9,1,10,1,10,
        1,10,3,10,141,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,3,14,174,8,14,1,15,
        1,15,3,15,178,8,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,17,3,17,190,8,17,1,18,1,18,1,18,1,18,1,18,1,18,5,18,198,8,18,10,
        18,12,18,201,9,18,1,19,1,19,1,19,1,19,3,19,207,8,19,1,20,1,20,1,
        20,1,20,1,20,1,20,5,20,215,8,20,10,20,12,20,218,9,20,1,21,1,21,1,
        21,1,21,3,21,224,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,3,22,237,8,22,1,23,1,23,1,23,3,23,242,8,23,1,24,1,24,
        1,24,3,24,247,8,24,1,25,1,25,1,25,1,25,3,25,253,8,25,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,3,
        27,270,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,280,8,28,
        1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,3,30,291,8,30,1,31,
        1,31,1,31,1,31,3,31,297,8,31,1,31,0,0,32,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        0,0,294,0,64,1,0,0,0,2,83,1,0,0,0,4,87,1,0,0,0,6,96,1,0,0,0,8,100,
        1,0,0,0,10,106,1,0,0,0,12,113,1,0,0,0,14,121,1,0,0,0,16,123,1,0,
        0,0,18,135,1,0,0,0,20,140,1,0,0,0,22,142,1,0,0,0,24,150,1,0,0,0,
        26,160,1,0,0,0,28,173,1,0,0,0,30,175,1,0,0,0,32,179,1,0,0,0,34,189,
        1,0,0,0,36,191,1,0,0,0,38,206,1,0,0,0,40,208,1,0,0,0,42,223,1,0,
        0,0,44,236,1,0,0,0,46,241,1,0,0,0,48,246,1,0,0,0,50,252,1,0,0,0,
        52,254,1,0,0,0,54,269,1,0,0,0,56,271,1,0,0,0,58,281,1,0,0,0,60,290,
        1,0,0,0,62,296,1,0,0,0,64,65,5,1,0,0,65,66,6,0,-1,0,66,67,6,0,-1,
        0,67,68,5,30,0,0,68,69,6,0,-1,0,69,70,5,2,0,0,70,71,3,4,2,0,71,72,
        3,2,1,0,72,73,5,3,0,0,73,74,3,10,5,0,74,75,5,4,0,0,75,76,5,2,0,0,
        76,77,5,0,0,1,77,78,6,0,-1,0,78,79,6,0,-1,0,79,1,1,0,0,0,80,81,3,
        52,26,0,81,82,3,2,1,0,82,84,1,0,0,0,83,80,1,0,0,0,83,84,1,0,0,0,
        84,3,1,0,0,0,85,86,5,5,0,0,86,88,3,6,3,0,87,85,1,0,0,0,87,88,1,0,
        0,0,88,5,1,0,0,0,89,90,6,3,-1,0,90,91,3,8,4,0,91,92,5,6,0,0,92,93,
        5,29,0,0,93,94,6,3,-1,0,94,95,5,2,0,0,95,97,1,0,0,0,96,89,1,0,0,
        0,97,98,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,7,1,0,0,0,100,101,
        5,30,0,0,101,104,6,4,-1,0,102,103,5,7,0,0,103,105,3,8,4,0,104,102,
        1,0,0,0,104,105,1,0,0,0,105,9,1,0,0,0,106,107,5,8,0,0,107,108,3,
        12,6,0,108,109,5,9,0,0,109,11,1,0,0,0,110,112,3,14,7,0,111,110,1,
        0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,13,1,0,
        0,0,115,113,1,0,0,0,116,122,3,22,11,0,117,122,3,26,13,0,118,122,
        3,24,12,0,119,122,3,58,29,0,120,122,3,16,8,0,121,116,1,0,0,0,121,
        117,1,0,0,0,121,118,1,0,0,0,121,119,1,0,0,0,121,120,1,0,0,0,122,
        15,1,0,0,0,123,124,5,10,0,0,124,125,3,18,9,0,125,126,5,11,0,0,126,
        127,5,2,0,0,127,128,6,8,-1,0,128,17,1,0,0,0,129,136,3,20,10,0,130,
        131,3,20,10,0,131,132,5,7,0,0,132,133,6,9,-1,0,133,134,3,18,9,0,
        134,136,1,0,0,0,135,129,1,0,0,0,135,130,1,0,0,0,136,19,1,0,0,0,137,
        141,3,30,15,0,138,139,5,33,0,0,139,141,6,10,-1,0,140,137,1,0,0,0,
        140,138,1,0,0,0,141,21,1,0,0,0,142,143,5,30,0,0,143,144,6,11,-1,
        0,144,145,5,12,0,0,145,146,6,11,-1,0,146,147,3,30,15,0,147,148,5,
        2,0,0,148,149,6,11,-1,0,149,23,1,0,0,0,150,151,5,13,0,0,151,152,
        6,12,-1,0,152,153,3,10,5,0,153,154,5,14,0,0,154,155,5,15,0,0,155,
        156,3,30,15,0,156,157,5,11,0,0,157,158,5,2,0,0,158,159,6,12,-1,0,
        159,25,1,0,0,0,160,161,5,16,0,0,161,162,5,15,0,0,162,163,3,30,15,
        0,163,164,5,11,0,0,164,165,6,13,-1,0,165,166,3,10,5,0,166,167,3,
        28,14,0,167,168,5,2,0,0,168,169,6,13,-1,0,169,27,1,0,0,0,170,171,
        5,17,0,0,171,172,6,14,-1,0,172,174,3,10,5,0,173,170,1,0,0,0,173,
        174,1,0,0,0,174,29,1,0,0,0,175,177,3,36,18,0,176,178,3,32,16,0,177,
        176,1,0,0,0,177,178,1,0,0,0,178,31,1,0,0,0,179,180,3,34,17,0,180,
        181,3,36,18,0,181,182,6,16,-1,0,182,33,1,0,0,0,183,184,5,18,0,0,
        184,190,6,17,-1,0,185,186,5,19,0,0,186,190,6,17,-1,0,187,188,5,20,
        0,0,188,190,6,17,-1,0,189,183,1,0,0,0,189,185,1,0,0,0,189,187,1,
        0,0,0,190,35,1,0,0,0,191,192,3,40,20,0,192,199,6,18,-1,0,193,194,
        3,38,19,0,194,195,3,40,20,0,195,196,6,18,-1,0,196,198,1,0,0,0,197,
        193,1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,
        37,1,0,0,0,201,199,1,0,0,0,202,203,5,21,0,0,203,207,6,19,-1,0,204,
        205,5,22,0,0,205,207,6,19,-1,0,206,202,1,0,0,0,206,204,1,0,0,0,207,
        39,1,0,0,0,208,209,3,44,22,0,209,216,6,20,-1,0,210,211,3,42,21,0,
        211,212,3,44,22,0,212,213,6,20,-1,0,213,215,1,0,0,0,214,210,1,0,
        0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,41,1,0,0,
        0,218,216,1,0,0,0,219,220,5,23,0,0,220,224,6,21,-1,0,221,222,5,24,
        0,0,222,224,6,21,-1,0,223,219,1,0,0,0,223,221,1,0,0,0,224,43,1,0,
        0,0,225,226,5,15,0,0,226,227,6,22,-1,0,227,228,3,30,15,0,228,229,
        5,11,0,0,229,230,6,22,-1,0,230,237,1,0,0,0,231,232,3,46,23,0,232,
        233,3,48,24,0,233,234,6,22,-1,0,234,237,1,0,0,0,235,237,3,48,24,
        0,236,225,1,0,0,0,236,231,1,0,0,0,236,235,1,0,0,0,237,45,1,0,0,0,
        238,242,5,21,0,0,239,240,5,22,0,0,240,242,6,23,-1,0,241,238,1,0,
        0,0,241,239,1,0,0,0,242,47,1,0,0,0,243,244,5,30,0,0,244,247,6,24,
        -1,0,245,247,3,50,25,0,246,243,1,0,0,0,246,245,1,0,0,0,247,49,1,
        0,0,0,248,249,5,31,0,0,249,253,6,25,-1,0,250,251,5,32,0,0,251,253,
        6,25,-1,0,252,248,1,0,0,0,252,250,1,0,0,0,253,51,1,0,0,0,254,255,
        5,25,0,0,255,256,6,26,-1,0,256,257,5,30,0,0,257,258,6,26,-1,0,258,
        259,5,15,0,0,259,260,3,54,27,0,260,261,5,11,0,0,261,262,5,26,0,0,
        262,263,3,4,2,0,263,264,3,10,5,0,264,265,5,27,0,0,265,266,5,2,0,
        0,266,267,6,26,-1,0,267,53,1,0,0,0,268,270,3,56,28,0,269,268,1,0,
        0,0,269,270,1,0,0,0,270,55,1,0,0,0,271,272,5,30,0,0,272,273,6,28,
        -1,0,273,274,5,6,0,0,274,275,5,29,0,0,275,276,6,28,-1,0,276,279,
        1,0,0,0,277,278,5,7,0,0,278,280,3,56,28,0,279,277,1,0,0,0,279,280,
        1,0,0,0,280,57,1,0,0,0,281,282,5,30,0,0,282,283,5,15,0,0,283,284,
        3,60,30,0,284,285,5,11,0,0,285,286,5,2,0,0,286,59,1,0,0,0,287,288,
        3,30,15,0,288,289,3,62,31,0,289,291,1,0,0,0,290,287,1,0,0,0,290,
        291,1,0,0,0,291,61,1,0,0,0,292,293,5,7,0,0,293,294,3,30,15,0,294,
        295,3,62,31,0,295,297,1,0,0,0,296,292,1,0,0,0,296,297,1,0,0,0,297,
        63,1,0,0,0,23,83,87,98,104,113,121,135,140,173,177,189,199,206,216,
        223,236,241,246,252,269,279,290,296
    ]

class Grammar_duckParser ( Parser ):

    grammarFileName = "Grammar_duck.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'main'", "'end'", 
                     "'var'", "':'", "','", "'{'", "'}'", "'print('", "')'", 
                     "'='", "'do'", "'while'", "'('", "'if'", "'else'", 
                     "'<'", "'>'", "'!='", "'+'", "'-'", "'*'", "'/'", "'void'", 
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
    RULE_termino = 20
    RULE_mult_div = 21
    RULE_factor = 22
    RULE_positivo_negativo = 23
    RULE_id_cte = 24
    RULE_cte = 25
    RULE_funcs = 26
    RULE_params = 27
    RULE_list_params = 28
    RULE_f_call = 29
    RULE_f_list_expresion = 30
    RULE_f_more_expresion = 31

    ruleNames =  [ "prog", "a_funcs", "vars", "more_vars", "list_id", "body", 
                   "list_statement", "statement", "print", "list_expresion", 
                   "exp_o_string", "assign", "cycle", "condition", "else", 
                   "expresion", "comparar", "comparacion", "exp", "sum_rest", 
                   "termino", "mult_div", "factor", "positivo_negativo", 
                   "id_cte", "cte", "funcs", "params", "list_params", "f_call", 
                   "f_list_expresion", "f_more_expresion" ]

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
            self.state = 64
            self.match(Grammar_duckParser.T__0)
            global semantica

            semantica.currType = "program"

            self.state = 67
            localctx._ID = self.match(Grammar_duckParser.ID)
            try:
                semantica.addFunc((None if localctx._ID is None else localctx._ID.text), semantica.currType) 
                semantica.currFunc = (None if localctx._ID is None else localctx._ID.text)
                semantica.progName = (None if localctx._ID is None else localctx._ID.text)
            except ValueError as e: 
                print(e)
                sys.exit()
            self.state = 69
            self.match(Grammar_duckParser.T__1)
            self.state = 70
            self.vars_()
            self.state = 71
            self.a_funcs()
            self.state = 72
            self.match(Grammar_duckParser.T__2)
            self.state = 73
            self.body()
            self.state = 74
            self.match(Grammar_duckParser.T__3)
            self.state = 75
            self.match(Grammar_duckParser.T__1)
            self.state = 76
            self.match(Grammar_duckParser.EOF)
            semantica.addCuadruplo(12)
            del semantica
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
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 80
                self.funcs()
                self.state = 81
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
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 85
                self.match(Grammar_duckParser.T__4)
                self.state = 86
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
            self.state = 96 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                semantica.tempIDS.clear()
                self.state = 90
                self.list_id()
                self.state = 91
                self.match(Grammar_duckParser.T__5)
                self.state = 92
                localctx._TYPE = self.match(Grammar_duckParser.TYPE)

                try:
                    semantica.addListVar(semantica.tempIDS,(None if localctx._TYPE is None else localctx._TYPE.text),semantica.currFunc)
                except ValueError as e:
                    print(e)
                    sys.exit()

                self.state = 94
                self.match(Grammar_duckParser.T__1)
                self.state = 98 
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
            self.state = 100
            localctx._ID = self.match(Grammar_duckParser.ID)

            semantica.addVarTempList((None if localctx._ID is None else localctx._ID.text))

            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 102
                self.match(Grammar_duckParser.T__6)
                self.state = 103
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
            self.state = 106
            self.match(Grammar_duckParser.T__7)
            self.state = 107
            self.list_statement()
            self.state = 108
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
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073816576) != 0):
                self.state = 110
                self.statement()
                self.state = 115
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
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 119
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 120
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
            self.state = 123
            self.match(Grammar_duckParser.T__9)
            self.state = 124
            self.list_expresion()
            self.state = 125
            self.match(Grammar_duckParser.T__10)
            self.state = 126
            self.match(Grammar_duckParser.T__1)

            semantica.pilaTipos.pop()
            temp = semantica.pilaVariables.pop()
            op = 11
            try:
                semantica.addCuadruplo(op,temp)
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
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.exp_o_string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.exp_o_string()
                self.state = 131
                self.match(Grammar_duckParser.T__6)

                semantica.pilaTipos.pop()
                temp = semantica.pilaVariables.pop()
                op = 11
                try:
                    semantica.addCuadruplo(op,temp)
                except MemoryError() as e:
                    print(e)
                    sys.exit()
                except ValueError as e2:
                    print(e)
                    sys.exit()

                self.state = 133
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
            self._CTE_STRING = None # Token

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
            if token in [15, 21, 22, 30, 31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.expresion()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                localctx._CTE_STRING = self.match(Grammar_duckParser.CTE_STRING)

                cteT = (None if localctx._CTE_STRING is None else localctx._CTE_STRING.text)
                cteT = cteT[1:-1] # quitamos comillas
                try:
                    semantica.addCTE(cteT,"string")
                except ValueError as e:
                    print(e)
                    sys.exit()
                try:
                    semantica.addPilaVar(cteT,cte=True,tipo=2)
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

            indice = semantica.currCuadruplo
            semantica.pilaSaltos.append(indice)

            self.state = 152
            self.body()
            self.state = 153
            self.match(Grammar_duckParser.T__13)
            self.state = 154
            self.match(Grammar_duckParser.T__14)
            self.state = 155
            self.expresion()
            self.state = 156
            self.match(Grammar_duckParser.T__10)
            self.state = 157
            self.match(Grammar_duckParser.T__1)

            indice      = semantica.pilaSaltos.pop() # a donde tenemos que saltar
            comparacion = semantica.pilaVariables.pop() # la exprecion que estamos comparando
            tipo = semantica.pilaTipos.pop() # sacamos el tipo de la pila de tipos
            op = 10 # goToTrue
            try:
                semantica.addCuadruplo(op,comparacion,indice)
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
            self.state = 160
            self.match(Grammar_duckParser.T__15)
            self.state = 161
            self.match(Grammar_duckParser.T__14)
            self.state = 162
            self.expresion()
            self.state = 163
            self.match(Grammar_duckParser.T__10)

            indice = semantica.currCuadruplo
            semantica.pilaSaltos.append(indice)
            comparacion = semantica.pilaVariables.pop() # la exprecion que estamos comparando
            tipo = semantica.pilaTipos.pop() # sacamos el tipo de la pila de tipos
            op = 9 # GoToFalse
            try:
                semantica.addCuadruplo(op,comparacion,indice)
            except MemoryError() as e:
                print(e)
                sys.exit()
            except ValueError as e2:
                print(e)
                sys.exit()

            self.state = 165
            self.body()
            self.state = 166
            self.else_()
            self.state = 167
            self.match(Grammar_duckParser.T__1)

            indice = semantica.pilaSaltos.pop() # a donde tenemos que regrear para editar
            semantica.setGoTo(indice, semantica.currCuadruplo)

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
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 170
                self.match(Grammar_duckParser.T__16)

                temp = semantica.pilaSaltos.pop() # indice del if
                indice = semantica.currCuadruplo # cuadruplo actual
                semantica.pilaSaltos.append(indice)
                op = 8 # GoTo
                try:
                    semantica.addCuadruplo(op)
                except MemoryError() as e:
                    print(e)
                    sys.exit()
                except ValueError as e2:
                    print(e)
                    sys.exit()
                indice = semantica.currCuadruplo # indice cambio ya que agregamos el GoTo
                semantica.setGoTo(temp,indice) # ponemos a donde debe saltar el if si es falso

                self.state = 172
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
            self.state = 175
            self.exp()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0):
                self.state = 176
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
            self.state = 179
            self.comparacion()
            self.state = 180
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
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(Grammar_duckParser.T__17)
                semantica.addPilaOp(4)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(Grammar_duckParser.T__18)
                semantica.addPilaOp(5)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.match(Grammar_duckParser.T__19)
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
            self.state = 191
            self.termino()

            if semantica.pilaOperadores : # revisar que no este vacio
                if (semantica.pilaOperadores[-1] == 0) or (semantica.pilaOperadores[-1] == 1):
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

            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 193
                self.sum_rest()
                self.state = 194
                self.termino()

                if semantica.pilaOperadores : # revisar que no este vacio
                    if (semantica.pilaOperadores[-1] == 0) or (semantica.pilaOperadores[-1]) == 1:
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

                self.state = 201
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
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(Grammar_duckParser.T__20)
                semantica.addPilaOp(0)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(Grammar_duckParser.T__21)
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
        self.enterRule(localctx, 40, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.factor()

            if semantica.pilaOperadores : # revisar que no este vacio
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
            while _la==23 or _la==24:
                self.state = 210
                self.mult_div()
                self.state = 211
                self.factor()

                if semantica.pilaOperadores : # revisar que no este vacio
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
        self.enterRule(localctx, 42, self.RULE_mult_div)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(Grammar_duckParser.T__22)
                semantica.addPilaOp(2);
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(Grammar_duckParser.T__23)
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
        self.enterRule(localctx, 44, self.RULE_factor)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(Grammar_duckParser.T__14)

                semantica.addPilaOp(-1) # meter barrera

                self.state = 227
                self.expresion()
                self.state = 228
                self.match(Grammar_duckParser.T__10)

                semantica.pilaOperadores.pop() # sacar barrera

                pass
            elif token in [21, 22]:
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
        self.enterRule(localctx, 46, self.RULE_positivo_negativo)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(Grammar_duckParser.T__20)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(Grammar_duckParser.T__21)

                try:
                    semantica.addCTE(-1,"int") # agregamos -1 si no existe
                except ValueError as e:
                    print(e)
                    sys.exit()
                semantica.addPilaOp(2) # agregamos *
                semantica.addPilaVar(-1, cte=True, tipo=1) # agregar -1 a pila de variables

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
        self.enterRule(localctx, 48, self.RULE_id_cte)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                localctx._ID = self.match(Grammar_duckParser.ID)

                try:
                    semantica.addPilaVar((None if localctx._ID is None else localctx._ID.text))
                except ValueError as e:
                    print(e)
                    sys.exit()

                pass
            elif token in [31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
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
        self.enterRule(localctx, 50, self.RULE_cte)
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                localctx._CTE_INT = self.match(Grammar_duckParser.CTE_INT)

                try:
                    semantica.addCTE((None if localctx._CTE_INT is None else localctx._CTE_INT.text), 'int')
                except ValueError as e:
                    print(e)
                    sys.exit()
                try:
                    semantica.addPilaVar((None if localctx._CTE_INT is None else localctx._CTE_INT.text), cte = True, tipo = 1)
                except ValueError as e:
                    print(e)
                    sys.exit()

                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                localctx._CTE_FLOAT = self.match(Grammar_duckParser.CTE_FLOAT)

                try:
                    semantica.addCTE((None if localctx._CTE_FLOAT is None else localctx._CTE_FLOAT.text), 'float')
                except ValueError as e:
                    print(e)
                    sys.exit()
                try:
                    semantica.addPilaVar((None if localctx._CTE_FLOAT is None else localctx._CTE_FLOAT.text), cte = True, tipo = 0)
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


        def vars_(self):
            return self.getTypedRuleContext(Grammar_duckParser.VarsContext,0)


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
        self.enterRule(localctx, 52, self.RULE_funcs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(Grammar_duckParser.T__24)
            semantica.currType = 'void'
            self.state = 256
            localctx._ID = self.match(Grammar_duckParser.ID)
            try: 
                semantica.addFunc((None if localctx._ID is None else localctx._ID.text), semantica.currType) 
                semantica.currFunc = (None if localctx._ID is None else localctx._ID.text)
            except ValueError as e: 
                print(e)
                sys.exit()

            self.state = 258
            self.match(Grammar_duckParser.T__14)
            self.state = 259
            self.params()
            self.state = 260
            self.match(Grammar_duckParser.T__10)
            self.state = 261
            self.match(Grammar_duckParser.T__25)
            self.state = 262
            self.vars_()
            self.state = 263
            self.body()
            self.state = 264
            self.match(Grammar_duckParser.T__26)
            self.state = 265
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
        self.enterRule(localctx, 54, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 268
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
        self.enterRule(localctx, 56, self.RULE_list_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            localctx._ID = self.match(Grammar_duckParser.ID)
            semantica.currID = (None if localctx._ID is None else localctx._ID.text)
            self.state = 273
            self.match(Grammar_duckParser.T__5)
            self.state = 274
            localctx._TYPE = self.match(Grammar_duckParser.TYPE)

            try: 
                semantica.addVar(semantica.currID, (None if localctx._TYPE is None else localctx._TYPE.text), semantica.currFunc) 
            except ValueError as e: 
                print(e)
                sys.exit()

            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 277
                self.match(Grammar_duckParser.T__6)
                self.state = 278
                self.list_params()


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
        self.enterRule(localctx, 58, self.RULE_f_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(Grammar_duckParser.ID)
            self.state = 282
            self.match(Grammar_duckParser.T__14)
            self.state = 283
            self.f_list_expresion()
            self.state = 284
            self.match(Grammar_duckParser.T__10)
            self.state = 285
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
        self.enterRule(localctx, 60, self.RULE_f_list_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7522516992) != 0):
                self.state = 287
                self.expresion()
                self.state = 288
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
        self.enterRule(localctx, 62, self.RULE_f_more_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 292
                self.match(Grammar_duckParser.T__6)
                self.state = 293
                self.expresion()
                self.state = 294
                self.f_more_expresion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





