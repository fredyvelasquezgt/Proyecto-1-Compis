# Generated from yapl.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .yaplParser import yaplParser
else:
    from yaplParser import yaplParser

# This class defines a complete generic visitor for a parse tree produced by yaplParser.

class yaplVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by yaplParser#prog.
    def visitProg(self, ctx:yaplParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#class_def.
    def visitClass_def(self, ctx:yaplParser.Class_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#feature.
    def visitFeature(self, ctx:yaplParser.FeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#formal.
    def visitFormal(self, ctx:yaplParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by yaplParser#expr.
    def visitExpr(self, ctx:yaplParser.ExprContext):
        return self.visitChildren(ctx)



del yaplParser