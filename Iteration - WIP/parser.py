from lexeme import Lexeme
from lexeme import Types
import variable

def shuntingYardParser(lexemes):
    rpn = []
    operatorStack = []

    # Our parser now really needs to deal with statements and expressions separately.
    # A statement is a line of code that does something but does not return a value
    # An expression is a line of code that can be reduced to a value
    if lexemes[0].supertype == Types.KEYWORD:
        # Keywords as the first lexeme on a line generate a different pathway to other statements
        pass
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
