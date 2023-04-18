from lexeme import Lexeme
from lexeme import Types


def srcLex(line):
    lexemes = []
    buffer = []
    position = 0
    positionMax = len(line)

    while position < positionMax:
        character = line[position]

        if character == ";":
            lexemes.append(Lexeme(";", Types.EXPRESSIONTERMINATOR, Types.CONTROL, 0))
            position += 1
        elif character.isdigit():
            start = position
            end = position
            while end < positionMax and (line[end].isdigit() or line[end] == "."):
                end = end + 1
            token = line[start:end]
            lexemes.append(Lexeme(token, Types.NUMBER, Types.VALUE, 0))
            position = end
        elif character.isalpha():
            start = position
            end = position
            while end < positionMax and (line[end].isalnum()):
                end = end + 1
            token = line[start:end]

            # Check for identities
            if token == "false" or token == "False":
                lexemes.append(Lexeme(token, Types.LFALSE, Types.VALUE, 0))
            elif token == "true" or token == "True":
                lexemes.append(Lexeme(token, Types.LTRUE, Types.VALUE, 0))
            else:
                lexemes.append(Lexeme(token, Types.IDENTIFIER, Types.VALUE, 0))
            position = end
        elif character == "\"":
            start = position
            end = position + 1
            while line[end] != "\"":
                end = end + 1
            end +=1             # account for the "
            token = line[start:end]
            lexemes.append(Lexeme(token, Types.STRING, Types.VALUE, 0))
            position = end + 1
        elif character == "(":
            lexemes.append(Lexeme("(", Types.LPAREN, Types.CONTROL, 0))
            position += 1
        elif character == ")":
            lexemes.append(Lexeme(")", Types.RPAREN, Types.CONTROL, 0))
            position += 1
        elif character == "+":
            lexemes.append(Lexeme("+", Types.BADD, Types.OPERATOR, 10))
            position += 1
        elif character == "-":
            if lexemes[-1].supertype == Types.OPERATOR:
                lexemes.append(Lexeme("-", Types.UNEG, Types.OPERATOR, 50))
            else:
                lexemes.append(Lexeme("-", Types.BSUB, Types.OPERATOR, 10))
            position += 1
        elif character == "*":
            lexemes.append(Lexeme("*", Types.BMUL, Types.OPERATOR, 20))
            position += 1
        elif character == "/":
            lexemes.append(Lexeme("/", Types.BDIV, Types.OPERATOR, 20))
            position += 1
        elif character == "&":
            lexemes.append(Lexeme("&", Types.BAND, Types.OPERATOR, 5))
            position += 1
        elif character == "|":
            lexemes.append(Lexeme("|", Types.BOR, Types.OPERATOR, 5))
            position += 1
        elif character == "~":
            lexemes.append(Lexeme("~", Types.UNEG, Types.OPERATOR, 2))
            position += 1
        elif character == "=":
            start = position
            end = position
            while end < positionMax and (line[end] == "="):
                end = end + 1
            token = line[start:end]
            if token == "=":
                lexemes.append(Lexeme("=", Types.ASSIGNMENT, Types.OPERATOR, 0))
                position += 1
            elif token == "==":
                lexemes.append(Lexeme("==", Types.EQUALITY, Types.OPERATOR, 1))
                position = end + 1
        elif character == ":":
            start = position
            end = position
            while end < positionMax and (line[end] == "="):
                end = end + 1
            token = line[start:end]
            if token == ":":
                pass
            elif token == ":=":
                lexemes.append(Lexeme(":=", Types.WALRUS, Types.OPERATOR, 0))
            position += 1
        elif character == "!":
            start = position
            end = position + 1
            if end < positionMax and (line[end] == "="):
                lexemes.append(Lexeme("!=", Types.NOTEQUAL, Types.OPERATOR, 1))
                position += 2
            else:
                lexemes.append(Lexeme("!", Types.UNARYNEGATION, Types.OPERATOR, 1))
                position += 1
        else:
            position = position + 1

    return lexemes