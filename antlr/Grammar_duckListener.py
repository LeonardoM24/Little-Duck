# Generated from Grammar_duck.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Grammar_duckParser import Grammar_duckParser
else:
    from Grammar_duckParser import Grammar_duckParser

import sys
sys.path.insert(0, './Semantica.py') 
from Semantica import Semantica
global DF
DF = Semantica()


# This class defines a complete listener for a parse tree produced by Grammar_duckParser.
class Grammar_duckListener(ParseTreeListener):

    # Enter a parse tree produced by Grammar_duckParser#prog.
    def enterProg(self, ctx:Grammar_duckParser.ProgContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#prog.
    def exitProg(self, ctx:Grammar_duckParser.ProgContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#a_funcs.
    def enterA_funcs(self, ctx:Grammar_duckParser.A_funcsContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#a_funcs.
    def exitA_funcs(self, ctx:Grammar_duckParser.A_funcsContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#vars.
    def enterVars(self, ctx:Grammar_duckParser.VarsContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#vars.
    def exitVars(self, ctx:Grammar_duckParser.VarsContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#more_vars.
    def enterMore_vars(self, ctx:Grammar_duckParser.More_varsContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#more_vars.
    def exitMore_vars(self, ctx:Grammar_duckParser.More_varsContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#list_id.
    def enterList_id(self, ctx:Grammar_duckParser.List_idContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#list_id.
    def exitList_id(self, ctx:Grammar_duckParser.List_idContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#body.
    def enterBody(self, ctx:Grammar_duckParser.BodyContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#body.
    def exitBody(self, ctx:Grammar_duckParser.BodyContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#list_statement.
    def enterList_statement(self, ctx:Grammar_duckParser.List_statementContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#list_statement.
    def exitList_statement(self, ctx:Grammar_duckParser.List_statementContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#statement.
    def enterStatement(self, ctx:Grammar_duckParser.StatementContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#statement.
    def exitStatement(self, ctx:Grammar_duckParser.StatementContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#print.
    def enterPrint(self, ctx:Grammar_duckParser.PrintContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#print.
    def exitPrint(self, ctx:Grammar_duckParser.PrintContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#list_expresion.
    def enterList_expresion(self, ctx:Grammar_duckParser.List_expresionContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#list_expresion.
    def exitList_expresion(self, ctx:Grammar_duckParser.List_expresionContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#exp_o_string.
    def enterExp_o_string(self, ctx:Grammar_duckParser.Exp_o_stringContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#exp_o_string.
    def exitExp_o_string(self, ctx:Grammar_duckParser.Exp_o_stringContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#assign.
    def enterAssign(self, ctx:Grammar_duckParser.AssignContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#assign.
    def exitAssign(self, ctx:Grammar_duckParser.AssignContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#cycle.
    def enterCycle(self, ctx:Grammar_duckParser.CycleContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#cycle.
    def exitCycle(self, ctx:Grammar_duckParser.CycleContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#condition.
    def enterCondition(self, ctx:Grammar_duckParser.ConditionContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#condition.
    def exitCondition(self, ctx:Grammar_duckParser.ConditionContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#else.
    def enterElse(self, ctx:Grammar_duckParser.ElseContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#else.
    def exitElse(self, ctx:Grammar_duckParser.ElseContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#expresion.
    def enterExpresion(self, ctx:Grammar_duckParser.ExpresionContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#expresion.
    def exitExpresion(self, ctx:Grammar_duckParser.ExpresionContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#comparar_exp.
    def enterComparar_exp(self, ctx:Grammar_duckParser.Comparar_expContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#comparar_exp.
    def exitComparar_exp(self, ctx:Grammar_duckParser.Comparar_expContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#exp.
    def enterExp(self, ctx:Grammar_duckParser.ExpContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#exp.
    def exitExp(self, ctx:Grammar_duckParser.ExpContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#list_terminos.
    def enterList_terminos(self, ctx:Grammar_duckParser.List_terminosContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#list_terminos.
    def exitList_terminos(self, ctx:Grammar_duckParser.List_terminosContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#next_termino.
    def enterNext_termino(self, ctx:Grammar_duckParser.Next_terminoContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#next_termino.
    def exitNext_termino(self, ctx:Grammar_duckParser.Next_terminoContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#sum_rest.
    def enterSum_rest(self, ctx:Grammar_duckParser.Sum_restContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#sum_rest.
    def exitSum_rest(self, ctx:Grammar_duckParser.Sum_restContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#termino.
    def enterTermino(self, ctx:Grammar_duckParser.TerminoContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#termino.
    def exitTermino(self, ctx:Grammar_duckParser.TerminoContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#list_factor.
    def enterList_factor(self, ctx:Grammar_duckParser.List_factorContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#list_factor.
    def exitList_factor(self, ctx:Grammar_duckParser.List_factorContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#next_factor.
    def enterNext_factor(self, ctx:Grammar_duckParser.Next_factorContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#next_factor.
    def exitNext_factor(self, ctx:Grammar_duckParser.Next_factorContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#mult_div.
    def enterMult_div(self, ctx:Grammar_duckParser.Mult_divContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#mult_div.
    def exitMult_div(self, ctx:Grammar_duckParser.Mult_divContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#factor.
    def enterFactor(self, ctx:Grammar_duckParser.FactorContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#factor.
    def exitFactor(self, ctx:Grammar_duckParser.FactorContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#id_cte.
    def enterId_cte(self, ctx:Grammar_duckParser.Id_cteContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#id_cte.
    def exitId_cte(self, ctx:Grammar_duckParser.Id_cteContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#cte.
    def enterCte(self, ctx:Grammar_duckParser.CteContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#cte.
    def exitCte(self, ctx:Grammar_duckParser.CteContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#funcs.
    def enterFuncs(self, ctx:Grammar_duckParser.FuncsContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#funcs.
    def exitFuncs(self, ctx:Grammar_duckParser.FuncsContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#params.
    def enterParams(self, ctx:Grammar_duckParser.ParamsContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#params.
    def exitParams(self, ctx:Grammar_duckParser.ParamsContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#list_params.
    def enterList_params(self, ctx:Grammar_duckParser.List_paramsContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#list_params.
    def exitList_params(self, ctx:Grammar_duckParser.List_paramsContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#var_no_var.
    def enterVar_no_var(self, ctx:Grammar_duckParser.Var_no_varContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#var_no_var.
    def exitVar_no_var(self, ctx:Grammar_duckParser.Var_no_varContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#f_call.
    def enterF_call(self, ctx:Grammar_duckParser.F_callContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#f_call.
    def exitF_call(self, ctx:Grammar_duckParser.F_callContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#f_list_expresion.
    def enterF_list_expresion(self, ctx:Grammar_duckParser.F_list_expresionContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#f_list_expresion.
    def exitF_list_expresion(self, ctx:Grammar_duckParser.F_list_expresionContext):
        pass


    # Enter a parse tree produced by Grammar_duckParser#f_more_expresion.
    def enterF_more_expresion(self, ctx:Grammar_duckParser.F_more_expresionContext):
        pass

    # Exit a parse tree produced by Grammar_duckParser#f_more_expresion.
    def exitF_more_expresion(self, ctx:Grammar_duckParser.F_more_expresionContext):
        pass



del Grammar_duckParser