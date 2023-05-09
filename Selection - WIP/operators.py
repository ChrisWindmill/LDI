import variable
from lexeme import Lexeme
from lexeme import Types

def isBinaryOperator(type):
    if type != Types.UNEG and type != Types.UNARYNEGATION and type != Types.USUB:
        return True
    return False


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

def replaceIdentifier(stack):
    value = stack.pop()
    if value.type == Types.IDENTIFIER:
        if variable.globalVariables[value.value]:
            # value exists
            temp = variable.globalVariables[value.value]
            value.value = temp.strValue
            value.type = temp.type
            value.superType = Types.VALUE
            value.precedece = temp.precedence

    return value

def binaryAdd(stack):
    rhs = replaceIdentifier(stack)
    lhs = replaceIdentifier(stack)
    
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
        result = lhs.value + rhs.value
        stack.append(Lexeme(str(result), Types.STRING, Types.VALUE, 0))
    # Unknown case - treat values as strings and concatenate
    else:
        result = str(lhs.value) + str(rhs.value)
        stack.append(Lexeme(str(result), Types.STRING, Types.VALUE, 0))

def Assignment(stack):
    rhs = replaceIdentifier(stack)
    name = stack.pop()

    var = variable.variable(name.value)
    var.supertype = Types.VALUE
    var.precedence = 0

    if rhs.type == Types.INTEGER:
        var.type = Types.INTEGER
        var.intValue = int(rhs.value)
    elif rhs.type == Types.FLOAT:
        var.type = Types.FLOAT
        var.floatValue = float(rhs.value)
    elif rhs.type == Types.STRING:
        var.type = Types.STRING
        var.strValue = int(rhs.value)
    elif rhs.type == Types.LTRUE:
        var.type = Types.LTRUE
        var.strValue = int(rhs.value)
    elif rhs.type == Types.LFALSE:
        var.type = Types.LFALSE
        var.strValue = int(rhs.value)
    else:
        # throw error
        pass

    var.update()
    variable.globalVariables[var.name] = var;
    stack.append(Lexeme(var.strValue, var.type, var.supertype, var.precedence))

def unaryNegation(stack):
    value = replaceIdentifier(stack)
    if value.type == Types.INTEGER:
        value.value = str(-int(value.value))
    elif value.type == Types.Float:
        value.value = str(-float(value.value))
    else:
        value.value = "Error"
        value.type = Types.STRING
    stack.append(value)

def binarySubtract(stack):
    rhs = replaceIdentifier(stack)
    lhs = replaceIdentifier(stack)

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
    rhs = replaceIdentifier(stack)
    lhs = replaceIdentifier(stack)

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
    rhs = replaceIdentifier(stack)
    lhs = replaceIdentifier(stack)

    # Mixed Int Float Case: promote integer to float for calculations
    if (lhs.type == Types.FLOAT or lhs.type == Types.INTEGER) and \
            (rhs.type == Types.INTEGER or rhs.type == Types.FLOAT):
        result = float(lhs.value) / float(rhs.value)
        stack.append(Lexeme(str(result), Types.FLOAT, Types.VALUE, 0))
    else:
        result = "Error"
        stack.append(Lexeme(str(result), Types.STRING, Types.VALUE, 0))


def binaryAND(stack):
    rhs = replaceIdentifier(stack)
    lhs = replaceIdentifier(stack)

    logicalLHS = isTrue(lhs)
    logicalRHS = isTrue(rhs)

    result = logicalLHS and logicalRHS
    if result:
        stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
    else:
        stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))

def binaryOR(stack):
    rhs = replaceIdentifier(stack)
    lhs = replaceIdentifier(stack)

    logicalLHS = isTrue(lhs)
    logicalRHS = isTrue(rhs)

    result = logicalLHS or logicalRHS
    if result:
        stack.append(Lexeme(str(result), Types.LTRUE, Types.VALUE, 0))
    else:
        stack.append(Lexeme(str(result), Types.LFALSE, Types.VALUE, 0))


def binaryNotEqual(stack):
    rhs = replaceIdentifier(stack)
    lhs = replaceIdentifier(stack)

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
    rhs = replaceIdentifier(stack)
    lhs = replaceIdentifier(stack)

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