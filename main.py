import sys
import os
from antlr4 import *
from build.yaplLexer import yaplLexer
from build.yaplParser import yaplParser
from yaplWalker import yaplWalker
from yaplErrorListener import yaplErrorListener
from prettytable import PrettyTable

def main():
    # input = FileStream(argv[1])
    input = FileStream('input/errores.yapl')

    lexer = yaplLexer(input)
    lexer.removeErrorListeners()
    lexer.addErrorListener(yaplErrorListener())

    stream = CommonTokenStream(lexer)
    stream.fill()

    print("Tokens:")
    for token in stream.tokens:
        print(token)

    parser = yaplParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(yaplErrorListener())

    tree = parser.prog()
    print("\nParse Tree:")
    # print(tree.toStringTree(parser.ruleNames))

    walker = yaplWalker()
    walker.initSymbolTable()
    walker.visit(tree)

    cont = 0
    print("\nSymbol Table:")
    myTable = PrettyTable()
    for record in walker.symbolTable.records:
        cont = cont + 1
        # print("Symbol", record.toString())
        myTable.field_names = record.keys()
        myTable.add_row(record.values())
    print(myTable)

    if len(walker.errors) >= 1:
        print("\n" + yaplErrorListener.ANSI_RED)
        print("----------------------------- ERROR -----------------------------")
        for error in walker.errors:
            if "payload" in error:
                print("Error: position " + str(error["payload"].line) + ":" + str(error["payload"].column) + " " + error["msg"])
            else:
                print("Error: " + error["msg"])

        print("-----------------------------------------------------------------")
        print("\n" + yaplErrorListener.ANSI_RESET)

if __name__ == '__main__':
    main()
