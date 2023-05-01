from lexeme import Lexeme
from lexeme import Types
import variable

def shuntingYard(lexemes):
    rpn = []
    operatorStack = []

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
