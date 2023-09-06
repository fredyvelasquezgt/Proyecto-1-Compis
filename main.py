# Importamos módulos y bibliotecas necesarios
import sys
import os
import io   # Agregar esta importación
from antlr4 import *
from build.yaplLexer import yaplLexer
from build.yaplParser import yaplParser
from yaplWalker import yaplWalker
from yaplErrorListener import yaplErrorListener
from prettytable import PrettyTable
import tkinter as tk
from tkinter import scrolledtext  # Para el mini editor de código con desplazamiento
from tkinter import messagebox   # Para mostrar mensajes


def main():
    # Tomamos un archivo como entrada. Aunque hay una línea comentada
    # que parece tomar el archivo desde los argumentos de línea de comando,
    # la línea sin comentar toma un archivo llamado "errores.yapl".
    input = FileStream('input/sample.yapl')

    # Creamos un lexer con la entrada. Esto segmentará la entrada en tokens.
    lexer = yaplLexer(input)
    # Eliminamos cualquier error listener predeterminado y añadimos uno personalizado.
    lexer.removeErrorListeners()
    lexer.addErrorListener(yaplErrorListener())

    # Creamos un flujo de tokens y lo llenamos con los tokens generados por el lexer.
    stream = CommonTokenStream(lexer)
    stream.fill()

    # Imprimimos los tokens generados.
    print("Tokens:")
    for token in stream.tokens:
        print(token)

    # Creamos un parser con el flujo de tokens.
    parser = yaplParser(stream)
    # Al igual que con el lexer, eliminamos cualquier listener predeterminado y añadimos uno personalizado.
    parser.removeErrorListeners()
    parser.addErrorListener(yaplErrorListener())

    # Creamos un árbol de sintaxis con el parser y lo imprimimos.
    tree = parser.prog()
    print("\nParse Tree:")
    # print(tree.toStringTree(parser.ruleNames))

    # Creamos un caminante (walker) para el árbol de sintaxis y lo visitamos.
    walker = yaplWalker()
    walker.initSymbolTable()  # Inicializamos la tabla de símbolos.
    walker.visit(tree)  # Visitamos el árbol para llenar la tabla de símbolos.

    # Imprimimos la tabla de símbolos.
    cont = 0
    print("\nSymbol Table:")
    myTable = PrettyTable()  # Usamos PrettyTable para una visualización bonita.
    for record in walker.symbolTable.records:
        cont = cont + 1
        myTable.field_names = record.keys()
        myTable.add_row(record.values())
    print(myTable)

    # Si hay errores en el caminante (walker), los imprimimos.
    if len(walker.errors) >= 1:
        # ANSI_RED es probablemente un código de color para imprimir en rojo.
        print("\n" + yaplErrorListener.ANSI_RED)
        print("----------------------------- ERROR -----------------------------")
        for error in walker.errors:
            # Dependiendo de si el error tiene un 'payload' o no, imprimimos diferentes mensajes.
            if "payload" in error:
                print("Error: position " + str(error["payload"].line) + ":" + str(error["payload"].column) + " " + error["msg"])
            else:
                print("Error: " + error["msg"])
        print("-----------------------------------------------------------------")
        print("\n" + yaplErrorListener.ANSI_RESET)  # Resetear el color.

# Si este script se está ejecutando como el principal, llamamos a la función main.
if __name__ == '__main__':
    main()



class CompilerApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Compiler App")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Label para el editor
        label_editor = tk.Label(self, text="Editor de código:")
        label_editor.pack(pady=10)

        # Text widget para el mini editor de código
        self.code_editor = scrolledtext.ScrolledText(self, undo=True, width=90, height=20, wrap=tk.WORD)
        self.code_editor.pack(pady=10, padx=10)

        # Botón para iniciar el proceso de compilación
        compile_button = tk.Button(self, text="Compilar", command=self.compile_code)
        compile_button.pack(pady=10)

        # Text widget para mostrar resultados
        self.results_area = scrolledtext.ScrolledText(self, undo=True, width=90, height=10, wrap=tk.WORD)
        self.results_area.pack(pady=10, padx=10)

    def compile_code(self):
        code = self.code_editor.get("1.0", tk.END).strip()  # Añadir .strip() para remover espacios y saltos de línea
        
        if not code:  # Si el código está vacío
            messagebox.showinfo("Información", "Por favor, introduce algún código antes de compilar.")
            return

        with open('input/sample.yapl', 'w') as file:
            file.write(code)

        # Redirigir la salida estándar para capturar los resultados
        original_stdout = sys.stdout
        result = io.StringIO()  # Usar StringIO en lugar de lista
        sys.stdout = result

        try:
            main()  # Llamando a la función main original
            self.results_area.delete("1.0", tk.END)
            self.results_area.insert(tk.INSERT, result.getvalue())  # Obtener el contenido del StringIO
        except Exception as e:
            self.results_area.delete("1.0", tk.END)
            self.results_area.insert(tk.INSERT, "Ocurrió un error: " + str(e))
            messagebox.showerror("Error", str(e))
        finally:
            # Restaurar la salida estándar
            sys.stdout = original_stdout

app = CompilerApp()
app.mainloop()