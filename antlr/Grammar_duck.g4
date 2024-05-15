//antlr4 -Dlanguage=Python3 Grammar_duck.g4

grammar Grammar_duck;	

@header {
import sys
sys.path.insert(0, './Semantica.py') 
from Semantica import DirectorioFunciones
global DF
DF = DirectorioFunciones()
}


prog    : 'program'{global DF}
{
DF.currType = "program"}
        ID 
{try:
    DF.addFunc($ID.text, DF.currType) 
    DF.currFunc = $ID.text
except ValueError as e: 
    print(e)
    sys.exit()} 
        ';' vars a_funcs 'main' body 'end' {del DF} EOF;


a_funcs : (funcs a_funcs)?;

vars      : ('var' more_vars)?;
more_vars : ( {DF.tempIDS.clear()} list_id ':' (TYPE) 
{
try:
    DF.addListVar(DF.tempIDS,$TYPE.text,DF.currFunc)
except ValueError as e:
    print(e)
    sys.exit()
}';')+;
list_id   : ID 
{
DF.addVarTempList($ID.text)
} (',' list_id)?;



body           : '{' list_statement '}';
list_statement : (statement)*;

statement   : assign
            | condition
            | cycle
            | f_call
            | print;

print           : 'print(' list_expresion ')' ';' ;
list_expresion  : exp_o_string
                | exp_o_string ',' list_expresion;
exp_o_string    : expresion | CTE_STRING;

assign : ID '=' expresion';';

cycle : 'do' body 'while' expresion ';';

condition : 'if' expresion body else';';
else      : ('else' body)?;

expresion    : exp comparar_exp;
comparar_exp : ( '<' exp | '>' exp | '!=' exp)?;

exp           : list_terminos;
list_terminos : termino next_termino;
next_termino  : (sum_rest termino next_termino)?;
sum_rest      : '+' | '-';

termino     : list_factor;
list_factor : factor next_factor;
next_factor : (mult_div factor next_factor)?;
mult_div    : '*' | '/' ;

factor  : '(' expresion ')' 
        | sum_rest id_cte
        | id_cte;
id_cte: ID | cte;

cte: CTE_INT | CTE_FLOAT;


funcs       : 'void' {DF.currType = 'void'} 
ID {try: 
    DF.addFunc($ID.text, DF.currType) 
    DF.currFunc = $ID.text
except ValueError as e: 
    print(e)
    sys.exit()
}
'(' params ')' '[' var_no_var body ']' ';' {DF.delDV(DF.currFunc)};

params: (list_params)?;
list_params: (ID {DF.currID = $ID.text}
':' TYPE
{
try: 
    DF.addVar(DF.currID, $TYPE.text, DF.currFunc) 
except ValueError as e: 
    print(e)
    sys.exit()
}
) (',' list_params)? ;
var_no_var  : vars;

f_call           : ID '(' f_list_expresion ')' ';';
f_list_expresion : (expresion f_more_expresion)?;
f_more_expresion : (',' expresion f_more_expresion)?;


// TOKENS

SKIPS : [ \r\t\n]+ -> skip ; // skip -->  espacios, enters y tabs

TYPE       : 'int' | 'float';
ID         : [a-zA-Z][A-Za-z0-9_]* ;
CTE_INT    : [0-9]+ ;
CTE_FLOAT  : [0-9]+'.'[0-9]+ ;
CTE_STRING : '\'' (~[\n]*) '\'' | '"' (~[\n]*) '"' ;
