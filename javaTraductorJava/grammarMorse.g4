grammar grammarMorse;

// Lexer rules
PRINT: 'print';
DEF: 'def';
RETURN: 'return';
LPAREN: '(';
RPAREN: ')';
COLON: ':';
COMMA: ',';
STAR: '*';
MINUS: '-';
EQUALS: '=';
WS: [ \t\r\n]+ -> skip;
NUMBER: [0-9]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' .*? '"' | '\'' .*? '\'';

// Parser rules
morse_line: statement+;
statement: func_def | print_stmt | return_stmt | assign_stmt;
func_def: DEF ID LPAREN param_list RPAREN COLON block;
print_stmt: PRINT LPAREN expression RPAREN;
return_stmt: RETURN expression;
assign_stmt: ID EQUALS expression;  // Asignación
param_list: (ID (COMMA ID)*)?;
block: '{' statement+ '}';
expression: primary (expr_op primary)*;
primary: ID | NUMBER | STRING | func_call;
func_call: ID LPAREN (expression (COMMA expression)*)? RPAREN;
expr_op: STAR | MINUS;
