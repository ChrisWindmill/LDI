from dataclasses import dataclass

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

@dataclass
class Lexeme:
    value: str
    type: Types
    supertype: Types
    precedence: int

    def __repr__(self):
        return self.value

def evaluate(rpn):
    result = None
    stack = []
    type = None

    for token in rpn:
        if token.supertype == Types.VALUE:
            stack.append(token)
        elif token.supertype == Types.OPERATOR:
            if token.type == Types.BADD:
                rhs = stack.pop()
                lhs = stack.pop()

                # Determine if ints:
                try:
                    rhs = int(rhs.value)
                    lhs = int(lhs.value)
                    type = "int"
                except ValueError:
                    try:
                        rhs = float(rhs.value)
                        lhs = float(lhs.value)
                        type = "float"
                    except ValueError:
                        if lhs.type == Types.STRING and rhs.type == Types.STRING:
                            type = "string"

                if type == "int":
                    result = rhs + lhs
                    stack.append(result)
                elif type == "float":
                    result = lhs + rhs
                    stack.append(result)
                elif type == "string":
                    result = lhs.value[1:-1] + rhs.value[1:-1]
                    stack.append(result)
                else:
                    stack.append("ERROR")
        else:
            pass
    result = stack.pop()
    return result

def shuntingYard(lexemes):
    rpn = []
    operatorStack = []

    for token in lexemes:
        if token.supertype == Types.VALUE:
            rpn.append(token)
        elif token.supertype == Types.OPERATOR:
            if len(operatorStack) > 0:
                topOperator = operatorStack[-1]
                if topOperator.type != Types.LPAREN:
                    if token.precedence <= topOperator.precedence:
                        rpn.append(operatorStack.pop())
                operatorStack.append(token)
            else:
                operatorStack.append(token)
        elif token.type == Types.LPAREN:
            operatorStack.append(token)
        elif token.type == Types.RPAREN:
            while len(operatorStack) > 0:
                topOperator = operatorStack[-1]
                if topOperator.type != Types.LPAREN:
                    rpn.append(operatorStack.pop())
                else:
                    operatorStack.pop() # remove left paren
                    break
    while len(operatorStack) > 0:
        rpn.append(operatorStack.pop())
    return rpn


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
            if token == "false":
                lexemes.append(Lexeme(token, Types.LFALSE, Types.VALUE, 0))
            elif token == "true":
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
            lexemes.append(Lexeme("-", Types.SUB, Types.OPERATOR, 10))
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
            elif token == "==":
                lexemes.append(Lexeme("=", Types.EQUALITY, Types.OPERATOR, 1))
            position += 1
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
        else:
            position = position + 1

    return lexemes

def readSourceFile(filepath):
    file = open(filepath, "r")
    lines = file.readlines()

    # count = 0
    # for line in lines:
    #     count += 1
    #     print(f"{count:03}: {line}", end="")

    for line in lines:
        if line[0] != '\n':
            if line[0] == "[":          # Handle comments in file
                print(Bcolors.HEADER + f"{line[1:-2]}" + Bcolors.ENDC)
            else:
                controlCharacterSplit = line.split(" :=: ")
                if len(controlCharacterSplit) == 1:             # An error has occurred, not a valid test
                    print(Bcolors.WARNING + f"An error has occurred: {controlCharacterSplit[0]}" + Bcolors.ENDC, end ="")
                else:
                    # Perform lexing:
                    lexemes = srcLex(controlCharacterSplit[1])
                    print(lexemes)
                    rpn = shuntingYard(lexemes)
                    print(rpn)
                    result = evaluate(rpn)
                    if controlCharacterSplit[0] == str(result):
                        print("Success!")
                    else:
                        print("Failed")
                    #print(bcolors.OKGREEN + f"{controlCharacterSplit[0]}" + bcolors.ENDC)
                    #print(bcolors.OKBLUE + f"{controlCharacterSplit[1]}" + bcolors.ENDC)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readSourceFile('shortTest.src')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
