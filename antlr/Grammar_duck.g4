//antlr4 -Dlanguage=Python3 Grammar_duck.g4

grammar Grammar_duck;	

@header {
import sys
sys.path.insert(0, './Semantica.py') 
from Semantica import Semantica
global Semantica
Semantica = Semantica()
}


///////////////////////////////////////////////////////////
prog    : 'program'{global Semantica}
{
Semantica.currType = "program"}
        ID 
{try:
    Semantica.addFunc($ID.text, Semantica.currType) 
    Semantica.currFunc = $ID.text
    Semantica.progName = $ID.text
except ValueError as e: 
    print(e)
    sys.exit()} 
        ';' vars a_funcs 'main' body 'end' 
        {print(Semantica.cuadruplos)} 
        {del Semantica} EOF;


a_funcs : (funcs a_funcs)?;
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
vars      : ('var' more_vars)?;
more_vars : ( {Semantica.tempIDS.clear()} list_id ':' (TYPE) 
{
try:
    Semantica.addListVar(Semantica.tempIDS,$TYPE.text,Semantica.currFunc)
except ValueError as e:
    print(e)
    sys.exit()
}';')+;
list_id   : ID 
{
Semantica.addVarTempList($ID.text)
} (',' list_id)?;
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
body           : '{' list_statement '}';
list_statement : (statement)*;

statement   : assign
            | condition
            | cycle
            | f_call
            | print;
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
print           : 'print(' list_expresion ')' ';' ;
list_expresion  : exp_o_string
                | exp_o_string ',' list_expresion;
exp_o_string    : expresion | CTE_STRING;
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
assign : ID {
try:
    Semantica.addPilaVar($ID.text)
except ValueError as e:
    print(e)
    sys.exit()
} '=' {
Semantica.addPilaOp(7) # 7 = "="
} expresion';'{
op = Semantica.pilaOperadores.pop() # debe ser un 7 "="
opD = Semantica.pilaVariables.pop() # operando derecho 
opI = Semantica.pilaVariables.pop() # operando izquierdo
try:
    Semantica.addCuadruplo(op,opI,opD)
except MemoryError() as e:
    print(e)
    sys.exit()

};
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
cycle : 'do' body 'while' expresion ';';
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
condition : 'if' expresion body else';';
else      : ('else' body)?;
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
expresion    : exp comparar;
comparar     : (comparacion exp {
# terminar la comparacion
op = Semantica.pilaOperadores.pop() # debe ser un 4,5 o 6
opD = Semantica.pilaVariables.pop()
opI = Semantica.pilaVariables.pop()
try:
    Semantica.addCuadruplo(op,opI,opD)
except MemoryError() as e:
    print(e)
    sys.exit()
})? ;
comparacion  : 
'<' {Semantica.addPilaOp(4)} 
| '>' {Semantica.addPilaOp(5)} 
| '!=' {Semantica.addPilaOp(6)};
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
exp : termino{
if Semantica.pilaOperadores[-1] == 0 or Semantica.pilaOperadores[-1] == 1:
    op = Semantica.pilaOperadores.pop()
    opD = Semantica.pilaVariables.pop()
    opI = Semantica.pilaVariables.pop()
    try:
        Semantica.addCuadruplo(op,opI,opD)
    except MemoryError() as e:
        print(e)
        sys.exit()
} (sum_rest termino)*;
sum_rest      : 
'+' {Semantica.addPilaOp(0)}
| '-' {Semantica.addPilaOp(1)};
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
termino : factor{
if Semantica.pilaOperadores[-1] == 2 or Semantica.pilaOperadores[-1] == 3:
    op = Semantica.pilaOperadores.pop()
    opD = Semantica.pilaVariables.pop()
    opI = Semantica.pilaVariables.pop()
    try:
        Semantica.addCuadruplo(op,opI,opD)
    except MemoryError() as e:
        print(e)
        sys.exit()
}(mult_div factor)*;
mult_div    : 
'*' {Semantica.addPilaOp(2)}
| '/' {Semantica.addPilaOp(3)};
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
factor  : '(' {
Semantica.addPilaOp(-1) # meter barrera
} expresion ')' {
Semantica.pilaOperadores.pop() # sacar barrera
}
| positivo_negativo id_cte {
op = Semantica.pilaOperadores.pop() # tiene que ser un *
opD = Semantica.pilaVariables.pop() # variable o cte
opI = Semantica.pilaVariables.pop() # -1
try:
    Semantica.addCuadruplo(op,opI,opD) # *, -1, var, temp = -var
except MemoryError() as e:
    print(e)
    sys.exit()
}
| id_cte;

positivo_negativo: 
'+' {#Semantica.convertirMenos = False} 
| '-' {
#Semantica.convertirMenos = True
Semantica.addCTE(-1,"int") # agregamos -1 si no existe
Semantica.addPilaOp(2) # agregamos *
Semantica.addPilaVar(-1) # agregar -1 a pila de variables
};

id_cte: ID{
try:
    Semantica.addPilaVar($ID.text)
except ValueError as e:
    print(e)
    sys.exit()
} | cte;
cte: 
CTE_INT {
Semantica.addCTE($CTE_INT.text, 'int')
Semantica.addPilaVar($CTE_INT.text)
}
| CTE_FLOAT {
Semantica.addCTE($CTE_FLOAT.text, 'float')
Semantica.addPilaVar($CTE_FLOAT.text)
};
//////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
funcs       : 'void' {Semantica.currType = 'void'} 
ID {try: 
    Semantica.addFunc($ID.text, Semantica.currType) 
    Semantica.currFunc = $ID.text
except ValueError as e: 
    print(e)
    sys.exit()
}
'(' params ')' '[' var_no_var body ']' ';' {Semantica.delDV(Semantica.currFunc)};

params: (list_params)?;
list_params: (ID {Semantica.currID = $ID.text}
':' TYPE
{
try: 
    Semantica.addVar(Semantica.currID, $TYPE.text, Semantica.currFunc) 
except ValueError as e: 
    print(e)
    sys.exit()
}
) (',' list_params)? ;
var_no_var  : vars;
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
f_call           : ID '(' f_list_expresion ')' ';';
f_list_expresion : (expresion f_more_expresion)?;
f_more_expresion : (',' expresion f_more_expresion)?;
///////////////////////////////////////////////////////////


// TOKENS =================================================

SKIPS : [ \r\t\n]+ -> skip ; // skip -->  espacios, enters y tabs

TYPE       : 'int' | 'float';
ID         : [a-zA-Z][A-Za-z0-9_]* ;
CTE_INT    : [0-9]+ ;
CTE_FLOAT  : [0-9]+'.'[0-9]+ ;
CTE_STRING : '\'' (~[\n]*) '\'' | '"' (~[\n]*) '"' ;
