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
        4,1,35,266,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,1,3,1,88,8,1,1,2,1,2,1,2,3,2,93,8,2,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,
        5,112,8,5,1,6,1,6,3,6,116,8,6,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,
        9,3,9,127,8,9,1,10,1,10,1,10,1,10,1,10,3,10,134,8,10,1,11,1,11,1,
        11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,145,8,12,1,13,1,13,3,13,149,
        8,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,1,16,1,17,1,17,3,17,170,8,17,1,18,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,19,3,19,181,8,19,1,20,1,20,1,21,1,21,
        1,21,1,22,1,22,1,22,1,22,3,22,192,8,22,1,23,1,23,1,24,1,24,1,25,
        1,25,1,25,1,26,1,26,1,26,1,26,3,26,205,8,26,1,27,1,27,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,3,28,217,8,28,1,29,1,29,3,29,221,8,
        29,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,
        31,1,32,1,32,1,32,1,32,3,32,240,8,32,1,33,1,33,1,33,1,33,1,33,1,
        33,3,33,248,8,33,1,34,3,34,251,8,34,1,35,1,35,1,35,1,35,1,36,3,36,
        258,8,36,1,37,1,37,1,37,1,37,3,37,264,8,37,1,37,0,0,38,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,
        54,56,58,60,62,64,66,68,70,72,74,0,4,1,0,8,9,1,0,23,24,1,0,25,26,
        1,0,33,34,252,0,76,1,0,0,0,2,87,1,0,0,0,4,92,1,0,0,0,6,94,1,0,0,
        0,8,97,1,0,0,0,10,111,1,0,0,0,12,115,1,0,0,0,14,117,1,0,0,0,16,119,
        1,0,0,0,18,126,1,0,0,0,20,133,1,0,0,0,22,135,1,0,0,0,24,144,1,0,
        0,0,26,148,1,0,0,0,28,150,1,0,0,0,30,155,1,0,0,0,32,161,1,0,0,0,
        34,169,1,0,0,0,36,171,1,0,0,0,38,180,1,0,0,0,40,182,1,0,0,0,42,184,
        1,0,0,0,44,191,1,0,0,0,46,193,1,0,0,0,48,195,1,0,0,0,50,197,1,0,
        0,0,52,204,1,0,0,0,54,206,1,0,0,0,56,216,1,0,0,0,58,220,1,0,0,0,
        60,222,1,0,0,0,62,224,1,0,0,0,64,239,1,0,0,0,66,247,1,0,0,0,68,250,
        1,0,0,0,70,252,1,0,0,0,72,257,1,0,0,0,74,263,1,0,0,0,76,77,5,1,0,
        0,77,78,5,32,0,0,78,79,5,2,0,0,79,80,3,2,1,0,80,81,3,4,2,0,81,82,
        5,3,0,0,82,83,3,16,8,0,83,84,5,4,0,0,84,85,5,0,0,1,85,1,1,0,0,0,
        86,88,3,6,3,0,87,86,1,0,0,0,87,88,1,0,0,0,88,3,1,0,0,0,89,90,3,62,
        31,0,90,91,3,4,2,0,91,93,1,0,0,0,92,89,1,0,0,0,92,93,1,0,0,0,93,
        5,1,0,0,0,94,95,5,5,0,0,95,96,3,8,4,0,96,7,1,0,0,0,97,98,5,32,0,
        0,98,99,3,12,6,0,99,100,5,6,0,0,100,101,3,14,7,0,101,102,5,2,0,0,
        102,103,3,10,5,0,103,9,1,0,0,0,104,105,5,32,0,0,105,106,3,12,6,0,
        106,107,5,6,0,0,107,108,3,14,7,0,108,109,5,2,0,0,109,110,3,10,5,
        0,110,112,1,0,0,0,111,104,1,0,0,0,111,112,1,0,0,0,112,11,1,0,0,0,
        113,114,5,7,0,0,114,116,5,32,0,0,115,113,1,0,0,0,115,116,1,0,0,0,
        116,13,1,0,0,0,117,118,7,0,0,0,118,15,1,0,0,0,119,120,5,10,0,0,120,
        121,3,18,9,0,121,122,5,11,0,0,122,17,1,0,0,0,123,124,3,20,10,0,124,
        125,3,18,9,0,125,127,1,0,0,0,126,123,1,0,0,0,126,127,1,0,0,0,127,
        19,1,0,0,0,128,134,3,28,14,0,129,134,3,32,16,0,130,134,3,30,15,0,
        131,134,3,70,35,0,132,134,3,22,11,0,133,128,1,0,0,0,133,129,1,0,
        0,0,133,130,1,0,0,0,133,131,1,0,0,0,133,132,1,0,0,0,134,21,1,0,0,
        0,135,136,5,12,0,0,136,137,3,24,12,0,137,138,5,13,0,0,138,23,1,0,
        0,0,139,145,3,26,13,0,140,141,3,26,13,0,141,142,5,7,0,0,142,143,
        3,24,12,0,143,145,1,0,0,0,144,139,1,0,0,0,144,140,1,0,0,0,145,25,
        1,0,0,0,146,149,3,36,18,0,147,149,5,35,0,0,148,146,1,0,0,0,148,147,
        1,0,0,0,149,27,1,0,0,0,150,151,5,14,0,0,151,152,5,15,0,0,152,153,
        3,36,18,0,153,154,5,2,0,0,154,29,1,0,0,0,155,156,5,16,0,0,156,157,
        3,16,8,0,157,158,5,17,0,0,158,159,3,36,18,0,159,160,5,2,0,0,160,
        31,1,0,0,0,161,162,5,18,0,0,162,163,3,36,18,0,163,164,3,16,8,0,164,
        165,3,34,17,0,165,166,5,2,0,0,166,33,1,0,0,0,167,168,5,19,0,0,168,
        170,3,16,8,0,169,167,1,0,0,0,169,170,1,0,0,0,170,35,1,0,0,0,171,
        172,3,40,20,0,172,173,3,38,19,0,173,37,1,0,0,0,174,175,5,20,0,0,
        175,181,3,40,20,0,176,177,5,21,0,0,177,181,3,40,20,0,178,179,5,22,
        0,0,179,181,3,40,20,0,180,174,1,0,0,0,180,176,1,0,0,0,180,178,1,
        0,0,0,180,181,1,0,0,0,181,39,1,0,0,0,182,183,3,42,21,0,183,41,1,
        0,0,0,184,185,3,48,24,0,185,186,3,44,22,0,186,43,1,0,0,0,187,188,
        3,46,23,0,188,189,3,48,24,0,189,190,3,44,22,0,190,192,1,0,0,0,191,
        187,1,0,0,0,191,192,1,0,0,0,192,45,1,0,0,0,193,194,7,1,0,0,194,47,
        1,0,0,0,195,196,3,50,25,0,196,49,1,0,0,0,197,198,3,56,28,0,198,199,
        3,52,26,0,199,51,1,0,0,0,200,201,3,54,27,0,201,202,3,56,28,0,202,
        203,3,52,26,0,203,205,1,0,0,0,204,200,1,0,0,0,204,205,1,0,0,0,205,
        53,1,0,0,0,206,207,7,2,0,0,207,55,1,0,0,0,208,209,5,27,0,0,209,210,
        3,36,18,0,210,211,5,13,0,0,211,217,1,0,0,0,212,213,3,46,23,0,213,
        214,3,58,29,0,214,217,1,0,0,0,215,217,3,58,29,0,216,208,1,0,0,0,
        216,212,1,0,0,0,216,215,1,0,0,0,217,57,1,0,0,0,218,221,5,32,0,0,
        219,221,3,60,30,0,220,218,1,0,0,0,220,219,1,0,0,0,221,59,1,0,0,0,
        222,223,7,3,0,0,223,61,1,0,0,0,224,225,5,28,0,0,225,226,5,32,0,0,
        226,227,5,27,0,0,227,228,3,64,32,0,228,229,5,13,0,0,229,230,5,29,
        0,0,230,231,3,68,34,0,231,232,3,16,8,0,232,233,5,30,0,0,233,234,
        5,2,0,0,234,63,1,0,0,0,235,236,5,32,0,0,236,237,5,6,0,0,237,240,
        3,14,7,0,238,240,3,66,33,0,239,235,1,0,0,0,239,238,1,0,0,0,240,65,
        1,0,0,0,241,242,5,7,0,0,242,243,5,32,0,0,243,244,5,6,0,0,244,245,
        3,14,7,0,245,246,3,66,33,0,246,248,1,0,0,0,247,241,1,0,0,0,247,248,
        1,0,0,0,248,67,1,0,0,0,249,251,3,6,3,0,250,249,1,0,0,0,250,251,1,
        0,0,0,251,69,1,0,0,0,252,253,5,32,0,0,253,254,5,27,0,0,254,255,5,
        13,0,0,255,71,1,0,0,0,256,258,3,36,18,0,257,256,1,0,0,0,257,258,
        1,0,0,0,258,73,1,0,0,0,259,260,5,7,0,0,260,261,3,36,18,0,261,262,
        3,74,37,0,262,264,1,0,0,0,263,259,1,0,0,0,263,264,1,0,0,0,264,75,
        1,0,0,0,19,87,92,111,115,126,133,144,148,169,180,191,204,216,220,
        239,247,250,257,263
    ]

class Grammar_duckParser ( Parser ):

    grammarFileName = "Grammar_duck.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'main'", "'end'", 
                     "'var'", "':'", "','", "'int'", "'float'", "'{'", "'}'", 
                     "'print('", "')'", "'id'", "'='", "'while'", "'do'", 
                     "'if'", "'else'", "'<'", "'>'", "'!='", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "'void'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SKIPS", "ID", 
                      "CTE_INT", "CTE_FLOAT", "CTE_STRING" ]

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
    T__29=30
    SKIPS=31
    ID=32
    CTE_INT=33
    CTE_FLOAT=34
    CTE_STRING=35

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
            if _la==28:
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
            if _la==32:
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
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 113
                self.match(Grammar_duckParser.T__6)
                self.state = 114
                self.match(Grammar_duckParser.ID)


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
            self.state = 117
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
            self.state = 119
            self.match(Grammar_duckParser.T__9)
            self.state = 120
            self.list_statement()
            self.state = 121
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

        def statement(self):
            return self.getTypedRuleContext(Grammar_duckParser.StatementContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(Grammar_duckParser.List_statementContext,0)


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
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4295315456) != 0):
                self.state = 123
                self.statement()
                self.state = 124
                self.list_statement()


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
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.assign()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.condition()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.cycle()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.f_call()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.print_()
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
            self.state = 135
            self.match(Grammar_duckParser.T__11)
            self.state = 136
            self.list_expresion()
            self.state = 137
            self.match(Grammar_duckParser.T__12)
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
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.exp_o_string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.exp_o_string()
                self.state = 141
                self.match(Grammar_duckParser.T__6)
                self.state = 142
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
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 27, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.expresion()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
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
            self.state = 150
            self.match(Grammar_duckParser.T__13)
            self.state = 151
            self.match(Grammar_duckParser.T__14)
            self.state = 152
            self.expresion()
            self.state = 153
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
            self.state = 155
            self.match(Grammar_duckParser.T__15)
            self.state = 156
            self.body()
            self.state = 157
            self.match(Grammar_duckParser.T__16)
            self.state = 158
            self.expresion()
            self.state = 159
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
            self.state = 161
            self.match(Grammar_duckParser.T__17)
            self.state = 162
            self.expresion()
            self.state = 163
            self.body()
            self.state = 164
            self.else_()
            self.state = 165
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
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 167
                self.match(Grammar_duckParser.T__18)
                self.state = 168
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
            self.state = 171
            self.exp()
            self.state = 172
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
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 174
                self.match(Grammar_duckParser.T__19)
                self.state = 175
                self.exp()
                pass
            elif token in [21]:
                self.state = 176
                self.match(Grammar_duckParser.T__20)
                self.state = 177
                self.exp()
                pass
            elif token in [22]:
                self.state = 178
                self.match(Grammar_duckParser.T__21)
                self.state = 179
                self.exp()
                pass
            elif token in [-1, 2, 7, 10, 13]:
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
            self.state = 182
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
            self.state = 184
            self.termino()
            self.state = 185
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
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23 or _la==24:
                self.state = 187
                self.sum_rest()
                self.state = 188
                self.termino()
                self.state = 189
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
            self.state = 193
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
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
            self.state = 195
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
            self.state = 197
            self.factor()
            self.state = 198
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
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25 or _la==26:
                self.state = 200
                self.mult_div()
                self.state = 201
                self.factor()
                self.state = 202
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
            self.state = 206
            _la = self._input.LA(1)
            if not(_la==25 or _la==26):
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
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(Grammar_duckParser.T__26)
                self.state = 209
                self.expresion()
                self.state = 210
                self.match(Grammar_duckParser.T__12)
                pass
            elif token in [23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.sum_rest()
                self.state = 213
                self.id_cte()
                pass
            elif token in [32, 33, 34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
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
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(Grammar_duckParser.ID)
                pass
            elif token in [33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
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
            self.state = 222
            _la = self._input.LA(1)
            if not(_la==33 or _la==34):
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
            self.state = 224
            self.match(Grammar_duckParser.T__27)
            self.state = 225
            self.match(Grammar_duckParser.ID)
            self.state = 226
            self.match(Grammar_duckParser.T__26)
            self.state = 227
            self.list_params()
            self.state = 228
            self.match(Grammar_duckParser.T__12)
            self.state = 229
            self.match(Grammar_duckParser.T__28)
            self.state = 230
            self.var_no_var()
            self.state = 231
            self.body()
            self.state = 232
            self.match(Grammar_duckParser.T__29)
            self.state = 233
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

        def ID(self):
            return self.getToken(Grammar_duckParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(Grammar_duckParser.TypeContext,0)


        def more_params(self):
            return self.getTypedRuleContext(Grammar_duckParser.More_paramsContext,0)


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
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(Grammar_duckParser.ID)
                self.state = 236
                self.match(Grammar_duckParser.T__5)
                self.state = 237
                self.type_()
                pass
            elif token in [7, 13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.more_params()
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
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 241
                self.match(Grammar_duckParser.T__6)
                self.state = 242
                self.match(Grammar_duckParser.ID)
                self.state = 243
                self.match(Grammar_duckParser.T__5)
                self.state = 244
                self.type_()
                self.state = 245
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
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 249
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
            self.state = 252
            self.match(Grammar_duckParser.ID)
            self.state = 253
            self.match(Grammar_duckParser.T__26)
            self.state = 254
            self.match(Grammar_duckParser.T__12)
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
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30224154624) != 0):
                self.state = 256
                self.expresion()


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 259
                self.match(Grammar_duckParser.T__6)
                self.state = 260
                self.expresion()
                self.state = 261
                self.f_more_expresion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




