grammar gramatica;

programa : 'start' (dclr | cmd)+ 'stop;';

dclr : tipo ID (VG ID)* PV;

tipo : 'Int' | 'Real' | 'Logic';

cmd : atrbcmd | showcmd | readcmd;

showcmd: 'echo' AP (ID | TEXT)+ FP PV;
readcmd: 'take' AP (TEXT VG)? ID FP PV;

atrbcmd: ID atrbcmdL;
atrbcmdL: '=' expr;

expr: (ID | NUM | TEXT) exprL* PV;
exprL: OP (ID | NUM | TEXT);

ID : [a-z] ([a-z]|[A-Z]|[0-9])*;
VG : ',';
PV : ';';
AP : '(';
FP : ')';
TEXT : '"' ([a-z]|[A-Z]|[0-9]|' '|'\n'|'\t'|':'|'?'|','|'.'|';'|'!')* '"';
NUM : [0-9]+ (',' [0-9]+)?;
OP : SUM | SUB | MUL | DIV | CONCAT;
SUM : '+';
SUB : '-';
MUL : '*';
DIV : '/';
CONCAT : '++';

BLANK     : (' '| '\t' | '\n' | '\r') -> skip;