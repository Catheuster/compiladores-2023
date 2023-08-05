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

def verifyID(self, identifier):
    if not self._symbolTable.exists(identifier):
        raise IsiSemanticException.IsiSemanticException("Símbolo '" + identifier + "' não declarado.\n")

def verifyType(self, identifier, type):
    self._symbol = self._symbolTable.get(identifier)
    if self._symbol.getType() != type:
        raise IsiSemanticException.IsiSemanticException("Símbolo '" + identifier + "' tem um tipo incompatível!\n")

def exibeComandos(self):
    for command in self._program.getCommands():
        print(command)

def generateCode(self, choice=1):
    self._program.generateTarget(choice)
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

                   (algExpr|boolExpr|strExpr) DOT

{self.verifyType(self._identifier, self._type)
self._cmd = CommandAssign.CommandAssign(self._identifier, self._exprContent)
self._stack[-1].append(self._cmd)}

                   ;

cmdIf: 'se' LP 
{self._exprContent = ""}
                boolExpr
{localExprCondition = self._exprContent}

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
                              boolExpr
{localwhileCondition = self._exprContent} 
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
                            boolExpr
{localdoWhileCondition = self._exprContent}

                                                RP

{self._doWhileList = self._stack.pop()
self._cmd = CommandDoWhile.CommandDoWhile(localdoWhileCondition, self._doWhileList)
self._stack[-1].append(self._cmd)}

                                                                        DOT ;

algExpr:	algTerm (AOP

{self._exprContent += self._input.LT(-1).text}

                   algTerm)* ;

boolExpr:   boolTerm (BOP

{self._exprContent += self._input.LT(-1).text
print(self._exprContent)}

                    boolTerm)*
                    | LP

{self._exprContent += '('}

                        boolExpr RP

{self._exprContent += ')'};

strExpr: strTerm;

boolTerm: (ID 

{self.verifyID(self._input.LT(-1).text)
self._exprContent += self._input.LT(-1).text
self.verifyType(self._input.LT(-1).text, IsiVariable.IsiVariable.BOOL)
}
            | BOOL 

{self._exprContent += self._input.LT(-1).text
self._type = IsiVariable.IsiVariable.BOOL}

                | algExpr 

                    ROP 

{self._exprContent += self._input.LT(-1).text}

                        algExpr)

{self._type = IsiVariable.IsiVariable.BOOL};

algTerm: (ID

{self.verifyID(self._input.LT(-1).text)
self._exprContent += self._input.LT(-1).text
self.verifyType(self._input.LT(-1).text, IsiVariable.IsiVariable.NUMBER)}

          | NUM

{self._type = IsiVariable.IsiVariable.NUMBER
self._exprContent += self._input.LT(-1).text}
            | LP

{self._exprContent += '('}

                algExpr RP

{self._exprContent += ')'})

{self._type = IsiVariable.IsiVariable.NUMBER};

strTerm: (ID
{self.verifyID(self._input.LT(-1).text)
self._exprContent += self._input.LT(-1).text
self.verifyType(self._input.LT(-1).text, IsiVariable.IsiVariable.TEXT)}
            | TEXT
            {self._exprContent += self._input.LT(-1).text})

{self._type = IsiVariable.IsiVariable.TEXT};

BOOL: 'verdadeiro' | 'falso' ;

ID: [a-z] ([a-z] | [A-Z] | [0-9])* ;

TEXT: '"' ([a-z] | [A-Z] | [0-9] | ' ')+ '"' ;

NUM: [0-9]+ ('.' [0-9])? ;

ASGN: ':=' ;

ROP: '<' | '>' | '<=' | '>=' | '!=' | '==' ;

AOP: '+' | '-' | '*' | '/' ;

BOP : '&&'| '||';

DOT: '.' ;

COMMA: ',' ;

LP: '(' ;

RP: ')' ;

LC: '{' ;

RC: '}' ;

WS:	(' ' | '\t' | '\n' | '\r') -> skip ;
