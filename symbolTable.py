# Define una clase para representar un símbolo.
class Symbol():
    # Constructor: inicializa un objeto de tipo Símbolo con varios atributos.
    def __init__(self, kind, id, class_type, line, column, value, scope, numParams, paramTypes):
        # Cada uno de estos atributos representa diferentes características de un símbolo.
        # Por ejemplo, el tipo del símbolo (variable, función, etc.), su nombre/identificador, su tipo, ubicación (línea y columna),
        # valor (si lo tiene), ámbito de definición, número de parámetros (en caso de que sea una función), y tipos de los parámetros.
        self.kind = str(kind)
        self.id = str(id)
        self.class_type = str(class_type)
        self.line = line
        self.column = column
        self.value = value
        self.scope = scope
        self.numParams = numParams
        self.paramTypes = paramTypes

    # Devuelve una lista de las claves/atributos del símbolo. Útil para representar el símbolo como un diccionario.
    def keys(self):
        return ["kind", "id", "class_type", "line", "column", "value", "scope", "numParams", "paramTypes"]

    # Devuelve una lista de los valores de los atributos del símbolo.
    def values(self):
        return [self.kind, self.id, self.class_type, self.line, self.column, self.value, self.scope, self.numParams, self.paramTypes]

    # Devuelve una representación en cadena del símbolo, con un formato específico.
    def toString(self):
        return "Id: {id}, Kind: {kind}, Line: {line}, ClassType: {class_type}, Column: {column}, Value: {value}, Scope: {scope}, Number of Parameters: {numParams}, Type of Parameters: {paramTypes}".format(
            kind=self.kind,
            id=self.id,
            class_type=self.class_type,
            line=self.line,
            column=self.column,
            value=self.value,
            scope=self.scope,
            numParams=self.numParams,
            paramTypes=self.paramTypes
        )

# Define una clase para representar una tabla de símbolos, que mantiene un registro de los símbolos.
class SymbolTable():
    # Constructor: inicializa una tabla de símbolos vacía.
    def __init__(self):
        self.records = []

    # Método para añadir un símbolo a la tabla.
    def add(
        self,
        kind,
        id,
        class_type=None,
        line=None,
        column=None,
        value=None,
        scope=None,
        is_array=False,
        numParams=None,
        paramTypes=None
    ):
        # Si el símbolo no es un array, lo añade a la tabla de símbolos.
        # (Nota: El código actual no hace nada diferente si es un array.)
        if not is_array:
            self.records.append(
                Symbol(
                    kind,
                    id,
                    class_type,
                    line,
                    column,
                    value,
                    scope,
                    numParams,
                    paramTypes
                )
            )

    # Método para buscar un símbolo en la tabla por tipo, identificador y (opcionalmente) ámbito.
    def find(self, kind, id, scope=None):
        for symbol in self.records:
            if symbol.kind == str(kind) and symbol.id == str(id):
                if scope:  # Si se proporciona un ámbito, busca el símbolo en ese ámbito específico.
                    if symbol.scope == scope:
                        return symbol
                else:  # Si no se proporciona un ámbito, simplemente devuelve el símbolo encontrado.
                    return symbol
