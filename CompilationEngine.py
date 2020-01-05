import JackTokenizer

#TODO - fill the API (not a single function does anything)
#TODO - note - when writing to the output file, should write in append mode and not runover the current content

class CompilationEngine:
    def __init__(self, input_file_path, output_file_path):
        self.input_stream = input_file_path
        #don't change this line, this line creates the tokenizer the compilation engine works with
        self.tokenizer = JackTokenizer.JackTokenizer(input_file_path)
        self.output_stream = output_file_path
    def CompileClass(self):
        return True

    def CompileClassVarDec(self):
        return True

    def CompileSubroutine(self):
        return True

    def CompileParameterList(self):
        return True

    def CompileVarDec(self):
        return True

    def CompileStatements(self):
        return True

    def CompileDo(self):
        return True

    def CompileLet(self):
        return True

    def CompileWhile(self):
        return True

    def CompileReturn(self):
        return True

    def CompileIf(self):
        return True

    def CompileExpression(self):
        return True

    def CompileTerm(self):
        return True

    def CompileExpressionList(self):
        return True
