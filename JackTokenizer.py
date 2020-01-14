import re

"""
constants - name of key words
"""

KEYWORD = "keyword"
SYMBOL = "symbol"
IDENTIFIER = "identifier"
INT_CONST = "integerConstant"
STRING_CONST = "stringConstant"
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
        #running on every word (seperated by spacebar)
        while i < len(buffer):
            buf = buffer[i]
            if '"' in buf:
                #a comment is starting inside this word
                beginning = i
                if buf[i:].count('"') > 1:
                    #comment also ends in this word
                    splitted = buf.split('"')
                    j = 0
                    while j < len(splitted):
                        var = splitted[j]
                        if j == 0 or j == len(splitted) - 1:
                            if var != '':
                                retVal.append(var)
                        else:
                            retVal.append('"' + var + '"')
                        j += 1
                    i += 1
                    continue
                if i == len(buffer) - 1:
                    break
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
        #removing comments
        if '//' in buffer:
            index = buffer.find('//')
            buffer = buffer[:index]

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
            while True:
                if '//' in buffer:
                    index = buffer.find('//')
                    buffer = buffer[:index]
                if '/**' in buffer:
                    while '*/' not in buffer:
                        buffer = self.input_file.readline()
                    index = buffer.find('*/')
                    buffer = buffer[index + 2:]
                if buffer == '\n':
                    if not buffer:
                        # EOF reached
                        return False
                    buffer = self.input_file.readline()
                    continue
                if buffer.split() == []:
                    buffer = self.input_file.readline()
                    continue
                break
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
        try:
            num = int(self.next_word)
            return INT_CONST
        except :
            #do nothing
            x = 0
        if self.next_word[0] == '"' and self.next_word[-1] == '"':
            return STRING_CONST

        #checking using a regular expression if the string is an identifier
        pattern = re.compile(r"[\w]")
        m = pattern.match(self.next_word[0])
        if not m:
            return "Unknown"
        elif m.end() == len(self.next_word[0]):
            return IDENTIFIER

        return "Unknown"

    def keyWord(self):
        return self.next_word

    def symbol(self):
        return self.next_word[0]

    def identifier(self):
        return self.next_word

    def intVal(self):
        retVal = int(self.next_word)
        return retVal

    def stringVal(self):
        #losing the first and last characters (which are ")
        retVal = self.next_word[1:-1]
        return retVal

    def maybe_smart_split(self, line):
        ret = line.split()
        ret = self.join_strings(ret)
        return ret

# def smart_split(line):
#     i = 0
#     retVal = []
#     begin = 0
#     end = 0
#     while i < len(line):
#         if line[i] == '"':
#             begin = i
#             i += 1
#             while line[i] != '"':
#                 i += 1
#             i += 1
#             end = i
#             retVal.append(line[begin:end])
#             print(retVal[0])
#         i += 1


# funcput = "out \"start\" out "
# smart_split(funcput)

#code flow wanted:
#split smartly (space bar and strings)
#for strings change characters inside string - // -> /, /" -> ", /' -> ', same with \
#handle comments (not inside strings) - types - //, /* */,
#split according to other symbols