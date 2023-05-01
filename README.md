# Language Design and Implementation 2022-23

## Initial Creation

## Implementing a language in an interpreted environment
- - - 
### 01 The Lexxer

### 01.1 Defining out language
#### 01.1.1 Defining our language - arithmetic operations
Binary add (+)
Binary subtract (-)
Binary multiply (*)
Binary division (/)
Unary negation (-)

#### 01.1.2 Defining our language - logical operations
Binary and (&)
Binary or (|)
Binary negation (!)

#### 01.1.3 Defining our language - variables and data storage
Global variables (any alphanumeric key starting with an alpha, that is not a keyword)
#### 01.1.4 Defining our language - control flow - selection
#### 01.1.5 Defining our language - control flow - repetition
#### 01.1.6 Defining our language - data structure - list
### 01.2 Implementing the lexxer
#### 01.2.1 Implementing the lexxer for 01.1.1

The binary add acts as an example for this section. Here we get the left and right hand operands for the addition, 
replacing identifiers with their original values (to begin with this will just return the value on the stack). Where we 
have two integer values we perform an integer addition, for two float values, or a mix of float and integer values we must 
promote the values to floating point, with the result being a float.

We have made the choice to handle string concatenation using the + operator.

We have made the choice to handle all other cases (e.g. adding logical values) to be a string concatenation of the string
version of whatever the value actually is.
```python
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
```
#### 01.2.2 Implementing the lexxer for 01.1.2
The binary and acts as an example for this section. Here we get the left and right hand operands for the addition, 
replacing them with their logical values. We treat logical values as their logical value, otherwise 0, 0.0, and the empty 
string are treated as false, everything else is true. Note: syntatically we accept true and True, false and False as equivalent.

```python
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
```


We then perform the logical and between the two values, returning the result as either True or False (no lower case).


```python
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
```
#### 01.2.3 Implementing the lexxer for 01.1.3
Replacing the identifier is then modified to look at the global variable list. We simplify the content here by assuiming
that the varible must exist in the global variable dictionary (otherwise we should throw an error). We create a token that
has the parameters of the variable.


```python
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
```
#### 01.2.4 Implementing the lexxer for 01.1.4
#### 01.2.5 Implementing the lexxer for 01.1.5
#### 01.2.6 Implementing the lexxer for 01.1.6
### 01.3 The finished product
#### 01.3.1 the "finished" lexxer
- - - 
### 02 The Parser

### 02.1 
### 03 Using the shunting yard algorithm to generate RPN formatted tokens
### 04 A simple stack machine implementation
### 05 A simple abstract syntax tree implementation
### 06 Adding more information to our Lexemes
### 07 Error checking and handling
### 08 A better stack machine implementation
### 09 A better AST implementation

## Implementing a language in a compiled environment