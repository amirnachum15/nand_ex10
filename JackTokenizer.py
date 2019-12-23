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
    def __init__(self, input_file_path):
        self.input_file = open(input_file_path, "r")


    def hasMoreTokens(self):

        return True

    def advance(self):
        if not self.next_word:
            return self.next_word
        #if there are no more words, return None
        return None

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

