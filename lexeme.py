from dataclasses import dataclass

class Types:
    NUMBER = 0
    INTEGER = 1
    FLOAT = 2
    STRING = 3
    IDENTIFIER = 4
    BADD = 5
    BSUB = 6
    USUB = 7
    BMUL = 8
    BDIV = 9
    BAND = 10
    BOR = 11
    UNEG = 12
    EXPRESSIONTERMINATOR = 13
    NEWLINE = 14
    SUB = 15
    LPAREN = 16
    RPAREN = 17
    LTRUE = 18
    LFALSE = 19
    ASSIGNMENT = 20
    EQUALITY = 21
    WALRUS = 22
    OPERATOR = 23
    VALUE = 24
    CONTROL = 25
    NOTEQUAL = 26
    UNARYNEGATION = 27

@dataclass
class Lexeme:
    value: str
    type: Types
    supertype: Types
    precedence: int

    def __repr__(self):
        return self.value