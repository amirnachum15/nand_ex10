"""
constants - name of key words
"""

CLASS = "class"
METHOD = "method"
FUNCTION = "function"
CONSTRUCTOR = "constructor"
INT = "int"
BOOLEAN = "boolean"
CHAR = "char"
VOID = "void"
VAR = "var"
STATIC = "static"
FIELD = "field"
LET = "let"
DO = "do"
IF = "if"
ELSE = "else"
WHILE = "while"
RETURN = "return"
TRUE = "true"
FALSE = "false"
NULL = "null"
THIS = "this"

class JackTokenizer:
    def __init__(self, input_file):
        self.input_file = input_file

    def hasMoreTokens(self):
        return True

    def advance(self):
        return true

    def keyWord(self):
        return True

    def symbol(self):
        return True

    def identifier(self):
        return True

    def intVal(self):
        return True

    def stringVal(self):
        return True

