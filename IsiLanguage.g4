grammar IsiLanguage;

@header{
from ..ast import CommandRead
from ..ast import CommandWrite
from ..ast import CommandAssign
from ..ast import CommandIf
from ..ast import CommandWhile
from ..ast import CommandDoWhile
from ..ast import IsiProgram
from ..datastructures import IsiSymbol
from ..datastructures import IsiSymbolTable
from ..datastructures import IsiVariable
from ..exceptions import IsiException
}

@members{
    self._type = None
    self._identifier = None
    self._value = None
    self._symbol_table = IsiSymbolTable.IsiSymbolTable()
    self._symbol = IsiSymbol.IsiSymbol
    self._program = IsiProgram.IsiProgram()
    self._readID = None
    self._writeID = None
    self._exprID = None
    self._exprContent = None
    self._stack = []
    self._unused_variables = []
    self._initialized_variables = []
    self._expr_stack = []
    self._type_table = ['numero','texto','booleano']

def verifyID(self, identifier):
    if not self._symbol_table.exists(identifier):
        raise IsiException.IsiSemanticException("Símbolo '" + identifier + "' não declarado.\n")

def verifyType(self, identifier, type):
    self._symbol = self._symbol_table.get(identifier)
    if self._symbol.getType() != type:
        raise IsiException.IsiSemanticException("Símbolo '" + identifier + "' e incompativel com o tipo " + self._type_table[type] + "\n")

def exibeComandos(self):
    for command in self._program.getCommands():
        print(command)

def generateCode(self, choice=1):
    return self._program.generateTarget(choice)

def stack_op(self,op):
    if op in ['<', '>', '<=', '>=', '!=', '==']:
        self._expr_stack.append("ROP")
    elif op in ['+', '-', '*', '/']:
        self._expr_stack.append("AOP")
    elif op in ['&&', '||']:
        self._expr_stack.append("BOP")
    elif op in ['++']:
        self._expr_stack.append("SOP")

def verify_stack(self):
    right_param = self._expr_stack.pop()
    op = self._expr_stack.pop()
    left_param = self._expr_stack.pop()

    match op:
        case 'AOP':
            if (right_param != IsiVariable.IsiVariable.NUMBER) or (left_param != IsiVariable.IsiVariable.NUMBER):
                raise IsiException.IsiSemanticException('Opercao invalida')
            self._expr_stack.append(IsiVariable.IsiVariable.NUMBER)
        case 'ROP':
            if (right_param != 0) or (left_param != 0):
                raise IsiException.IsiSemanticException('Opercao invalida')
            self._expr_stack.append(IsiVariable.IsiVariable.BOOL)
        case 'BOP':
            if (right_param != IsiVariable.IsiVariable.BOOL) or (left_param != IsiVariable.IsiVariable.BOOL):
                raise IsiException.IsiSemanticException('Opercao invalida')
            self._expr_stack.append(IsiVariable.IsiVariable.BOOL)
        case 'SOP':
            if (right_param != IsiVariable.IsiVariable.TEXT) or (left_param != IsiVariable.IsiVariable.TEXT):
                raise IsiException.IsiSemanticException('Opercao invalida')
            self._expr_stack.append(IsiVariable.IsiVariable.TEXT)
        case _:
            raise IsiException.IsiSemanticException('Erro inesperado')
}

prog: 'programa' (declaration | block)+ 'fimprog.'

{self._program.setVariableTable(self._symbol_table)
self._program.setCommands(self._stack.pop())
if self._unused_variables:
    print(f"Warning: Variáveis declaradas, mas não usadas. {self._unused_variables}\n")}
                                                   ;

declaration: tipo ID

{self._identifier = self._input.LT(-1).text;
self._value = None
self._symbol = IsiVariable.IsiVariable(self._identifier, self._type, self._value)
if not self._symbol_table.exists(self._identifier):
    self._symbol_table.add(self._symbol)
    self._unused_variables.append(self._identifier)
    print(f"Símbolo adicionado: {self._symbol}")
else:
    raise IsiException.IsiSemanticException("Símbolo '" + self._identifier + "' já declarado.\n")}

                              (COMMA ID

{self._identifier = self._input.LT(-1).text;
self._value = None
self._symbol = IsiVariable.IsiVariable(self._identifier, self._type, self._value)
if not self._symbol_table.exists(self._identifier):
    self._symbol_table.add(self._symbol)
    self._unused_variables.append(self._identifier)
    print(f"Símbolo adicionado: {self._symbol}")
else:
    raise IsiException.IsiSemanticException("Símbolo '" + self._identifier + "' já declarado.\n")}

                                        )* DOT ;

tipo: 'numero'

    {self._type = IsiVariable.IsiVariable.NUMBER}

    | 'texto'

    {self._type = IsiVariable.IsiVariable.TEXT}

    | 'booleano'

    {self._type = IsiVariable.IsiVariable.BOOL}

                                     ;

block:

{self._currentThread = []
self._stack.append(self._currentThread)}

        (cmd)+ ;

cmd: cmdRead | cmdWrite | cmdAssign | cmdIf | cmdWhile | cmdDoWhile;

cmdRead: 'leia' LP ID

{self.verifyID(self._input.LT(-1).text)
self._readID = self._input.LT(-1).text
if self._readID in self._unused_variables:
    self._unused_variables.remove(self._readID)
if self._readID not in self._initialized_variables:
    self._initialized_variables.append(self._readID)}

                      RP DOT

{self._value = self._symbol_table.get(self._readID)
self._cmd = CommandRead.CommandRead(self._readID, self._value)
self._stack[-1].append(self._cmd)}

                             ;

cmdWrite: 'escreva' LP (TEXT

{self._writeInput = self._input.LT(-1).text}

                             | ID

{self.verifyID(self._input.LT(-1).text)
self._writeInput = self._input.LT(-1).text
if self._writeInput not in self._initialized_variables:
    raise IsiException.IsiSemanticException("Símbolo '" + self._writeInput + "' não inicializado.\n")}

                                  ) RP DOT

{self._cmd = CommandWrite.CommandWrite(self._writeInput)
self._stack[-1].append(self._cmd)}

                                           ;

cmdAssign: ID

{self._identifier = self._input.LT(-1).text
self.verifyID(self._identifier)
if self._identifier in self._unused_variables:
    self._unused_variables.remove(self._identifier)
if self._identifier not in self._initialized_variables:
    self._initialized_variables.append(self._identifier)}

              ASGN

{self._exprContent = ""}

                   expr DOT

{self.verifyType(self._identifier, self._type)
self._cmd = CommandAssign.CommandAssign(self._identifier, self._exprContent)
self._stack[-1].append(self._cmd)}

                   ;

cmdIf: 'se' LP 
{self._exprContent = ""}
                expr
{
if self._type != IsiVariable.IsiVariable.BOOL:
    raise IsiException.IsiSemanticException("expressao deve ser do tipo booleano")
localExprCondition = self._exprContent}

                              RP 'entao' LC

{self._currentThread = []
self._stack.append(self._currentThread)}

                                            (cmd)+ RC

{localTrueList = self._stack.pop()
localFalseList = []}

                                                      ('senao' LC

{self._currentThread = []
self._stack.append(self._currentThread)}
                                                                  (cmd)+ RC

{localFalseList = self._stack.pop()}

                                                                           )?

{self._cmd = CommandIf.CommandIf(localExprCondition, localTrueList, localFalseList)
self._stack[-1].append(self._cmd)}

                                                                              ;

cmdWhile: 'enquanto' LP 
{self._exprContent=""}
                              expr
{
if self._type != IsiVariable.IsiVariable.BOOL:
    raise IsiException.IsiSemanticException("expressao deve ser do tipo booleano")
localwhileCondition = self._exprContent} 
                                RP LC

{self._currentThread = []
self._stack.append(self._currentThread)}

                                                       (cmd)+ RC

{self._whileList = self._stack.pop()
self._cmd = CommandWhile.CommandWhile(localwhileCondition, self._whileList)
self._stack[-1].append(self._cmd)}

                                                                 ;

cmdDoWhile: 'faca' LC

{self._currentThread = []
self._stack.append(self._currentThread)}

                      (cmd)+ RC 'enquanto' LP 
{self._exprContent=""}
                            expr
{
if self._type != IsiVariable.IsiVariable.BOOL:
    raise IsiException.IsiSemanticException("expressao deve retornar um booleano")
localdoWhileCondition = self._exprContent
}

                                                RP

{self._doWhileList = self._stack.pop()
self._cmd = CommandDoWhile.CommandDoWhile(localdoWhileCondition, self._doWhileList)
self._stack[-1].append(self._cmd)}

                                                                        DOT ;

expr: term (OP 
{self._exprContent += self._input.LT(-1).text
self.stack_op(self._input.LT(-1).text)}
        term
{self.verify_stack()})*
{self._type = self._expr_stack.pop()};

term: 
    (
    ID      
{
self._symbol = self._symbol_table.get(self._input.LT(-1).text)
self.verifyID(self._input.LT(-1).text)
self._expr_stack.append(self._symbol.getType())
}
    |NUM    {self._expr_stack.append(IsiVariable.IsiVariable.NUMBER)}
    |BOOL   {self._expr_stack.append(IsiVariable.IsiVariable.BOOL)}
    |TEXT   {self._expr_stack.append(IsiVariable.IsiVariable.TEXT)}
){self._exprContent += self._input.LT(-1).text}
    |LP

{self._exprContent += '('}

        expr RP

{self._exprContent += ')'} {self._expr_stack.append(self._type)};

OP: AOP | BOP | ROP | SOP;

BOOL: 'verdadeiro' | 'falso' ;

ID: [a-z] ([a-z] | [A-Z] | [0-9])* ;

TEXT: '"' ([a-z] | [A-Z] | [0-9] | ' ' | ',' | '.' | ';' | '!' | '?')+ '"' ;

NUM: [0-9]+ ('.' [0-9]+)? ;

ASGN: ':=' ;

ROP: '<' | '>' | '<=' | '>=' | '!=' | '==';

AOP: '+' | '-' | '*' | '/' ;

BOP : '&&'| '||' ;

SOP : '++';

DOT: '.' ;

COMMA: ',' ;

LP: '(' ;

RP: ')' ;

LC: '{' ;

RC: '}' ;

WS:	(' ' | '\t' | '\n' | '\r') -> skip ;
