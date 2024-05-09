//antlr4-parse Expr.g4 prog -gui PARA VER EL ARBOL COMO UI
//antlr4-parse Expr.g4 prog -tree CONSEGUIMOS EL PARSER EN UN TREE
//antlr4-parse Expr.g4 prog -tokens -trace PARA VER COMO SE CONSIGUEN LOS TOKENS Y TRACE POR EL PROCESO

grammar Expr;		
prog:	expr EOF ;
expr:	expr ('*'|'/') expr
    |	expr ('+'|'-') expr
    |	INT
    |	'(' expr ')'
    ;
NEWLINE : [\r\n]+ -> skip;
INT     : [0-9]+ ;