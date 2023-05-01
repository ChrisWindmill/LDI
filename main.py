import operators
import parser
import lexxer
import interpreter
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
                    # Perform parsing (create RPN version of lines):
                    rpn = parser.shuntingYardParser(lexemes)
                    print(rpn)
                    # Interpret the line of code
                    result = interpreter.evaluate(rpn)

                    # Determine if the return value matches the expected test result
                    if controlCharacterSplit[0] == str(result):
                        print(f"Success! --- {controlCharacterSplit[0]}")
                    else:
                        print(f"Failed --- {controlCharacterSplit[0]}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readSourceFile('test.src')
