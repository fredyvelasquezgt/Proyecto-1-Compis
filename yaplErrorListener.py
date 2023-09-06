# Importamos las funciones y clases necesarias de la biblioteca ANTLR4.
from antlr4 import *
from antlr4.error.ErrorListener import *

# Definimos una clase yaplErrorListener que hereda de la clase ErrorListener.
class yaplErrorListener(ErrorListener):

    # Estas son constantes de clase para cambiar el color del texto en la terminal.
    # ANSI_RESET restablece el color del texto a su valor predeterminado.
    # ANSI_RED cambia el color del texto a rojo.
    ANSI_RESET = "\u001B[0m"
    ANSI_RED = "\u001B[31m"

    # Este método se llama automáticamente cuando el analizador detecta un error de sintaxis.
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Cambiamos el color del texto a rojo.
        print("\n" + self.ANSI_RED)

        # Imprimimos un mensaje de error con formato, mostrando la línea y columna donde ocurrió el error,
        # junto con el mensaje de error proporcionado.
        print("----------------------------- ERROR -----------------------------")
        print("Error: position " + str(line) + ":" + str(column) + " " + msg)
        print("-----------------------------------------------------------------")

        # Restablecemos el color del texto a su valor predeterminado.
        print("\n" + self.ANSI_RESET)
