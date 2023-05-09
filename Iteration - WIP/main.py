import operators
import parser
import lexxer
import interpreter
from lexeme import Lexeme
from lexeme import Types
from variable import variable
from dataclasses import dataclass
from naryTree import node
from naryTree import ifNode


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


@dataclass
class rpnLine:
    lineNo: int
    lexemes: list

def immediateResolve(line):
    controlCharacterSplit = line.split(" :=: ")
    # Error case: a test line must have a result and an expression to be valid
    if len(controlCharacterSplit) == 1:
        print(Bcolors.WARNING + f"An error has occurred: {controlCharacterSplit[0]}" + Bcolors.ENDC, end="")
    else:
        lexemes = lexxer.srcLex(controlCharacterSplit[1])
        print(lexemes)
        rpn = parser.shuntingYardParser(lexemes)
        print(rpn)
        result = interpreter.evaluate(rpn)
        if controlCharacterSplit[0] == str(result):
            print(f"Success! --- {controlCharacterSplit[0]}")
        else:
            print(f"Failed --- {controlCharacterSplit[0]}")

def delayedResolve(line):
    lexemes = lexxer.srcLex(line)
    rpn = parser.shuntingYardParser(lexemes)
    return rpn

def generateAST(program: list):
    rootNode = node("Root")
    currentNode = rootNode
    parsingIF = 0
    parsingWhile = 0

    for i in range(0, len(program)):
        if program[i].lexemes[0].supertype == Types.KEYWORD:
            if program[i].lexemes[0].type == Types.IF:
                # condition statement
                parsingIF = parsingIF + 1
                IFNode = ifNode(program[i].lexemes[1:])
                IFNode.branch = "left"
                IFNode.parent = currentNode
                if isinstance(currentNode, ifNode):
                    if currentNode.branch == "left":
                        currentNode.left.append(IFNode)
                    else:
                        currentNode.right.append(IFNode)
                else:
                    currentNode.nodes.append(IFNode)
                currentNode = IFNode
            elif program[i].lexemes[0].type == Types.ELSE:
                if isinstance(currentNode, ifNode):
                    currentNode.branch = "right"
            elif program[i].lexemes[0].type == Types.ENDIF:
                parsingIF = parsingIF - 1
                currentNode = currentNode.parent
        else:
            if isinstance(currentNode, ifNode):
                if currentNode.branch == "left":
                    currentNode.left.append(parser.RPNToAST(program[i].lexemes))
                else:
                    currentNode.right.append(parser.RPNToAST(program[i].lexemes))
            elif type(currentNode) == "<class \'naryTree.whileNode\'>":
                pass
            else:
                currentNode.nodes.append(parser.RPNToAST(program[i].lexemes))

    return rootNode

def readSourceFile(filepath):
    file = open(filepath, "r")
    lines = file.readlines()

    # Generate list of lines
    program = []
    lineCount = 0

    for line in lines:
        # If the line is blank, skip it:
        if line[0] == "\n":
            pass
        # If the line is a source code only comment, display it, then remove
        elif line[0] == "[":
            print(Bcolors.HEADER + f"{line[1:-2]}" + Bcolors.ENDC)
        else:
            # Line is a test line, resolve immediately and interpret: <result> :=: <expression>
            if " :=: " in line:
                immediateResolve(line)
            else:
                program.append(rpnLine(lineCount, delayedResolve(line)))
                lineCount = lineCount + 1

    if len(program) > 0:
        ast = generateAST(program)
        # Program is now a simple AST of RPN sequences, we evaluate left to right from root node
        for line in program:
            print(line)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #readSourceFile('test.src')
    readSourceFile('program.src')
