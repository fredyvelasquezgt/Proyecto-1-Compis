

class Symbol():

    def __init__(self, kind, id, class_type, line, column, value, scope, numParams, paramTypes):
        self.kind = str(kind)
        self.id = str(id)
        self.class_type = str(class_type)
        self.line = line
        self.column = column
        self.value = value
        self.scope = scope
        self.numParams = numParams
        self.paramTypes = paramTypes

    def keys(self):
        return ["kind", "id", "class_type", "line", "column", "value", "scope", "numParams", "paramTypes"]

    def values(self):
        return [self.kind, self.id, self.class_type, self.line, self.column, self.value, self.scope, self.numParams, self.paramTypes]

    def toString(self):
        return "Id: {id}, Kind: {kind}, Line: {line}, ClassType: {class_type}, Column: {column}, Value: {value}, Scope: {scope}, Number of Parameters: {numParams}, Type of Parameters: {paramTypes}".format(
            kind = self.kind,
            id = self.id,
            class_type = self.class_type,
            line = self.line,
            column = self.column,
            value = self.value,
            scope = self.scope,
            numParams = self.numParams,
            paramTypes = self.paramTypes
        )


class SymbolTable():

    def __init__(self):
        self.records = []

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

    def find(self, kind, id, scope=None):
        for symbol in self.records:
            if symbol.kind == str(kind) and symbol.id == str(id):
                if scope:
                    if symbol.scope == scope:
                        return symbol
                else:
                    return symbol
