
from antlr4 import *
from symbolTable import SymbolTable
from build.yaplParser import yaplParser
from build.yaplVisitor import yaplVisitor

# This class defines a custom visitor for a parse tree.

class yaplWalker(yaplVisitor):

    def __init__(self) -> None:
        self.basic_types = ["Int", "String", "Bool"]
        self.errors = []
        self.main_class_count = 0
        self.main_method_count = 0
        self.current_class = None
        self.current_method = None
        super().__init__()

    def initSymbolTable(self):
        self.symbolTable = SymbolTable()

    def getSymbolTable(self):
        return  self.symbolTable

    # Visit a parse tree produced by yaplParser#prog.
    def visitProg(self, ctx:yaplParser.ProgContext):

        # Defining Int
        self.symbolTable.add(
            "CLASS",
            "Int",
            "class",
        )

        # Defining Bool
        self.symbolTable.add(
            "CLASS",
            "Bool",
            "class",
        )

        # Defining String
        self.symbolTable.add(
            "CLASS",
            "String",
            "class",
        )

        # Defining IO
        self.symbolTable.add(
            "CLASS",
            "IO",
            "class",
        )

        self.symbolTable.add(
            "OBJECT_ID",
            "in_string",
            "Object",
            numParams=1,
            paramTypes=["String"],
            scope="global - IO"
        )

        self.symbolTable.add(
            "OBJECT_ID",
            "out_string",
            "Object",
            numParams=1,
            paramTypes=["String"],
            scope="global - IO"
        )

        self.symbolTable.add(
            "OBJECT_ID",
            "in_int",
            "Object",
            numParams=1,
            paramTypes=["Int"],
            scope="global - IO"
        )

        self.symbolTable.add(
            "OBJECT_ID",
            "out_int",
            "Object",
            numParams=1,
            paramTypes=["Int"],
            scope="global - IO"
        )

        self.visitChildren(ctx)

        # Checking the amount of Main classes
        if self.main_class_count != 1:
            self.errors.append({
                "msg": "Solo una clase Main debe existir",
                # "payload": ctx.TYPE_ID()[0].getPayload()
            })

        # Checking the amount of main methods
        if self.main_method_count != 1:
            self.errors.append({
                "msg": "Solo un metodo main en la clase Main debe existir",
                # "payload": feat_child_ctx.OBJECT_ID().getPayload()
            })

        return ctx


    # Visit a parse tree produced by yaplParser#class_def.
    def visitClass_def(self, ctx:yaplParser.Class_defContext):

        self.current_class = str(ctx.TYPE_ID()[0])

        # Checking Main Class errors
        if self.current_class == "Main":
            self.main_class_count += 1
            if len(ctx.TYPE_ID()) > 1:
                self.errors.append({
                    "msg": "Clase Main no debe heredar de ninguna",
                    "payload": ctx.TYPE_ID()[1].getPayload()
                })

        self.symbolTable.add(
            "CLASS",
            self.current_class,
            ctx.CLASS(),
            line=ctx.CLASS().getPayload().line,
            column=ctx.CLASS().getPayload().column
        )

        # Class inheritance validations
        if ctx.INHERITS():
            # Inherit from a basic type is not possible
            if str(ctx.TYPE_ID()[1]) in self.basic_types:
                self.errors.append({
                    "msg": "No se puede heredar de un tipo basico",
                    "payload": ctx.TYPE_ID()[1].getPayload()
                })

            # Recursive inheritance is not possible
            if self.current_class == str(ctx.TYPE_ID()[1]):
                self.errors.append({
                    "msg": "No se puede heredar recursivamente",
                    "payload": ctx.TYPE_ID()[1].getPayload()
                })

            # Multiple inheritance is not possible
            if len(ctx.TYPE_ID()) >= 3 and ctx.TYPE_ID()[2]:
                self.errors.append({
                    "msg": "No se puede tener multiple herencia",
                    "payload": ctx.TYPE_ID()[2].getPayload()
                })

        self.visitChildren(ctx)
        return ctx


    # Visit a parse tree produced by yaplParser#feature.
    def visitFeature(self, ctx:yaplParser.FeatureContext):

        self.current_method = str(ctx.OBJECT_ID())

        # Checking the amount of main methods
        if str(ctx.OBJECT_ID()) == "main":
            self.main_method_count += 1

            if len(ctx.formal()) > 0:
                self.errors.append({
                    "msg": "Metodo main no debe tener parametros formales",
                    "payload": ctx.OBJECT_ID().getPayload()
                })

        self.symbolTable.add(
            "OBJECT_ID",
            ctx.OBJECT_ID(),
            ctx.TYPE_ID()[0],
            line=ctx.OBJECT_ID().getPayload().line,
            column=ctx.OBJECT_ID().getPayload().column,
            numParams=len(ctx.formal()),
            paramTypes=[],
            scope="global - {class_scope}".format(class_scope=self.current_class)
        )

        self.visitChildren(ctx)
        return ctx


    # Visit a parse tree produced by yaplParser#formal.
    def visitFormal(self, ctx:yaplParser.FormalContext):
        global_scope = "global - {class_scope}".format(class_scope=self.current_class)
        scope = "local - {method_scope}".format(method_scope=self.current_method)

        # Adding the current formal to the feature which belongs
        feature_symbol = self.symbolTable.find("OBJECT_ID", self.current_method, global_scope)

        if feature_symbol:
            feature_symbol.paramTypes.append(str(ctx.TYPE_ID()[0]))

        # Checking if already exists this formal on the current_scope
        symbol = self.symbolTable.find("OBJECT_ID", ctx.OBJECT_ID(), scope)

        if symbol:
            self.errors.append({
                "msg": "{id} already exists".format(id=ctx.OBJECT_ID()),
                "payload": ctx.OBJECT_ID().getPayload()
            })

        self.symbolTable.add(
            "OBJECT_ID",
            ctx.OBJECT_ID(),
            ctx.TYPE_ID()[0],
            line=ctx.OBJECT_ID().getPayload().line,
            column=ctx.OBJECT_ID().getPayload().column,
            scope=scope
        )

        self.visitChildren(ctx)
        return ctx


    # Visit a parse tree produced by yaplParser#expr.
    def visitExpr(self, ctx:yaplParser.ExprContext):
        if ctx.LET():
            self.symbolTable.add(
                "OBJECT_ID",
                ctx.OBJECT_ID()[0],
                ctx.TYPE_ID()[0],
                line=ctx.LET().getPayload().line,
                column=ctx.LET().getPayload().column
            )

        if len(ctx.OBJECT_ID()) == 1:
            symbol = self.symbolTable.find("OBJECT_ID", ctx.OBJECT_ID()[0])

            if not symbol:
                self.errors.append({
                    "msg": "Undefined: {id}".format(id=ctx.OBJECT_ID()[0]),
                    "payload": ctx.OBJECT_ID()[0].getPayload()
                })

                self.symbolTable.add(
                    "OBJECT_ID",
                    ctx.OBJECT_ID()[0],
                    line=ctx.OBJECT_ID()[0].getPayload().line,
                    column=ctx.OBJECT_ID()[0].getPayload().column
                )

        if len(ctx.TYPE_ID()) == 1:
            self.symbolTable.add(
                "TYPE_ID",
                ctx.TYPE_ID()[0],
                line=ctx.TYPE_ID()[0].getPayload().line,
                column=ctx.TYPE_ID()[0].getPayload().column
            )

        if ctx.IF():
            self.symbolTable.add(
                "IF",
                ctx.IF(),
                line=ctx.IF().getPayload().line,
                column=ctx.IF().getPayload().column
            )

        if ctx.THEN():
            self.symbolTable.add(
                "THEN",
                ctx.THEN(),
                line=ctx.THEN().getPayload().line,
                column=ctx.THEN().getPayload().column
            )

        if ctx.ELSE():
            self.symbolTable.add(
                "ELSE",
                ctx.ELSE(),
                line=ctx.ELSE().getPayload().line,
                column=ctx.ELSE().getPayload().column
            )

        if ctx.FI():
            self.symbolTable.add(
                "FI",
                ctx.FI(),
                line=ctx.FI().getPayload().line,
                column=ctx.FI().getPayload().column
            )

        if ctx.WHILE():
            self.symbolTable.add(
                "WHILE",
                ctx.WHILE(),
                line=ctx.WHILE().getPayload().line,
                column=ctx.WHILE().getPayload().column
            )

        if ctx.LOOP():
            self.symbolTable.add(
                "LOOP",
                ctx.LOOP(),
                line=ctx.LOOP().getPayload().line,
                column=ctx.LOOP().getPayload().column
            )

        if ctx.POOL():
            self.symbolTable.add(
                "POOL",
                ctx.POOL(),
                line=ctx.POOL().getPayload().line,
                column=ctx.POOL().getPayload().column
            )

        if ctx.IN():
            self.symbolTable.add(
                "IN",
                ctx.IN(),
                line=ctx.IN().getPayload().line,
                column=ctx.IN().getPayload().column
            )

        if ctx.NEW():
            self.symbolTable.add(
                "NEW",
                ctx.NEW(),
                line=ctx.NEW().getPayload().line,
                column=ctx.NEW().getPayload().column
            )

        if ctx.ISVOID():
            self.symbolTable.add(
                "ISVOID",
                ctx.ISVOID(),
                line=ctx.ISVOID().getPayload().line,
                column=ctx.ISVOID().getPayload().column
            )

        if ctx.NOT():
            self.symbolTable.add(
                "NOT",
                ctx.NOT(),
                line=ctx.NOT().getPayload().line,
                column=ctx.NOT().getPayload().column
            )

        if ctx.INT():
            self.symbolTable.add(
                "INT",
                ctx.INT(),
                line=ctx.INT().getPayload().line,
                column=ctx.INT().getPayload().column
            )

        if ctx.STRING():
            self.symbolTable.add(
                "STRING",
                ctx.STRING(),
                line=ctx.STRING().getPayload().line,
                column=ctx.STRING().getPayload().column
            )

        if ctx.TRUE():
            self.symbolTable.add(
                "TRUE",
                ctx.TRUE(),
                line=ctx.TRUE().getPayload().line,
                column=ctx.TRUE().getPayload().column
            )

        if ctx.FALSE():
            self.symbolTable.add(
                "FALSE",
                ctx.FALSE(),
                line=ctx.FALSE().getPayload().line,
                column=ctx.FALSE().getPayload().column
            )

        if ctx.SELF():
            self.symbolTable.add(
                "SELF",
                ctx.SELF(),
                line=ctx.SELF().getPayload().line,
                column=ctx.SELF().getPayload().column
            )

        self.visitChildren(ctx)
        return ctx



del yaplParser