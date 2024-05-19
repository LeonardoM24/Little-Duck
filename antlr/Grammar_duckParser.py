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
global DF
DF = Semantica()

def serializedATN():
    return [
        4,1,33,264,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,1,1,1,1,1,3,1,88,8,1,1,2,1,2,3,2,92,8,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,4,3,101,8,3,11,3,12,3,102,1,4,1,4,1,4,1,4,3,4,109,8,
        4,1,5,1,5,1,5,1,5,1,6,5,6,116,8,6,10,6,12,6,119,9,6,1,7,1,7,1,7,
        1,7,1,7,3,7,126,8,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,
        138,8,9,1,10,1,10,3,10,142,8,10,1,11,1,11,1,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,3,
        14,163,8,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,3,16,174,
        8,16,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,3,19,185,8,19,
        1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,23,3,23,198,
        8,23,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,210,
        8,25,1,26,1,26,3,26,214,8,26,1,27,1,27,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,3,29,233,8,29,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,243,8,30,1,31,1,31,
        1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,3,33,256,8,33,1,34,
        1,34,1,34,1,34,3,34,262,8,34,1,34,0,0,35,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        64,66,68,0,3,1,0,20,21,1,0,22,23,1,0,31,32,252,0,70,1,0,0,0,2,87,
        1,0,0,0,4,91,1,0,0,0,6,100,1,0,0,0,8,104,1,0,0,0,10,110,1,0,0,0,
        12,117,1,0,0,0,14,125,1,0,0,0,16,127,1,0,0,0,18,137,1,0,0,0,20,141,
        1,0,0,0,22,143,1,0,0,0,24,148,1,0,0,0,26,154,1,0,0,0,28,162,1,0,
        0,0,30,164,1,0,0,0,32,173,1,0,0,0,34,175,1,0,0,0,36,177,1,0,0,0,
        38,184,1,0,0,0,40,186,1,0,0,0,42,188,1,0,0,0,44,190,1,0,0,0,46,197,
        1,0,0,0,48,199,1,0,0,0,50,209,1,0,0,0,52,213,1,0,0,0,54,215,1,0,
        0,0,56,217,1,0,0,0,58,232,1,0,0,0,60,234,1,0,0,0,62,244,1,0,0,0,
        64,246,1,0,0,0,66,255,1,0,0,0,68,261,1,0,0,0,70,71,5,1,0,0,71,72,
        6,0,-1,0,72,73,6,0,-1,0,73,74,5,30,0,0,74,75,6,0,-1,0,75,76,5,2,
        0,0,76,77,3,4,2,0,77,78,3,2,1,0,78,79,5,3,0,0,79,80,3,10,5,0,80,
        81,5,4,0,0,81,82,6,0,-1,0,82,83,5,0,0,1,83,1,1,0,0,0,84,85,3,56,
        28,0,85,86,3,2,1,0,86,88,1,0,0,0,87,84,1,0,0,0,87,88,1,0,0,0,88,
        3,1,0,0,0,89,90,5,5,0,0,90,92,3,6,3,0,91,89,1,0,0,0,91,92,1,0,0,
        0,92,5,1,0,0,0,93,94,6,3,-1,0,94,95,3,8,4,0,95,96,5,6,0,0,96,97,
        5,29,0,0,97,98,6,3,-1,0,98,99,5,2,0,0,99,101,1,0,0,0,100,93,1,0,
        0,0,101,102,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,7,1,0,0,
        0,104,105,5,30,0,0,105,108,6,4,-1,0,106,107,5,7,0,0,107,109,3,8,
        4,0,108,106,1,0,0,0,108,109,1,0,0,0,109,9,1,0,0,0,110,111,5,8,0,
        0,111,112,3,12,6,0,112,113,5,9,0,0,113,11,1,0,0,0,114,116,3,14,7,
        0,115,114,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,
        0,118,13,1,0,0,0,119,117,1,0,0,0,120,126,3,22,11,0,121,126,3,26,
        13,0,122,126,3,24,12,0,123,126,3,64,32,0,124,126,3,16,8,0,125,120,
        1,0,0,0,125,121,1,0,0,0,125,122,1,0,0,0,125,123,1,0,0,0,125,124,
        1,0,0,0,126,15,1,0,0,0,127,128,5,10,0,0,128,129,3,18,9,0,129,130,
        5,11,0,0,130,131,5,2,0,0,131,17,1,0,0,0,132,138,3,20,10,0,133,134,
        3,20,10,0,134,135,5,7,0,0,135,136,3,18,9,0,136,138,1,0,0,0,137,132,
        1,0,0,0,137,133,1,0,0,0,138,19,1,0,0,0,139,142,3,30,15,0,140,142,
        5,33,0,0,141,139,1,0,0,0,141,140,1,0,0,0,142,21,1,0,0,0,143,144,
        5,30,0,0,144,145,5,12,0,0,145,146,3,30,15,0,146,147,5,2,0,0,147,
        23,1,0,0,0,148,149,5,13,0,0,149,150,3,10,5,0,150,151,5,14,0,0,151,
        152,3,30,15,0,152,153,5,2,0,0,153,25,1,0,0,0,154,155,5,15,0,0,155,
        156,3,30,15,0,156,157,3,10,5,0,157,158,3,28,14,0,158,159,5,2,0,0,
        159,27,1,0,0,0,160,161,5,16,0,0,161,163,3,10,5,0,162,160,1,0,0,0,
        162,163,1,0,0,0,163,29,1,0,0,0,164,165,3,34,17,0,165,166,3,32,16,
        0,166,31,1,0,0,0,167,168,5,17,0,0,168,174,3,34,17,0,169,170,5,18,
        0,0,170,174,3,34,17,0,171,172,5,19,0,0,172,174,3,34,17,0,173,167,
        1,0,0,0,173,169,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,33,1,
        0,0,0,175,176,3,36,18,0,176,35,1,0,0,0,177,178,3,42,21,0,178,179,
        3,38,19,0,179,37,1,0,0,0,180,181,3,40,20,0,181,182,3,42,21,0,182,
        183,3,38,19,0,183,185,1,0,0,0,184,180,1,0,0,0,184,185,1,0,0,0,185,
        39,1,0,0,0,186,187,7,0,0,0,187,41,1,0,0,0,188,189,3,44,22,0,189,
        43,1,0,0,0,190,191,3,50,25,0,191,192,3,46,23,0,192,45,1,0,0,0,193,
        194,3,48,24,0,194,195,3,50,25,0,195,196,3,46,23,0,196,198,1,0,0,
        0,197,193,1,0,0,0,197,198,1,0,0,0,198,47,1,0,0,0,199,200,7,1,0,0,
        200,49,1,0,0,0,201,202,5,24,0,0,202,203,3,30,15,0,203,204,5,11,0,
        0,204,210,1,0,0,0,205,206,3,40,20,0,206,207,3,52,26,0,207,210,1,
        0,0,0,208,210,3,52,26,0,209,201,1,0,0,0,209,205,1,0,0,0,209,208,
        1,0,0,0,210,51,1,0,0,0,211,214,5,30,0,0,212,214,3,54,27,0,213,211,
        1,0,0,0,213,212,1,0,0,0,214,53,1,0,0,0,215,216,7,2,0,0,216,55,1,
        0,0,0,217,218,5,25,0,0,218,219,6,28,-1,0,219,220,5,30,0,0,220,221,
        6,28,-1,0,221,222,5,24,0,0,222,223,3,58,29,0,223,224,5,11,0,0,224,
        225,5,26,0,0,225,226,3,62,31,0,226,227,3,10,5,0,227,228,5,27,0,0,
        228,229,5,2,0,0,229,230,6,28,-1,0,230,57,1,0,0,0,231,233,3,60,30,
        0,232,231,1,0,0,0,232,233,1,0,0,0,233,59,1,0,0,0,234,235,5,30,0,
        0,235,236,6,30,-1,0,236,237,5,6,0,0,237,238,5,29,0,0,238,239,6,30,
        -1,0,239,242,1,0,0,0,240,241,5,7,0,0,241,243,3,60,30,0,242,240,1,
        0,0,0,242,243,1,0,0,0,243,61,1,0,0,0,244,245,3,4,2,0,245,63,1,0,
        0,0,246,247,5,30,0,0,247,248,5,24,0,0,248,249,3,66,33,0,249,250,
        5,11,0,0,250,251,5,2,0,0,251,65,1,0,0,0,252,253,3,30,15,0,253,254,
        3,68,34,0,254,256,1,0,0,0,255,252,1,0,0,0,255,256,1,0,0,0,256,67,
        1,0,0,0,257,258,5,7,0,0,258,259,3,30,15,0,259,260,3,68,34,0,260,
        262,1,0,0,0,261,257,1,0,0,0,261,262,1,0,0,0,262,69,1,0,0,0,18,87,
        91,102,108,117,125,137,141,162,173,184,197,209,213,232,242,255,261
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
    RULE_comparar_exp = 16
    RULE_exp = 17
    RULE_list_terminos = 18
    RULE_next_termino = 19
    RULE_sum_rest = 20
    RULE_termino = 21
    RULE_list_factor = 22
    RULE_next_factor = 23
    RULE_mult_div = 24
    RULE_factor = 25
    RULE_id_cte = 26
    RULE_cte = 27
    RULE_funcs = 28
    RULE_params = 29
    RULE_list_params = 30
    RULE_var_no_var = 31
    RULE_f_call = 32
    RULE_f_list_expresion = 33
    RULE_f_more_expresion = 34

    ruleNames =  [ "prog", "a_funcs", "vars", "more_vars", "list_id", "body", 
                   "list_statement", "statement", "print", "list_expresion", 
                   "exp_o_string", "assign", "cycle", "condition", "else", 
                   "expresion", "comparar_exp", "exp", "list_terminos", 
                   "next_termino", "sum_rest", "termino", "list_factor", 
                   "next_factor", "mult_div", "factor", "id_cte", "cte", 
                   "funcs", "params", "list_params", "var_no_var", "f_call", 
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
            self.state = 70
            self.match(Grammar_duckParser.T__0)
            global DF

            DF.currType = "program"
            self.state = 73
            localctx._ID = self.match(Grammar_duckParser.ID)
            try:
                DF.addFunc((None if localctx._ID is None else localctx._ID.text), DF.currType) 
                DF.currFunc = (None if localctx._ID is None else localctx._ID.text)
                DF.progName = (None if localctx._ID is None else localctx._ID.text)
            except ValueError as e: 
                print(e)
                sys.exit()
            self.state = 75
            self.match(Grammar_duckParser.T__1)
            self.state = 76
            self.vars_()
            self.state = 77
            self.a_funcs()
            self.state = 78
            self.match(Grammar_duckParser.T__2)
            self.state = 79
            self.body()
            self.state = 80
            self.match(Grammar_duckParser.T__3)
            del DF
            self.state = 82
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
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 84
                self.funcs()
                self.state = 85
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
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 89
                self.match(Grammar_duckParser.T__4)
                self.state = 90
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
            self.state = 100 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                DF.tempIDS.clear()
                self.state = 94
                self.list_id()
                self.state = 95
                self.match(Grammar_duckParser.T__5)

                self.state = 96
                localctx._TYPE = self.match(Grammar_duckParser.TYPE)

                try:
                    DF.addListVar(DF.tempIDS,(None if localctx._TYPE is None else localctx._TYPE.text),DF.currFunc)
                except ValueError as e:
                    print(e)
                    sys.exit()

                self.state = 98
                self.match(Grammar_duckParser.T__1)
                self.state = 102 
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
            self.state = 104
            localctx._ID = self.match(Grammar_duckParser.ID)

            DF.addVarTempList((None if localctx._ID is None else localctx._ID.text))

            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 106
                self.match(Grammar_duckParser.T__6)
                self.state = 107
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
            self.state = 110
            self.match(Grammar_duckParser.T__7)
            self.state = 111
            self.list_statement()
            self.state = 112
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
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073783808) != 0):
                self.state = 114
                self.statement()
                self.state = 119
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
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 124
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
            self.state = 127
            self.match(Grammar_duckParser.T__9)
            self.state = 128
            self.list_expresion()
            self.state = 129
            self.match(Grammar_duckParser.T__10)
            self.state = 130
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
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.exp_o_string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.exp_o_string()
                self.state = 134
                self.match(Grammar_duckParser.T__6)
                self.state = 135
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
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 24, 30, 31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.expresion()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
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
        self.enterRule(localctx, 22, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(Grammar_duckParser.ID)
            self.state = 144
            self.match(Grammar_duckParser.T__11)
            self.state = 145
            self.expresion()
            self.state = 146
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
        self.enterRule(localctx, 24, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(Grammar_duckParser.T__12)
            self.state = 149
            self.body()
            self.state = 150
            self.match(Grammar_duckParser.T__13)
            self.state = 151
            self.expresion()
            self.state = 152
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
            self.state = 154
            self.match(Grammar_duckParser.T__14)
            self.state = 155
            self.expresion()
            self.state = 156
            self.body()
            self.state = 157
            self.else_()
            self.state = 158
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
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 160
                self.match(Grammar_duckParser.T__15)
                self.state = 161
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
        self.enterRule(localctx, 30, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.exp()
            self.state = 165
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
        self.enterRule(localctx, 32, self.RULE_comparar_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 167
                self.match(Grammar_duckParser.T__16)
                self.state = 168
                self.exp()
                pass
            elif token in [18]:
                self.state = 169
                self.match(Grammar_duckParser.T__17)
                self.state = 170
                self.exp()
                pass
            elif token in [19]:
                self.state = 171
                self.match(Grammar_duckParser.T__18)
                self.state = 172
                self.exp()
                pass
            elif token in [2, 7, 8, 11]:
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
        self.enterRule(localctx, 34, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
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
        self.enterRule(localctx, 36, self.RULE_list_terminos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.termino()
            self.state = 178
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
        self.enterRule(localctx, 38, self.RULE_next_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20 or _la==21:
                self.state = 180
                self.sum_rest()
                self.state = 181
                self.termino()
                self.state = 182
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
        self.enterRule(localctx, 40, self.RULE_sum_rest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
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
        self.enterRule(localctx, 42, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
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
        self.enterRule(localctx, 44, self.RULE_list_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.factor()
            self.state = 191
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
        self.enterRule(localctx, 46, self.RULE_next_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22 or _la==23:
                self.state = 193
                self.mult_div()
                self.state = 194
                self.factor()
                self.state = 195
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
        self.enterRule(localctx, 48, self.RULE_mult_div)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
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
        self.enterRule(localctx, 50, self.RULE_factor)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(Grammar_duckParser.T__23)
                self.state = 202
                self.expresion()
                self.state = 203
                self.match(Grammar_duckParser.T__10)
                pass
            elif token in [20, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.sum_rest()
                self.state = 206
                self.id_cte()
                pass
            elif token in [30, 31, 32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
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
        self.enterRule(localctx, 52, self.RULE_id_cte)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(Grammar_duckParser.ID)
                pass
            elif token in [31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
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
        self.enterRule(localctx, 54, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
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
        self.enterRule(localctx, 56, self.RULE_funcs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(Grammar_duckParser.T__24)
            DF.currType = 'void'
            self.state = 219
            localctx._ID = self.match(Grammar_duckParser.ID)
            try: 
                DF.addFunc((None if localctx._ID is None else localctx._ID.text), DF.currType) 
                DF.currFunc = (None if localctx._ID is None else localctx._ID.text)
            except ValueError as e: 
                print(e)
                sys.exit()

            self.state = 221
            self.match(Grammar_duckParser.T__23)
            self.state = 222
            self.params()
            self.state = 223
            self.match(Grammar_duckParser.T__10)
            self.state = 224
            self.match(Grammar_duckParser.T__25)
            self.state = 225
            self.var_no_var()
            self.state = 226
            self.body()
            self.state = 227
            self.match(Grammar_duckParser.T__26)
            self.state = 228
            self.match(Grammar_duckParser.T__1)
            DF.delDV(DF.currFunc)
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
        self.enterRule(localctx, 58, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 231
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
        self.enterRule(localctx, 60, self.RULE_list_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            localctx._ID = self.match(Grammar_duckParser.ID)
            DF.currID = (None if localctx._ID is None else localctx._ID.text)
            self.state = 236
            self.match(Grammar_duckParser.T__5)
            self.state = 237
            localctx._TYPE = self.match(Grammar_duckParser.TYPE)

            try: 
                DF.addVar(DF.currID, (None if localctx._TYPE is None else localctx._TYPE.text), DF.currFunc) 
            except ValueError as e: 
                print(e)
                sys.exit()

            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 240
                self.match(Grammar_duckParser.T__6)
                self.state = 241
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
        self.enterRule(localctx, 62, self.RULE_var_no_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
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
        self.enterRule(localctx, 64, self.RULE_f_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(Grammar_duckParser.ID)
            self.state = 247
            self.match(Grammar_duckParser.T__23)
            self.state = 248
            self.f_list_expresion()
            self.state = 249
            self.match(Grammar_duckParser.T__10)
            self.state = 250
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
        self.enterRule(localctx, 66, self.RULE_f_list_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7536115712) != 0):
                self.state = 252
                self.expresion()
                self.state = 253
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
        self.enterRule(localctx, 68, self.RULE_f_more_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 257
                self.match(Grammar_duckParser.T__6)
                self.state = 258
                self.expresion()
                self.state = 259
                self.f_more_expresion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





