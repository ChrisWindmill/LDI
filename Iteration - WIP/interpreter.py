import operators
from lexeme import Types
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
