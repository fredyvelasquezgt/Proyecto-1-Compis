# Define una clase para representar un símbolo.
class Symbol

    # Este método inicializa un objeto de tipo Symbol. Al igual que en la versión Python, se inicializa con varios atributos.
    def initialize(kind, id, class_type, line, column, value, scope, numParams, paramTypes)
        @kind = kind.to_s
        @id = id.to_s
        @class_type = class_type.to_s
        @line = line
        @column = column
        @value = value
        @scope = scope
        @numParams = numParams
        @paramTypes = paramTypes
    end

    # NOTA: A diferencia de la versión de Python, este código de Ruby omite los métodos `keys`, `values` y `toString`. 
    # Esto puede deberse a que esos métodos no son necesarios en el contexto de este código de Ruby o están definidos en otro lugar.

end

# Define una clase para representar una tabla de símbolos.
class SymbolTable

    # Este método inicializa una tabla de símbolos vacía.
    def initialize
        @records = []
    end

    # Método para añadir un símbolo a la tabla.
    def add(
        kind,
        id,
        class_type=nil,
        line=nil,
        column=nil,
        value=nil,
        scope=nil,
        is_array=false,
        numParams=nil,
        paramTypes=nil
    )
        # Si el símbolo no es un array, lo añade a la tabla de símbolos.
        unless is_array
            @records.append(
                Symbol.new(kind, id, class_type, line, column, value, scope, numParams, paramTypes)
            )
        end
    end

    # Método para buscar un símbolo en la tabla por tipo, identificador y (opcionalmente) ámbito.
    def find(kind, id, scope=nil)
        @records.each do |symbol|
            if symbol.kind == kind.to_s && symbol.id == id.to_s
                return symbol unless scope
                return symbol if scope == symbol.scope
            end
        end
    end

end
