grammar IsiLanguage;

@header{
from ..ast import AbstractCommand
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
from ..exceptions import IsiSemanticException
}

@members{
    self._type = None
    self._identifier = None
    self._value = None
    self._symbolTable = IsiSymbolTable.IsiSymbolTable()
    self._symbol = IsiSymbol.IsiSymbol
    self._program = IsiProgram.IsiProgram()
    self._readID = None
    self._writeID = None
    self._exprID = None
    self._exprContent = None
    self._stack = []
    self._unusedVariables = []
    self._initializedVariables = []
    self._exprCondition = None
    self._trueList = []
    self._falseList = []
    self._expr_stack = []
    self._typetable = ['numero','texto','booleano']

def verifyID(self, identifier):
    if not self._symbolTable.exists(identifier):
        raise IsiSemanticException.IsiSemanticException("Símbolo '" + identifier + "' não declarado.\n")

def verifyType(self, identifier, type):
    self._symbol = self._symbolTable.get(identifier)
    if self._symbol.getType() != type:
        raise IsiSemanticException.IsiSemanticException("Símbolo '" + identifier + "' e incompativel com o tipo " + self._typetable[type] + "\n")

def exibeComandos(self):
    for command in self._program.getCommands():
        print(command)

def generateCode(self, choice=1):
    self._program.generateTarget(choice)

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
    print('inicio')
    print(self._expr_stack)
    right_param = self._expr_stack.pop()
    op = self._expr_stack.pop()
    left_param = self._expr_stack.pop()

    match op:
        case 'AOP':
            if (right_param != IsiVariable.IsiVariable.NUMBER) or (left_param != IsiVariable.IsiVariable.NUMBER):
                raise IsiSemanticException.IsiSemanticException('Opercao invalida')
            self._expr_stack.append(IsiVariable.IsiVariable.NUMBER)
        case 'ROP':
            if (right_param != 0) or (left_param != 0):
                raise IsiSemanticException.IsiSemanticException('Opercao invalida')
            self._expr_stack.append(IsiVariable.IsiVariable.BOOL)
        case 'BOP':
            if (right_param != IsiVariable.IsiVariable.BOOL) or (left_param != IsiVariable.IsiVariable.BOOL):
                raise IsiSemanticException.IsiSemanticException('Opercao invalida')
            self._expr_stack.append(IsiVariable.IsiVariable.BOOL)
        case 'SOP':
            if (right_param != IsiVariable.IsiVariable.TEXT) or (left_param != IsiVariable.IsiVariable.TEXT):
                raise IsiSemanticException.IsiSemanticException('Opercao invalida')
            self._expr_stack.append(IsiVariable.IsiVariable.TEXT)
    print('fim')
    print(self._expr_stack)
}

prog: 'programa' (declaration | block)+ 'fimprog.'

{self._program.setVariableTable(self._symbolTable)
self._program.setCommands(self._stack.pop())
if self._unusedVariables:
    print(f"Warning: Variáveis declaradas, mas não usadas. {self._unusedVariables}\n")}
                                                   ;

declaration: tipo ID

{self._identifier = self._input.LT(-1).text;
self._value = None
self._symbol = IsiVariable.IsiVariable(self._identifier, self._type, self._value)
if not self._symbolTable.exists(self._identifier):
    self._symbolTable.add(self._symbol)
    self._unusedVariables.append(self._identifier)
    print(f"Símbolo adicionado: {self._symbol}")
else:
    raise IsiSemanticException.IsiSemanticException("Símbolo '" + self._identifier + "' já declarado.\n")}

                              (COMMA ID

{self._identifier = self._input.LT(-1).text;
self._value = None
self._symbol = IsiVariable.IsiVariable(self._identifier, self._type, self._value)
if not self._symbolTable.exists(self._identifier):
    self._symbolTable.add(self._symbol)
    self._unusedVariables.append(self._identifier)
    print(f"Símbolo adicionado: {self._symbol}")
else:
    raise IsiSemanticException.IsiSemanticException("Símbolo '" + self._identifier + "' já declarado.\n")}

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
if self._readID in self._unusedVariables:
    self._unusedVariables.remove(self._readID)
if self._readID not in self._initializedVariables:
    self._initializedVariables.append(self._readID)}

                      RP DOT

{self._value = self._symbolTable.get(self._readID)
self._cmd = CommandRead.CommandRead(self._readID, self._value)
self._stack[-1].append(self._cmd)}

                             ;

cmdWrite: 'escreva' LP (TEXT

{self._writeInput = self._input.LT(-1).text}

                             | ID

{self.verifyID(self._input.LT(-1).text)
self._writeInput = self._input.LT(-1).text
if self._writeInput not in self._initializedVariables:
    raise IsiSemanticException.IsiSemanticException("Símbolo '" + self._writeInput + "' não inicializado.\n")}

                                  ) RP DOT

{self._cmd = CommandWrite.CommandWrite(self._writeInput)
self._stack[-1].append(self._cmd)}

                                           ;

cmdAssign: ID

{self._identifier = self._input.LT(-1).text
self.verifyID(self._identifier)
if self._identifier in self._unusedVariables:
    self._unusedVariables.remove(self._identifier)
if self._identifier not in self._initializedVariables:
    self._initializedVariables.append(self._identifier)}

              ASGN

{self._exprContent = ""}

                   (expr) DOT

{self.verifyType(self._identifier, self._type)
self._cmd = CommandAssign.CommandAssign(self._identifier, self._exprContent)
self._stack[-1].append(self._cmd)}

                   ;

cmdIf: 'se' LP 
{self._exprContent = ""}
                expr
{
if self._type != IsiVariable.IsiVariable.BOOL:
    raise IsiSemanticException.IsiSemanticException("expressao deve ser do tipo booleano")
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
    raise IsiSemanticException.IsiSemanticException("expressao deve ser do tipo booleano")
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
    raise IsiSemanticException.IsiSemanticException("expressao deve retornar um booleano")
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
self._symbol = self._symbolTable.get(self._input.LT(-1).text)
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

TEXT: '"' ([a-z] | [A-Z] | [0-9] | ' ')+ '"' ;

NUM: [0-9]+ ('.' [0-9])? ;

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
