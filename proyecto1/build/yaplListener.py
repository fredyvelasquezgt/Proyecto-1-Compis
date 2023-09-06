# Generated from yapl.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .yaplParser import yaplParser
else:
    from yaplParser import yaplParser

# This class defines a complete listener for a parse tree produced by yaplParser.
class yaplListener(ParseTreeListener):

    # Enter a parse tree produced by yaplParser#prog.
    def enterProg(self, ctx:yaplParser.ProgContext):
        pass

    # Exit a parse tree produced by yaplParser#prog.
    def exitProg(self, ctx:yaplParser.ProgContext):
        pass


    # Enter a parse tree produced by yaplParser#class_def.
    def enterClass_def(self, ctx:yaplParser.Class_defContext):
        pass

    # Exit a parse tree produced by yaplParser#class_def.
    def exitClass_def(self, ctx:yaplParser.Class_defContext):
        pass


    # Enter a parse tree produced by yaplParser#feature.
    def enterFeature(self, ctx:yaplParser.FeatureContext):
        pass

    # Exit a parse tree produced by yaplParser#feature.
    def exitFeature(self, ctx:yaplParser.FeatureContext):
        pass


    # Enter a parse tree produced by yaplParser#formal.
    def enterFormal(self, ctx:yaplParser.FormalContext):
        pass

    # Exit a parse tree produced by yaplParser#formal.
    def exitFormal(self, ctx:yaplParser.FormalContext):
        pass


    # Enter a parse tree produced by yaplParser#expr.
    def enterExpr(self, ctx:yaplParser.ExprContext):
        pass

    # Exit a parse tree produced by yaplParser#expr.
    def exitExpr(self, ctx:yaplParser.ExprContext):
        pass



del yaplParser