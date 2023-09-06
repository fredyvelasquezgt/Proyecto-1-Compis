from yaplWalker import yaplWalker

# Una variable global que rastrea el número de errores encontrados
error = 0

def checkInferenceRule(operator, a, aType, b, bType):
    global error  # Indica que se usará la variable global 'error'

    # Si ambos operandos son de tipo INT, no hay error, independientemente del operador.
    if aType == "INT" and bType == "INT":
        pass

    # Si uno de los operandos es INT y el otro es STRING.
    elif (aType == "INT" and bType == "STRING") or (aType == "STRING" and bType == "INT"):
        # Si el operador es +, -, o /, es un error.
        if operator == "+" or operator == "-" or operator == "/":
            error += 1

    # Si ambos operandos son de tipo STRING.
    elif aType == "STRING" and bType == "STRING":
        # Si el operador es -, * o /, es un error.
        if operator == "-" or operator == "*" or operator == "/":
            error += 1

    # Si un operando es INT o STRING y el otro es TRUE o FALSE.
    elif (aType == "INT" and bType == "TRUE") or (aType == "INT" and bType == "FALSE") or (aType == "STRING" and bType == "TRUE") or (aType == "STRING" and bType == "FALSE"):
        # Cualquier combinación de estos operandos es un error.
        error += 1

    # Si ambos operandos son de tipo TRUE o FALSE.
    elif (aType == "TRUE" and bType == "TRUE") or (aType == "TRUE" and bType == "FALSE") or (aType == "FALSE" and bType == "TRUE") or (aType == "FALSE" and bType == "FALSE"):
        # Cualquier combinación de estos operandos es un error.
        error += 1
