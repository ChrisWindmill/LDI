import operators
import shuntingYard
import lexxer
from lexeme import Lexeme
from lexeme import Types
from variable import variable


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



def evaluate(rpn):
    result = None
    stack = []
    type = None

    for token in rpn:
        if token.supertype == Types.VALUE:
            # Determine number type if not already done
            if token.type == Types.NUMBER:
                if operators.isInt(token.value):
                    token.type = Types.INTEGER
                elif operators.isFloat(token.value):
                    token.type = Types.FLOAT
            elif token.type == Types.LTRUE or token.type == Types.LFALSE:
                pass
            else:
                token.type = Types.STRING
            stack.append(token)
        elif token.supertype == Types.IDENTIFIER:
            stack.append(token)
        elif token.supertype == Types.OPERATOR:
            if token.type == Types.BADD:
                operators.binaryAdd(stack)
            elif token.type == Types.BSUB:
                operators.binarySubtract(stack)
            elif token.type == Types.BMUL:
                operators.binaryMultiply(stack)
            elif token.type == Types.BDIV:
                operators.binaryDivision(stack)
            elif token.type == Types.BAND:
                operators.binaryAND(stack)
            elif token.type == Types.BOR:
                operators.binaryOR(stack)
            elif token.type == Types.ASSIGNMENT:
                operators.Assignment(stack)
            elif token.type == Types.EQUALITY:
                operators.binaryEquality(stack)
            elif token.type == Types.UNEG:
                operators.unaryNegation(stack)
            elif token.type == Types.NOTEQUAL:
                operators.binaryNotEqual(stack)
        else:
            pass
    result = stack.pop()
    return result

def readSourceFile(filepath):
    file = open(filepath, "r")
    lines = file.readlines()

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
                    lexemes = lexxer.srcLex(controlCharacterSplit[1])
                    print(lexemes)
                    rpn = shuntingYard.shuntingYard(lexemes)
                    print(rpn)
                    result = evaluate(rpn)
                    if controlCharacterSplit[0] == str(result):
                        print(f"Success! --- {controlCharacterSplit[0]}")
                    else:
                        print(f"Failed --- {controlCharacterSplit[0]}")
                    #print(bcolors.OKGREEN + f"{controlCharacterSplit[0]}" + bcolors.ENDC)
                    #print(bcolors.OKBLUE + f"{controlCharacterSplit[1]}" + bcolors.ENDC)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readSourceFile('test.src')
