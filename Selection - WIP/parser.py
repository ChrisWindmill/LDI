from lexeme import Lexeme
from lexeme import Types
from naryTree import node
import operators
import variable

def shuntingYardParser(lexemes):
    rpn = []
    operatorStack = []

    if lexemes[0].supertype == Types.KEYWORD:
        # Keywords as the first lexeme on a line generate a different pathway to other statements
        if len(lexemes) > 1:
            rpn = shuntingYardParser(lexemes[1:])
        rpn.insert(0, lexemes[0])
    else:
        for token in lexemes:
            if token.supertype == Types.VALUE:
                rpn.append(token)
            elif token.supertype == Types.IDENTIFIER:
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


def RPNToAST(rpn):
    nodeList = []

    for token in rpn:
        if token.supertype == Types.KEYWORD:
            pass
        elif token.supertype == Types.VALUE or \
             token.supertype == Types.IDENTIFIER:
            nodeList.append(node(token))
        elif token.supertype == Types.OPERATOR:
            currentNode = node(token)
            if operators.isBinaryOperator(token.type):
                currentNode.nodes.insert(0, nodeList.pop())
                currentNode.nodes.insert(0, nodeList.pop())
            else:
                currentNode.nodes.insert(0, nodeList.pop())
            for childNode in currentNode.nodes:
                childNode.parent = currentNode
            nodeList.append(currentNode)

    return nodeList.pop()

