# Proyecto 1 - Compiladores 2

## Autores

- Fredy Velasquez
- Jorge Caballeros

## Ejecutar programa

Correr el comando en terminal y en folder del programa

`python3 main.py`

Esto abre una interfaz con un editor de codigo pequeño en donde podemos colocar código.

Ejecutar el botón de compilar para ejecutar las funciones.

Abajo evaluar el output.

Botón de borrar para reiniciar el funcionamiento.

## Consideraciones

- Contar con tkinter instalado
- Contar con ANTLR instalado
- Contar con una version reciente de python
- Contar con prettytable instalado

## Explicación


- main.py:

Maneja la lógica principal del compilador:

Permite a los usuarios escribir código en una interfaz gráfica, compilar ese código para analizarlo y ver la salida (tokens, estructura, errores, etc.) en la misma ventana.

Lee un archivo. Procesa ese archivo para segmentar el contenido en "tokens" (pequeñas piezas de código que tienen un significado específico, como variables o operadores).
Imprime esos tokens.
Convierte los tokens en un árbol de sintaxis, que representa la estructura del código.
Usa un "caminante" para recorrer el árbol y construir una tabla de símbolos. Esta tabla guarda información sobre las variables y funciones en el código.
Si hay errores durante el análisis, estos se imprimen en color rojo.

- symbolTable.py

Este programa define dos clases principales: Symbol y SymbolTable. La clase Symbol se utiliza para representar un símbolo con atributos específicos, como el tipo de símbolo (variable, función, etc.), su identificador, tipo, ubicación, valor, ámbito de definición, número de parámetros y los tipos de esos parámetros. Además, ofrece métodos para obtener las claves y valores de sus atributos y una representación en cadena del símbolo.

Por otro lado, la clase SymbolTable es esencialmente una colección de objetos Symbol y representa una tabla de símbolos. La tabla de símbolos se utiliza en la compilación y análisis de programas para mantener un registro de todos los símbolos definidos. Esta clase permite añadir símbolos a la tabla y buscar un símbolo específico en ella basado en ciertos criterios, como tipo, identificador y ámbito. La funcionalidad de manejar símbolos como arrays parece estar esbozada pero no completamente implementada en el código proporcionado.

- typeSystem.py

El código es una función llamada checkInferenceRule que verifica la validez de las operaciones entre dos operandos dados sus tipos y el operador utilizado. La función utiliza una variable global error para llevar un registro del número de errores encontrados. El propósito es asegurarse de que las operaciones se estén realizando entre tipos compatibles y reportar un error si no lo son. Por ejemplo:

Operaciones entre dos operandos de tipo INT son siempre válidas.
No se permite sumar, restar o dividir un INT con un STRING y viceversa.
No se permite restar, multiplicar o dividir dos STRINGs.
Cualquier operación que involucre a un INT o STRING con TRUE o FALSE es inválida.
Cualquier operación entre TRUE y FALSE también es inválida.
Cada vez que se detecta una combinación inválida de operandos y operadores, se incrementa el contador de errores. Es importante señalar que el archivo hace referencia a un módulo yaplWalker, aunque no se utiliza explícitamente en este fragmento de código.

- yapl.g4

Define una gramática para un lenguaje llamado "yapl" usando ANTLR, que es una herramienta para generar analizadores léxicos y sintácticos. Esta gramática define la estructura y la sintaxis de un lenguaje de programación orientado a objetos, permitiendo la definición de clases, métodos, atributos y una variedad de expresiones y operaciones comunes. La gramática puede ser utilizada por ANTLR para generar analizadores que procesen y analicen el código escrito en el lenguaje "yapl".Aquí está un resumen simplificado:

Definición léxica:

Define tokens como palabras clave (CLASS, ELSE, FALSE, etc.), identificadores para tipos (TYPE_ID), identificadores para objetos (OBJECT_ID), números enteros (INT), cadenas (STRING), comentarios y más.
Se define una serie de reglas para reconocer estos tokens, como patrones de caracteres que deben coincidir.
Definición sintáctica:

Define cómo deben organizarse y combinarse los tokens para formar estructuras válidas en el lenguaje.
prog: Describe que un programa consiste en una o más definiciones de clases, cada una terminada con un punto y coma.
class_def: Describe la definición de una clase, que puede o no heredar de otra clase y tiene un conjunto de características dentro de llaves {...}.
feature: Representa las características (métodos o atributos) de una clase. Puede ser una definición de función o una asignación.
formal: Describe los parámetros formales de una función.
expr: Es la regla más compleja y describe las diferentes expresiones válidas en el lenguaje, como asignaciones, llamadas a métodos, estructuras condicionales, loops, operaciones aritméticas, y más. Por ejemplo, IF expr THEN expr ELSE expr FI describe una expresión condicional.

- yaplErrorListener.py

Define una clase llamada yaplErrorListener que tiene el propósito de personalizar el comportamiento al encontrarse con errores de sintaxis en el código que se está analizando usando ANTLR4.yaplErrorListener está diseñada para proporcionar una retroalimentación visual clara y personalizada en caso de que se encuentren errores de sintaxis durante el análisis de código con ANTLR4. Al usar esta clase, los errores se mostrarán en rojo en la terminal para que sean fácilmente identificables. Aquí está un resumen simplificado:

Importaciones:

Se importan funciones y clases esenciales de la biblioteca ANTLR4, incluyendo la clase base ErrorListener que proporciona métodos para manejar errores.
Clase yaplErrorListener:

Hereda de ErrorListener. Esta clase se utiliza para personalizar cómo se manejan y se reportan los errores de sintaxis detectados por ANTLR4.
Dentro de la clase, se definen dos constantes de clase, ANSI_RESET y ANSI_RED, que se utilizan para cambiar el color del texto en la terminal.
Método syntaxError:

Es un método que se llama automáticamente cuando ANTLR4 detecta un error de sintaxis en el código fuente que está analizando.
El método cambia el color del texto de la terminal a rojo, imprime un mensaje de error con formato, indicando la línea y columna del error, y luego restablece el color del texto a su valor predeterminado.
Esta personalización proporciona una visualización clara y destacada de los errores, haciéndolos fácilmente identificables para el usuario.

- yaplWalker.py

Parte de un analizador de lenguajes de programación que utiliza la herramienta ANTLR4. ANTLR4 es una herramienta que ayuda a crear analizadores para lenguajes de programación.Define cómo procesar y verificar un código fuente escrito en el lenguaje yapl. Utiliza la herramienta ANTLR4 para analizar el código, y durante el análisis, verifica errores comunes y construye una tabla de símbolos para referencia futura.

Importaciones:

Importa algunas clases y funciones necesarias para trabajar con árboles de análisis y la tabla de símbolos.
Clase yaplWalker:

Es una clase personalizada que "camina" o "visita" a través del árbol de análisis generado por ANTLR4 para el lenguaje yapl.
La clase contiene métodos que definen cómo se deben procesar diferentes partes del código fuente yapl.
Inicialización __init__:

Define algunas variables iniciales, como los tipos básicos, errores y contadores.
Métodos de la Tabla de Símbolos:

initSymbolTable: Inicializa la tabla de símbolos.
getSymbolTable: Devuelve la tabla de símbolos.
Métodos Visitantes:

Estos métodos determinan qué hacer cuando el "visitante" encuentra ciertas construcciones en el código fuente:
visitProg: Procesa el programa entero. Añade tipos básicos a la tabla de símbolos y verifica que solo haya una clase "Main" y un método "main".
visitClass_def: Procesa las definiciones de clases y verifica errores, como heredar de tipos básicos o herencia recursiva.
visitFeature: Procesa las características de una clase, como métodos.
visitFormal: Procesa los parámetros de un método.
visitExpr: Procesa diferentes tipos de expresiones, como declaraciones IF, WHILE, LET, entre otras, y las añade a la tabla de símbolos.
Liberación de Memoria:

Al final, el programa elimina la referencia al analizador para liberar memoria.





