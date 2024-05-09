# Generated from Grammar_duck.g4 by ANTLR 4.13.1
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
        4,1,34,275,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,1,3,1,88,8,1,1,2,1,2,1,2,3,2,93,8,2,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,
        5,112,8,5,1,6,1,6,1,6,3,6,117,8,6,1,7,1,7,1,8,1,8,1,8,1,8,1,9,5,
        9,126,8,9,10,9,12,9,129,9,9,1,10,1,10,1,10,1,10,1,10,3,10,136,8,
        10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,148,8,
        12,1,13,1,13,3,13,152,8,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,3,17,173,
        8,17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,3,19,184,8,19,
        1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,3,22,195,8,22,1,23,
        1,23,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,26,1,26,3,26,208,8,26,
        1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,220,8,28,
        1,29,1,29,3,29,224,8,29,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,3,32,245,
        8,32,1,33,1,33,1,33,1,33,1,33,1,33,3,33,253,8,33,1,34,3,34,256,8,
        34,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,3,36,267,8,36,1,
        37,1,37,1,37,1,37,3,37,273,8,37,1,37,0,0,38,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,0,4,1,0,8,9,1,0,22,23,1,0,24,25,1,0,32,33,261,
        0,76,1,0,0,0,2,87,1,0,0,0,4,92,1,0,0,0,6,94,1,0,0,0,8,97,1,0,0,0,
        10,111,1,0,0,0,12,116,1,0,0,0,14,118,1,0,0,0,16,120,1,0,0,0,18,127,
        1,0,0,0,20,135,1,0,0,0,22,137,1,0,0,0,24,147,1,0,0,0,26,151,1,0,
        0,0,28,153,1,0,0,0,30,158,1,0,0,0,32,164,1,0,0,0,34,172,1,0,0,0,
        36,174,1,0,0,0,38,183,1,0,0,0,40,185,1,0,0,0,42,187,1,0,0,0,44,194,
        1,0,0,0,46,196,1,0,0,0,48,198,1,0,0,0,50,200,1,0,0,0,52,207,1,0,
        0,0,54,209,1,0,0,0,56,219,1,0,0,0,58,223,1,0,0,0,60,225,1,0,0,0,
        62,227,1,0,0,0,64,244,1,0,0,0,66,252,1,0,0,0,68,255,1,0,0,0,70,257,
        1,0,0,0,72,266,1,0,0,0,74,272,1,0,0,0,76,77,5,1,0,0,77,78,5,31,0,
        0,78,79,5,2,0,0,79,80,3,2,1,0,80,81,3,4,2,0,81,82,5,3,0,0,82,83,
        3,16,8,0,83,84,5,4,0,0,84,85,5,0,0,1,85,1,1,0,0,0,86,88,3,6,3,0,
        87,86,1,0,0,0,87,88,1,0,0,0,88,3,1,0,0,0,89,90,3,62,31,0,90,91,3,
        4,2,0,91,93,1,0,0,0,92,89,1,0,0,0,92,93,1,0,0,0,93,5,1,0,0,0,94,
        95,5,5,0,0,95,96,3,8,4,0,96,7,1,0,0,0,97,98,5,31,0,0,98,99,3,12,
        6,0,99,100,5,6,0,0,100,101,3,14,7,0,101,102,5,2,0,0,102,103,3,10,
        5,0,103,9,1,0,0,0,104,105,5,31,0,0,105,106,3,12,6,0,106,107,5,6,
        0,0,107,108,3,14,7,0,108,109,5,2,0,0,109,110,3,10,5,0,110,112,1,
        0,0,0,111,104,1,0,0,0,111,112,1,0,0,0,112,11,1,0,0,0,113,114,5,7,
        0,0,114,115,5,31,0,0,115,117,3,12,6,0,116,113,1,0,0,0,116,117,1,
        0,0,0,117,13,1,0,0,0,118,119,7,0,0,0,119,15,1,0,0,0,120,121,5,10,
        0,0,121,122,3,18,9,0,122,123,5,11,0,0,123,17,1,0,0,0,124,126,3,20,
        10,0,125,124,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,
        0,0,128,19,1,0,0,0,129,127,1,0,0,0,130,136,3,28,14,0,131,136,3,32,
        16,0,132,136,3,30,15,0,133,136,3,70,35,0,134,136,3,22,11,0,135,130,
        1,0,0,0,135,131,1,0,0,0,135,132,1,0,0,0,135,133,1,0,0,0,135,134,
        1,0,0,0,136,21,1,0,0,0,137,138,5,12,0,0,138,139,3,24,12,0,139,140,
        5,13,0,0,140,141,5,2,0,0,141,23,1,0,0,0,142,148,3,26,13,0,143,144,
        3,26,13,0,144,145,5,7,0,0,145,146,3,24,12,0,146,148,1,0,0,0,147,
        142,1,0,0,0,147,143,1,0,0,0,148,25,1,0,0,0,149,152,3,36,18,0,150,
        152,5,34,0,0,151,149,1,0,0,0,151,150,1,0,0,0,152,27,1,0,0,0,153,
        154,5,31,0,0,154,155,5,14,0,0,155,156,3,36,18,0,156,157,5,2,0,0,
        157,29,1,0,0,0,158,159,5,15,0,0,159,160,3,16,8,0,160,161,5,16,0,
        0,161,162,3,36,18,0,162,163,5,2,0,0,163,31,1,0,0,0,164,165,5,17,
        0,0,165,166,3,36,18,0,166,167,3,16,8,0,167,168,3,34,17,0,168,169,
        5,2,0,0,169,33,1,0,0,0,170,171,5,18,0,0,171,173,3,16,8,0,172,170,
        1,0,0,0,172,173,1,0,0,0,173,35,1,0,0,0,174,175,3,40,20,0,175,176,
        3,38,19,0,176,37,1,0,0,0,177,178,5,19,0,0,178,184,3,40,20,0,179,
        180,5,20,0,0,180,184,3,40,20,0,181,182,5,21,0,0,182,184,3,40,20,
        0,183,177,1,0,0,0,183,179,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,
        0,184,39,1,0,0,0,185,186,3,42,21,0,186,41,1,0,0,0,187,188,3,48,24,
        0,188,189,3,44,22,0,189,43,1,0,0,0,190,191,3,46,23,0,191,192,3,48,
        24,0,192,193,3,44,22,0,193,195,1,0,0,0,194,190,1,0,0,0,194,195,1,
        0,0,0,195,45,1,0,0,0,196,197,7,1,0,0,197,47,1,0,0,0,198,199,3,50,
        25,0,199,49,1,0,0,0,200,201,3,56,28,0,201,202,3,52,26,0,202,51,1,
        0,0,0,203,204,3,54,27,0,204,205,3,56,28,0,205,206,3,52,26,0,206,
        208,1,0,0,0,207,203,1,0,0,0,207,208,1,0,0,0,208,53,1,0,0,0,209,210,
        7,2,0,0,210,55,1,0,0,0,211,212,5,26,0,0,212,213,3,36,18,0,213,214,
        5,13,0,0,214,220,1,0,0,0,215,216,3,46,23,0,216,217,3,58,29,0,217,
        220,1,0,0,0,218,220,3,58,29,0,219,211,1,0,0,0,219,215,1,0,0,0,219,
        218,1,0,0,0,220,57,1,0,0,0,221,224,5,31,0,0,222,224,3,60,30,0,223,
        221,1,0,0,0,223,222,1,0,0,0,224,59,1,0,0,0,225,226,7,3,0,0,226,61,
        1,0,0,0,227,228,5,27,0,0,228,229,5,31,0,0,229,230,5,26,0,0,230,231,
        3,64,32,0,231,232,5,13,0,0,232,233,5,28,0,0,233,234,3,68,34,0,234,
        235,3,16,8,0,235,236,5,29,0,0,236,237,5,2,0,0,237,63,1,0,0,0,238,
        239,5,31,0,0,239,240,5,6,0,0,240,241,3,14,7,0,241,242,1,0,0,0,242,
        243,3,66,33,0,243,245,1,0,0,0,244,238,1,0,0,0,244,245,1,0,0,0,245,
        65,1,0,0,0,246,247,5,7,0,0,247,248,5,31,0,0,248,249,5,6,0,0,249,
        250,3,14,7,0,250,251,3,66,33,0,251,253,1,0,0,0,252,246,1,0,0,0,252,
        253,1,0,0,0,253,67,1,0,0,0,254,256,3,6,3,0,255,254,1,0,0,0,255,256,
        1,0,0,0,256,69,1,0,0,0,257,258,5,31,0,0,258,259,5,26,0,0,259,260,
        3,72,36,0,260,261,5,13,0,0,261,262,5,2,0,0,262,71,1,0,0,0,263,264,
        3,36,18,0,264,265,3,74,37,0,265,267,1,0,0,0,266,263,1,0,0,0,266,
        267,1,0,0,0,267,73,1,0,0,0,268,269,5,7,0,0,269,270,3,36,18,0,270,
        271,3,74,37,0,271,273,1,0,0,0,272,268,1,0,0,0,272,273,1,0,0,0,273,
        75,1,0,0,0,19,87,92,111,116,127,135,147,151,172,183,194,207,219,
        223,244,252,255,266,272
    ]

class Grammar_duckParser ( Parser ):

    grammarFileName = "Grammar_duck.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'main'", "'end'", 
                     "'var'", "':'", "','", "'int'", "'float'", "'{'", "'}'", 
                     "'print('", "')'", "'='", "'do'", "'while'", "'if'", 
                     "'else'", "'<'", "'>'", "'!='", "'+'", "'-'", "'*'", 
                     "'/'", "'('", "'void'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SKIPS", "ID", "CTE_INT", 
                      "CTE_FLOAT", "CTE_STRING" ]

    RULE_prog = 0
    RULE_a_vars = 1
    RULE_a_funcs = 2
    RULE_vars = 3
    RULE_list_vars = 4
    RULE_more_vars = 5
    RULE_list_id = 6
    RULE_type = 7
    RULE_body = 8
    RULE_list_statement = 9
    RULE_statement = 10
    RULE_print = 11
    RULE_list_expresion = 12
    RULE_exp_o_string = 13
    RULE_assign = 14
    RULE_cycle = 15
    RULE_condition = 16
    RULE_else = 17
    RULE_expresion = 18
    RULE_comparar_exp = 19
    RULE_exp = 20
    RULE_list_terminos = 21
    RULE_next_termino = 22
    RULE_sum_rest = 23
    RULE_termino = 24
    RULE_list_factor = 25
    RULE_next_factor = 26
    RULE_mult_div = 27
    RULE_factor = 28
    RULE_id_cte = 29
    RULE_cte = 30
    RULE_funcs = 31
    RULE_list_params = 32
    RULE_more_params = 33
    RULE_var_no_var = 34
    RULE_f_call = 35
    RULE_f_list_expresion = 36
    RULE_f_more_expresion = 37

    ruleNames =  [ "prog", "a_vars", "a_funcs", "vars", "list_vars", "more_vars", 
                   "list_id", "type", "body", "list_statement", "statement", 
                   "print", "list_expresion", "exp_o_string", "assign", 
                   "cycle", "condition", "else", "expresion", "comparar_exp", 
                   "exp", "list_terminos", "next_termino", "sum_rest", "termino", 
                   "list_factor", "next_factor", "mult_div", "factor", "id_cte", 
                   "cte", "funcs", "list_params", "more_params", "var_no_var", 
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
    T__27=28
    T__28=29
    SKIPS=30
    ID=31
    CTE_INT=32
    CTE_FLOAT=33
    CTE_STRING=34

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

        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def a_vars(self):
            return self.getTypedRuleContext(Grammar_duckParser.A_varsContext,0)


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
            self.state = 76
            self.match(Grammar_duckParser.T__0)
            self.state = 77
            self.match(Grammar_duckParser.ID)
            self.state = 78
            self.match(Grammar_duckParser.T__1)
            self.state = 79
            self.a_vars()
            self.state = 80
            self.a_funcs()
            self.state = 81
            self.match(Grammar_duckParser.T__2)
            self.state = 82
            self.body()
            self.state = 83
            self.match(Grammar_duckParser.T__3)
            self.state = 84
            self.match(Grammar_duckParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A_varsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self):
            return self.getTypedRuleContext(Grammar_duckParser.VarsContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_a_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA_vars" ):
                listener.enterA_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA_vars" ):
                listener.exitA_vars(self)




    def a_vars(self):

        localctx = Grammar_duckParser.A_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_a_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 86
                self.vars_()


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
        self.enterRule(localctx, 4, self.RULE_a_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 89
                self.funcs()
                self.state = 90
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

        def list_vars(self):
            return self.getTypedRuleContext(Grammar_duckParser.List_varsContext,0)


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
        self.enterRule(localctx, 6, self.RULE_vars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(Grammar_duckParser.T__4)
            self.state = 95
            self.list_vars()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_varsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def list_id(self):
            return self.getTypedRuleContext(Grammar_duckParser.List_idContext,0)


        def type_(self):
            return self.getTypedRuleContext(Grammar_duckParser.TypeContext,0)


        def more_vars(self):
            return self.getTypedRuleContext(Grammar_duckParser.More_varsContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_list_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_vars" ):
                listener.enterList_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_vars" ):
                listener.exitList_vars(self)




    def list_vars(self):

        localctx = Grammar_duckParser.List_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list_vars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(Grammar_duckParser.ID)
            self.state = 98
            self.list_id()
            self.state = 99
            self.match(Grammar_duckParser.T__5)
            self.state = 100
            self.type_()
            self.state = 101
            self.match(Grammar_duckParser.T__1)
            self.state = 102
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

        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def list_id(self):
            return self.getTypedRuleContext(Grammar_duckParser.List_idContext,0)


        def type_(self):
            return self.getTypedRuleContext(Grammar_duckParser.TypeContext,0)


        def more_vars(self):
            return self.getTypedRuleContext(Grammar_duckParser.More_varsContext,0)


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
        self.enterRule(localctx, 10, self.RULE_more_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 104
                self.match(Grammar_duckParser.ID)
                self.state = 105
                self.list_id()
                self.state = 106
                self.match(Grammar_duckParser.T__5)
                self.state = 107
                self.type_()
                self.state = 108
                self.match(Grammar_duckParser.T__1)
                self.state = 109
                self.more_vars()


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
        self.enterRule(localctx, 12, self.RULE_list_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 113
                self.match(Grammar_duckParser.T__6)
                self.state = 114
                self.match(Grammar_duckParser.ID)
                self.state = 115
                self.list_id()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = Grammar_duckParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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
        self.enterRule(localctx, 16, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(Grammar_duckParser.T__9)
            self.state = 121
            self.list_statement()
            self.state = 122
            self.match(Grammar_duckParser.T__10)
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
        self.enterRule(localctx, 18, self.RULE_list_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2147651584) != 0):
                self.state = 124
                self.statement()
                self.state = 129
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
        self.enterRule(localctx, 20, self.RULE_statement)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 134
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
        self.enterRule(localctx, 22, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(Grammar_duckParser.T__11)
            self.state = 138
            self.list_expresion()
            self.state = 139
            self.match(Grammar_duckParser.T__12)
            self.state = 140
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
        self.enterRule(localctx, 24, self.RULE_list_expresion)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.exp_o_string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.exp_o_string()
                self.state = 144
                self.match(Grammar_duckParser.T__6)
                self.state = 145
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
        self.enterRule(localctx, 26, self.RULE_exp_o_string)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 26, 31, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.expresion()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
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
        self.enterRule(localctx, 28, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(Grammar_duckParser.ID)
            self.state = 154
            self.match(Grammar_duckParser.T__13)
            self.state = 155
            self.expresion()
            self.state = 156
            self.match(Grammar_duckParser.T__1)
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
        self.enterRule(localctx, 30, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(Grammar_duckParser.T__14)
            self.state = 159
            self.body()
            self.state = 160
            self.match(Grammar_duckParser.T__15)
            self.state = 161
            self.expresion()
            self.state = 162
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
        self.enterRule(localctx, 32, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(Grammar_duckParser.T__16)
            self.state = 165
            self.expresion()
            self.state = 166
            self.body()
            self.state = 167
            self.else_()
            self.state = 168
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
        self.enterRule(localctx, 34, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 170
                self.match(Grammar_duckParser.T__17)
                self.state = 171
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


        def comparar_exp(self):
            return self.getTypedRuleContext(Grammar_duckParser.Comparar_expContext,0)


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
        self.enterRule(localctx, 36, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.exp()
            self.state = 175
            self.comparar_exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparar_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(Grammar_duckParser.ExpContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_comparar_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparar_exp" ):
                listener.enterComparar_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparar_exp" ):
                listener.exitComparar_exp(self)




    def comparar_exp(self):

        localctx = Grammar_duckParser.Comparar_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_comparar_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.state = 177
                self.match(Grammar_duckParser.T__18)
                self.state = 178
                self.exp()
                pass
            elif token in [20]:
                self.state = 179
                self.match(Grammar_duckParser.T__19)
                self.state = 180
                self.exp()
                pass
            elif token in [21]:
                self.state = 181
                self.match(Grammar_duckParser.T__20)
                self.state = 182
                self.exp()
                pass
            elif token in [2, 7, 10, 13]:
                pass
            else:
                pass
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

        def list_terminos(self):
            return self.getTypedRuleContext(Grammar_duckParser.List_terminosContext,0)


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
        self.enterRule(localctx, 40, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.list_terminos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_terminosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(Grammar_duckParser.TerminoContext,0)


        def next_termino(self):
            return self.getTypedRuleContext(Grammar_duckParser.Next_terminoContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_list_terminos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_terminos" ):
                listener.enterList_terminos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_terminos" ):
                listener.exitList_terminos(self)




    def list_terminos(self):

        localctx = Grammar_duckParser.List_terminosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_terminos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.termino()
            self.state = 188
            self.next_termino()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_terminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sum_rest(self):
            return self.getTypedRuleContext(Grammar_duckParser.Sum_restContext,0)


        def termino(self):
            return self.getTypedRuleContext(Grammar_duckParser.TerminoContext,0)


        def next_termino(self):
            return self.getTypedRuleContext(Grammar_duckParser.Next_terminoContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_next_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNext_termino" ):
                listener.enterNext_termino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNext_termino" ):
                listener.exitNext_termino(self)




    def next_termino(self):

        localctx = Grammar_duckParser.Next_terminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_next_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22 or _la==23:
                self.state = 190
                self.sum_rest()
                self.state = 191
                self.termino()
                self.state = 192
                self.next_termino()


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
        self.enterRule(localctx, 46, self.RULE_sum_rest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
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


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_factor(self):
            return self.getTypedRuleContext(Grammar_duckParser.List_factorContext,0)


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
        self.enterRule(localctx, 48, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.list_factor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_factorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(Grammar_duckParser.FactorContext,0)


        def next_factor(self):
            return self.getTypedRuleContext(Grammar_duckParser.Next_factorContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_list_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_factor" ):
                listener.enterList_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_factor" ):
                listener.exitList_factor(self)




    def list_factor(self):

        localctx = Grammar_duckParser.List_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_list_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.factor()
            self.state = 201
            self.next_factor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_factorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mult_div(self):
            return self.getTypedRuleContext(Grammar_duckParser.Mult_divContext,0)


        def factor(self):
            return self.getTypedRuleContext(Grammar_duckParser.FactorContext,0)


        def next_factor(self):
            return self.getTypedRuleContext(Grammar_duckParser.Next_factorContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_next_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNext_factor" ):
                listener.enterNext_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNext_factor" ):
                listener.exitNext_factor(self)




    def next_factor(self):

        localctx = Grammar_duckParser.Next_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_next_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24 or _la==25:
                self.state = 203
                self.mult_div()
                self.state = 204
                self.factor()
                self.state = 205
                self.next_factor()


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
        self.enterRule(localctx, 54, self.RULE_mult_div)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(Grammar_duckParser.ExpresionContext,0)


        def sum_rest(self):
            return self.getTypedRuleContext(Grammar_duckParser.Sum_restContext,0)


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
        self.enterRule(localctx, 56, self.RULE_factor)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(Grammar_duckParser.T__25)
                self.state = 212
                self.expresion()
                self.state = 213
                self.match(Grammar_duckParser.T__12)
                pass
            elif token in [22, 23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.sum_rest()
                self.state = 216
                self.id_cte()
                pass
            elif token in [31, 32, 33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
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


    class Id_cteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 58, self.RULE_id_cte)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(Grammar_duckParser.ID)
                pass
            elif token in [32, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
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
        self.enterRule(localctx, 60, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            _la = self._input.LA(1)
            if not(_la==32 or _la==33):
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


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def list_params(self):
            return self.getTypedRuleContext(Grammar_duckParser.List_paramsContext,0)


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
        self.enterRule(localctx, 62, self.RULE_funcs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(Grammar_duckParser.T__26)
            self.state = 228
            self.match(Grammar_duckParser.ID)
            self.state = 229
            self.match(Grammar_duckParser.T__25)
            self.state = 230
            self.list_params()
            self.state = 231
            self.match(Grammar_duckParser.T__12)
            self.state = 232
            self.match(Grammar_duckParser.T__27)
            self.state = 233
            self.var_no_var()
            self.state = 234
            self.body()
            self.state = 235
            self.match(Grammar_duckParser.T__28)
            self.state = 236
            self.match(Grammar_duckParser.T__1)
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

        def more_params(self):
            return self.getTypedRuleContext(Grammar_duckParser.More_paramsContext,0)


        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(Grammar_duckParser.TypeContext,0)


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
        self.enterRule(localctx, 64, self.RULE_list_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 238
                self.match(Grammar_duckParser.ID)
                self.state = 239
                self.match(Grammar_duckParser.T__5)
                self.state = 240
                self.type_()
                self.state = 242
                self.more_params()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(Grammar_duckParser.TypeContext,0)


        def more_params(self):
            return self.getTypedRuleContext(Grammar_duckParser.More_paramsContext,0)


        def getRuleIndex(self):
            return Grammar_duckParser.RULE_more_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMore_params" ):
                listener.enterMore_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMore_params" ):
                listener.exitMore_params(self)




    def more_params(self):

        localctx = Grammar_duckParser.More_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_more_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 246
                self.match(Grammar_duckParser.T__6)
                self.state = 247
                self.match(Grammar_duckParser.ID)
                self.state = 248
                self.match(Grammar_duckParser.T__5)
                self.state = 249
                self.type_()
                self.state = 250
                self.more_params()


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
        self.enterRule(localctx, 68, self.RULE_var_no_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 254
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
        self.enterRule(localctx, 70, self.RULE_f_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(Grammar_duckParser.ID)
            self.state = 258
            self.match(Grammar_duckParser.T__25)
            self.state = 259
            self.f_list_expresion()
            self.state = 260
            self.match(Grammar_duckParser.T__12)
            self.state = 261
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
        self.enterRule(localctx, 72, self.RULE_f_list_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15112077312) != 0):
                self.state = 263
                self.expresion()
                self.state = 264
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
        self.enterRule(localctx, 74, self.RULE_f_more_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 268
                self.match(Grammar_duckParser.T__6)
                self.state = 269
                self.expresion()
                self.state = 270
                self.f_more_expresion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





