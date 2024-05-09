grammar Grammar_duck;	

prog    : 'program' ID ';' a_vars a_funcs 'main' body 'end' EOF;
a_vars  : (vars)? ;
a_funcs : (funcs a_funcs)?;

vars      : 'var' list_vars;
list_vars : ID list_id ':' type ';' more_vars;
more_vars : (ID list_id ':' type ';' more_vars)?;
list_id   : (',' ID list_id)?;

type : 'int' | 'float';

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


funcs       : 'void' ID '(' list_params ')' '[' var_no_var body ']' ';';
list_params : ((ID ':' type) more_params)?;
more_params : (',' ID ':' type more_params)?;
var_no_var  : (vars)?;

f_call           : ID '(' f_list_expresion ')' ';';
f_list_expresion : (expresion f_more_expresion)?;
f_more_expresion : (',' expresion f_more_expresion)?;


// TOKENS

SKIPS : [ \r\t\n]+ -> skip ; // skip -->  espacios, enters y tabs

ID         : [a-zA-Z][A-Za-z0-9_]* ;
CTE_INT    : [0-9]+ ;
CTE_FLOAT  : [0-9]+'.'[0-9]+ ;
CTE_STRING : '\'' (~[\n]*) '\''
            | '"' (~[\n]*) '"' ;

