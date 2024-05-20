//antlr4 -Dlanguage=Python3 Grammar_duck.g4

grammar Grammar_duck;	

@header {
import sys
sys.path.insert(0, './Semantica.py') 
from Semantica import Semantica
global semantica
semantica = Semantica()
}


///////////////////////////////////////////////////////////
prog    : 'program'{global semantica}
{
semantica.currType = "program"}
        ID 
{try:
    semantica.addFunc($ID.text, semantica.currType) 
    semantica.currFunc = $ID.text
    semantica.progName = $ID.text
except ValueError as e: 
    print(e)
    sys.exit()} 
        ';' vars a_funcs 'main' body 'end' 
        {del semantica} EOF;


a_funcs : (funcs a_funcs)?;
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
vars      : ('var' more_vars)?;
more_vars : ( {semantica.tempIDS.clear()} list_id ':' (TYPE) 
{
try:
    semantica.addListVar(semantica.tempIDS,$TYPE.text,semantica.currFunc)
except ValueError as e:
    print(e)
    sys.exit()
}';')+;
list_id   : ID 
{
semantica.addVarTempList($ID.text)
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
print           : 'print(' list_expresion ')' ';'{
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
} ;
list_expresion  : exp_o_string
                | exp_o_string ','{
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
} list_expresion;
exp_o_string    : expresion | CTE_STRING {
cte = $CTE_STRING.text
try:
    semantica.addCTE(cte,"string")
except ValueError as e:
    print(e)
    sys.exit()
try:
    semantica.addPilaVar(cte)
except ValueError as e:
    print(e)
    sys.exit()
};
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
assign : ID {
try:
    semantica.addPilaVar($ID.text)
except ValueError as e:
    print(e)
    sys.exit()
} '=' {
semantica.addPilaOp(7) # 7 = "="
} expresion';'{
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
};
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
cycle : 'do'{
indice = semantica.currCuadruplo
semantica.pilaSaltos.append(indice)
} body 'while' '(' expresion ')' ';'{
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
};
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
condition : 'if' '(' expresion ')' 
{
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
}body else';' {
indice = semantica.pilaSaltos.pop() # a donde tenemos que regrear para editar
semantica.setGoTo(indice, semantica.currCuadruplo)
};

else      : ('else' {
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
} body)?;
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
expresion    : exp comparar?;
comparar     : (comparacion exp {
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
}) ;
comparacion  : 
'<' {semantica.addPilaOp(4)} 
| '>' {semantica.addPilaOp(5)} 
| '!=' {semantica.addPilaOp(6)};
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
exp : termino{
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
} (sum_rest termino{
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
})*;
sum_rest      : 
'+' {semantica.addPilaOp(0)}
| '-' {semantica.addPilaOp(1)};
///////////////////////////////////////////////////////////

x : factor (mult_div factor)*;

///////////////////////////////////////////////////////////
termino : factor{
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
} (mult_div factor{
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
})*;
mult_div    : 
'*' {semantica.addPilaOp(2);}
| '/' {semantica.addPilaOp(3)};
///////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
factor  : '(' {
semantica.addPilaOp(-1) # meter barrera
} expresion ')' {
semantica.pilaOperadores.pop() # sacar barrera
}
| positivo_negativo id_cte {
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
}
| id_cte;

positivo_negativo: 
'+' {#semantica.convertirMenos = False} 
| '-' {
#semantica.convertirMenos = True

try:
    semantica.addCTE(-1,"int") # agregamos -1 si no existe
except ValueError as e:
    print(e)
    sys.exit()
semantica.addPilaOp(2) # agregamos *
semantica.addPilaVar(-1) # agregar -1 a pila de variables
};

id_cte: ID{
try:
    semantica.addPilaVar($ID.text)
except ValueError as e:
    print(e)
    sys.exit()
} | cte;

cte: 
CTE_INT {
try:
    semantica.addCTE($CTE_INT.text, 'int')
except ValueError as e:
    print(e)
    sys.exit()
try:
    semantica.addPilaVar($CTE_INT.text)
except ValueError as e:
    print(e)
    sys.exit()
}
| CTE_FLOAT {
try:
    semantica.addCTE($CTE_FLOAT.text, 'float')
except ValueError as e:
    print(e)
    sys.exit()
try:
    semantica.addPilaVar($CTE_FLOAT.text)
except ValueError as e:
    print(e)
    sys.exit()
};
//////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////
funcs       : 'void' {semantica.currType = 'void'} 
ID {try: 
    semantica.addFunc($ID.text, semantica.currType) 
    semantica.currFunc = $ID.text
except ValueError as e: 
    print(e)
    sys.exit()
}
'(' params ')' '[' var_no_var body ']' ';' {semantica.delDV(semantica.currFunc)};

params: (list_params)?;
list_params: (ID {semantica.currID = $ID.text}
':' TYPE
{
try: 
    semantica.addVar(semantica.currID, $TYPE.text, semantica.currFunc) 
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
