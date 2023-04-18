from lexeme import Lexeme
from lexeme import Types

def isFloat (string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def isTrue(lexeme):
    logicalVal = False
    # Convert to logical values:
    if lexeme.type == Types.INTEGER:
        if int(lexeme.value) != 0:
            logicalVal = True
    elif lexeme.type == Types.FLOAT:
        if float(lexeme.value) != 0.0:
            logicalVal = True
    elif lexeme.type == Types.STRING:
        if lexeme.value != "":
            logicalVal = True
    elif lexeme.type == Types.LTRUE:
        logicalVal = True
    else:
        pass

    return logicalVal

def binaryAdd(stack):
    rhs = stack.pop()
    lhs = stack.pop()

    # Strictly Integer Case
    if lhs.type == Types.INTEGER and rhs.type == Types.INTEGER:
        result = int(rhs.value) + int(lhs.value)
        stack.append(Lexeme(str(result), Types.INTEGER, Types.VALUE, 0))
    # Strictly Float Case
    elif lhs.type == Types.FLOAT and rhs.type == Types.FLOAT:
        result = float(lhs.value) + float(rhs.value)
        stack.append(Lexeme(str(result), Types.FLOAT, Types.VALUE, 0))
    # Mixed Int Float Case: promote integer to float for calculations
    elif (lhs.type == Types.FLOAT and rhs.type == Types.INTEGER) or \
            (lhs.type == Types.INTEGER and rhs.type == Types.FLOAT):
        result = float(lhs.value) + float(rhs.value)
        stack.append(Lexeme(str(result), Types.FLOAT, Types.VALUE, 0))
    # Strictly String Case
    elif lhs.type == Types.STRING and rhs.type == Types.STRING:
        result = lhs.value[1:-1] + rhs.value[1:-1]
        stack.append(Lexeme(str(result), Types.STRING, Types.VALUE, 0))
    # Unknown case - treat values as strings and concatenate
    else:
        result = str(lhs.value)[1:-1] + str(rhs.value)[1:-1]
        stack.append(Lexeme(str(result), Types.STRING, Types.VALUE, 0))

def unaryNegation(stack):
    value = stack.pop()
    if value.type == Types.INTEGER:
        value.value = str(-int(value.value))
    elif value.type == Types.Float:
        value.value = str(-float(value.value))
    else:
        value.value = "Error"
        value.type = Types.STRING
    stack.append(value)

def binarySubtract(stack):
    rhs = stack.pop()
    lhs = stack.pop()

    # Strictly Integer Case
    if lhs.type == Types.INTEGER and rhs.type == Types.INTEGER:
        result = int(lhs.value) - int(rhs.value)
        stack.append(Lexeme(str(result), Types.INTEGER, Types.VALUE, 0))
    # Strictly Float Case
    elif lhs.type == Types.FLOAT and rhs.type == Types.FLOAT:
        result = float(lhs.value) - float(rhs.value)
        stack.append(Lexeme(str(result), Types.FLOAT, Types.VALUE, 0))
    # Mixed Int Float Case: promote integer to float for calculations
    elif (lhs.type == Types.FLOAT and rhs.type == Types.INTEGER) or \
            (lhs.type == Types.INTEGER and rhs.type == Types.FLOAT):
        result = float(lhs.value) - float(rhs.value)
        stack.append(Lexeme(str(result), Types.FLOAT, Types.VALUE, 0))
    else:
        result = "Error"
        stack.append(Lexeme(str(result), Types.STRING, Types.VALUE, 0))


def binaryMultiply(stack):
    rhs = stack.pop()
    lhs = stack.pop()

    # Strictly Integer Case
    if lhs.type == Types.INTEGER and rhs.type == Types.INTEGER:
        result = int(lhs.value) * int(rhs.value)
        stack.append(Lexeme(str(result), Types.INTEGER, Types.VALUE, 0))
    # Strictly Float Case
    elif lhs.type == Types.FLOAT and rhs.type == Types.FLOAT:
        result = float(lhs.value) * float(rhs.value)
        stack.append(Lexeme(str(result), Types.FLOAT, Types.VALUE, 0))
    # Mixed Int Float Case: promote integer to float for calculations
    elif (lhs.type == Types.FLOAT and rhs.type == Types.INTEGER) or \
            (lhs.type == Types.INTEGER and rhs.type == Types.FLOAT):
        result = float(lhs.value) * float(rhs.value)
        stack.append(Lexeme(str(result), Types.FLOAT, Types.VALUE, 0))
    else:
        result = "Error"
        stack.append(Lexeme(str(result), Types.STRING, Types.VALUE, 0))


def binaryDivision(stack):
    rhs = stack.pop()
    lhs = stack.pop()

    # Mixed Int Float Case: promote integer to float for calculations
    if (lhs.type == Types.FLOAT or lhs.type == Types.INTEGER) and \
            (rhs.type == Types.INTEGER or rhs.type == Types.FLOAT):
        result = float(lhs.value) / float(rhs.value)
        stack.append(Lexeme(str(result), Types.FLOAT, Types.VALUE, 0))
    else:
        result = "Error"
        stack.append(Lexeme(str(result), Types.STRING, Types.VALUE, 0))


def binaryAND(stack):
    rhs = stack.pop()
    lhs = stack.pop()

    logicalLHS = isTrue(lhs)
    logicalRHS = isTrue(rhs)

    result = logicalLHS and logicalRHS
    if result:
        stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
    else:
        stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))

def binaryOR(stack):
    rhs = stack.pop()
    lhs = stack.pop()

    logicalLHS = isTrue(lhs)
    logicalRHS = isTrue(rhs)

    result = logicalLHS or logicalRHS
    if result:
        stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
    else:
        stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))


def binaryNotEqual(stack):
    rhs = stack.pop()
    lhs = stack.pop()

    # Strictly String Case:
    if lhs.type == Types.STRING and rhs.type == Types.STRING:
        result = lhs.value != rhs.value
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
    # Strictly Integer Case:
    elif lhs.type == Types.INTEGER and rhs.type == Types.INTEGER:
        result = int(lhs.value) != int(lhs.value)
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
    # Strictly Float Case:
    elif lhs.type == Types.FLOAT and rhs.type == Types.FLOAT:
        result = float(lhs.value) != float(lhs.value)
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
    # Strictly Logical Case:
    elif (lhs.type == Types.LTRUE or lhs.type == Types.LFALSE) and \
            (rhs.type == Types.LTRUE or rhs.type == Types.LFALSE):
        result = rhs.type != lhs.type
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
    # Mixed Cases:
        # int float
    elif (lhs.type == Types.INTEGER or lhs.type == Types.FLOAT) and \
            (rhs.type == Types.INTEGER or rhs.type == Types.FLOAT):
        result = float(lhs.value) != float(lhs.value)
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
        # int string
    elif (lhs.type == Types.INTEGER or lhs.type == Types.STRING) and \
            (rhs.type == Types.STRING or rhs.type == Types.INTEGER):
        result = str(lhs.value) != str(lhs.value)
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
        # float string
    elif (lhs.type == Types.FLOAT or lhs.type == Types.STRING) and \
            (rhs.type == Types.STRING or rhs.type == Types.FLOAT):
        result = str(lhs.value) != str(lhs.value)
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
        # logical int
    elif (lhs.type == Types.INTEGER or lhs.type == Types.LTRUE or lhs.type == Types.LFALSE) and \
            (rhs.type == Types.INTEGER or rhs.type == Types.LTRUE or rhs.type == Types.LFALSE):
        result = not(isTrue(lhs)) or not(isTrue(rhs))
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
        # logical float
    elif (lhs.type == Types.FLOAT or lhs.type == Types.LTRUE or lhs.type == Types.LFALSE) and \
            (rhs.type == Types.FLOAT or rhs.type == Types.LTRUE or rhs.type == Types.LFALSE):
        result = not(isTrue(lhs)) or not(isTrue(rhs))
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
        # logical string
    elif (lhs.type == Types.STRING or lhs.type == Types.LTRUE or lhs.type == Types.LFALSE) and \
            (rhs.type == Types.STRING or rhs.type == Types.LTRUE or rhs.type == Types.LFALSE):
        result = not(isTrue(lhs)) or not(isTrue(rhs))
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))

def binaryEquality(stack):
    rhs = stack.pop()
    lhs = stack.pop()

    # Strictly String Case:
    if lhs.type == Types.STRING and rhs.type == Types.STRING:
        result = lhs.value == rhs.value
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
    # Strictly Integer Case:
    elif lhs.type == Types.INTEGER and rhs.type == Types.INTEGER:
        result = int(lhs.value) == int(lhs.value)
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
    # Strictly Float Case:
    elif lhs.type == Types.FLOAT and rhs.type == Types.FLOAT:
        result = float(lhs.value) == float(lhs.value)
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
    # Strictly Logical Case:
    elif (lhs.type == Types.LTRUE or lhs.type == Types.LFALSE) and \
            (rhs.type == Types.LTRUE or rhs.type == Types.LFALSE):
        result = rhs.type == lhs.type
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
    # Mixed Cases:
    # int float
    elif (lhs.type == Types.INTEGER or lhs.type == Types.FLOAT) and \
            (rhs.type == Types.INTEGER or rhs.type == Types.FLOAT):
        result = float(lhs.value) == float(lhs.value)
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
        # int string
    elif (lhs.type == Types.INTEGER or lhs.type == Types.STRING) and \
            (rhs.type == Types.STRING or rhs.type == Types.INTEGER):
        result = str(lhs.value) == str(lhs.value)
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
        # float string
    elif (lhs.type == Types.FLOAT or lhs.type == Types.STRING) and \
            (rhs.type == Types.STRING or rhs.type == Types.FLOAT):
        result = str(lhs.value) == str(lhs.value)
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
        # logical int
    elif (lhs.type == Types.INTEGER or lhs.type == Types.LTRUE or lhs.type == Types.LFALSE) and \
            (rhs.type == Types.INTEGER or rhs.type == Types.LTRUE or rhs.type == Types.LFALSE):
        result = isTrue(lhs) and isTrue(rhs)
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
        # logical float
    elif (lhs.type == Types.FLOAT or lhs.type == Types.LTRUE or lhs.type == Types.LFALSE) and \
            (rhs.type == Types.FLOAT or rhs.type == Types.LTRUE or rhs.type == Types.LFALSE):
        result = isTrue(lhs) and isTrue(rhs)
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))
        # logical string
    elif (lhs.type == Types.STRING or lhs.type == Types.LTRUE or lhs.type == Types.LFALSE) and \
            (rhs.type == Types.STRING or rhs.type == Types.LTRUE or rhs.type == Types.LFALSE):
        result = isTrue(lhs) and isTrue(rhs)
        if result:
            stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
        else:
            stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))