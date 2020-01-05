import re

"""
constants - name of key words
"""

KEYWORD = "keyword"
SYMBOL = "symbol"
IDENTIFIER = "identifier"
INT_CONST = "integerConstant"
STRING_CONST = "string_const"
TOKEN_TYPES = [KEYWORD, SYMBOL, IDENTIFIER, INT_CONST, STRING_CONST]

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
KEYWORDS = [CLASS, METHOD, FUNCTION, CONSTRUCTOR, INT, BOOLEAN, CHAR, VOID, VAR, STATIC, FIELD,
            LET, DO, IF, ELSE, WHILE, RETURN, TRUE, FALSE, NULL, THIS]
SYMBOLS = ["{", "}", "[", "]", "(", ")", ".", ",", ";", "+", "-", "*", "/", "&", "|", "<", ">", "=", "~"]

class JackTokenizer:
    def __init__(self, input_file_path):
        self.input_file = open(input_file_path, "r")
        self.words = []
        self.index = 0
        self.next_word = ""

    def _split_according_to_char(self, buffer, char):
        """
        this function gets a list, and splits the buffer according to the char
        saving the char, and deleting (like in regular split)
        """
        #checking if the char appears in the buffer
        char_occur = False
        for value in buffer:
            if char in value:
                char_occur = True
                break
        if not char_occur:
            return buffer
        tmp = []
        for buf in buffer:

            if char in buf:
                #we need to split
                splitted = buf.split(char)
                for word in splitted:
                    tmp.append(word) if word != "" else None
                    tmp.append(char)
                tmp = tmp[:-1]
            else:
                tmp.append(buf)
        return tmp

    def join_strings(self, buffer):
        retVal = []
        i = 0
        while i < len(buffer):
            buf = buffer[i]
            if '"' in buf:
                beginning = i
                while '"' not in buffer[i+1]:
                    i += 1
                end = i + 1
                i = end
                joined_string = ""
                for index in range(beginning, end + 1):
                    joined_string += buffer[index]
                    joined_string += ' '
                joined_string = joined_string[:-1]
                retVal.append(joined_string)
            else:
                retVal.append(buf)
            i += 1

        return retVal

    def _split_symbols(self, buffer):
        #first we will split everything in respect to spacebar
        retVal = buffer.split()
        retVal = self.join_strings(retVal)
        for char_to_split in SYMBOLS:
            retVal = self._split_according_to_char(retVal, char_to_split)
        return retVal

    def hasMoreTokens(self):
        if len(self.words) <= self.index:
            #this means that we need to read from the file
            buffer = self.input_file.readline()
            if not buffer:
                #EOF reached
                return False
            self.words = self._split_symbols(buffer)
            self.index = 0

        #we just need to give the next word in self.words
        self.next_word = self.words[self.index]
        self.index += 1
        return True

    def advance(self):
        if not self.next_word:
            return None
        #if there are no more words, return None
        return self.next_word

    def tokenType(self):
        if self.next_word in KEYWORDS:
            return KEYWORD
        if self.next_word in SYMBOLS:
            return SYMBOL
        #TODO - add a regex to check if next word is an identifier
        try:
            num = int(self.next_word)
            return INT_CONST
        except ValueError:
            x = 0
        #TODO - check if value error is the right type of error (when i have wifi)
        if self.next_word[0] == '"' and self.next_word[-1] == '"':
            return STRING_CONST
        pattern = re.compile(r"[\w]")
        m = pattern.match(self.next_word[0])
        if not m:
            return "Unknown"
        elif m.end() == len(self.next_word[0]):
            return IDENTIFIER

        return "Unknown"



    def keyWord(self):
        return self.next_word[0]

    def symbol(self):
        return self.next_word[0]

    def identifier(self):
        return self.next_word[0]

    def intVal(self):
        retVal = int(self.next_word)
        return retVal

    def stringVal(self):
        #losing the first and last characters (which are ")
        retVal = self.next_word[1:-1]
        return retVal

