import JackTokenizer

#TODO - fill the API (not a single function does anything)
#TODO - note - when writing to the output file, should write in append mode and not runover the current content

class CompilationEngine:
    def __init__(self, input_file_path, output_file_path):
        self.input_stream = input_file_path
        #don't change this line, this line creates the tokenizer the compilation engine works with
        self.tokenizer = JackTokenizer.JackTokenizer(input_file_path)
        self.output_stream = output_file_path
        self.add_to_me = []

    def get_next_tocken(self):
        if self.tokenizer.hasMoreTokens():
            self.tokenizer.advance()

    def CompileClass(self):
        self.add_to_me.append("<class>\n")

        # class
        self.get_next_tocken()
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append( self.tokenizer.keyWord())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        #class name
        self.get_next_tocken()
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.identifier())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        #{
        self.get_next_tocken()
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        #class var dec*
        self.get_next_tocken()
        while self.tokenizer.keyWord() in [JackTokenizer.FIELD, JackTokenizer.STATIC]:
            self.CompileClassVarDec()

        #class subroutine Dec
        while self.tokenizer.keyWord() in [JackTokenizer.CONSTRUCTOR, JackTokenizer.FUNCTION, JackTokenizer.METHOD]:
            self.CompileSubroutineDec()

        # }
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")


        self.add_to_me.append("</class>\n")

        self.write_to_output_file()

    def CompileClassVarDec(self):
        self.add_to_me.append("<classVarDec>\n")

        #('static' | 'field')
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.keyWord())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        #compileType
        self.get_next_tocken()
        self.CompileType()


        # varName
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.identifier())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()
        while self.tokenizer.symbol()!=";":
            # ,
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.symbol())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            # varName
            self.get_next_tocken()
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.identifier())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            self.get_next_tocken()

        #;
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()

        self.add_to_me.append("</classVarDec>\n")

    def CompileSubroutineDec(self):

        self.add_to_me.append("<subroutineDec>\n")

        # ('constructor' | 'function' | 'method')
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.keyWord())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()
        if self.tokenizer.tokenType()==JackTokenizer.IDENTIFIER:
            # type
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.identifier())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")
        else:
            # void
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.keyWord())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        #subroutineName
        self.get_next_tocken()
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.identifier())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        #(
        self.get_next_tocken()
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        #parameterlist
        self.get_next_tocken()
        self.CompileParameterList()

        # )
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        #subroutineBody
        self.get_next_tocken()
        self.CompileSubroutineBody()

        self.add_to_me.append("</subroutineDec>\n")

    def CompileType(self):
        if self.tokenizer.tokenType() == JackTokenizer.KEYWORD:
            # 'int' | 'char' | 'boolean'
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.keyWord())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")
        else:
            # className
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.identifier())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()

    def CompileSubroutine(self):
        pass

    def CompileSubroutineBody(self):
        self.add_to_me.append("<subroutineBody>\n")
        #{
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()
        #loop over varDec
        while self.tokenizer.keyWord() not in [JackTokenizer.RETURN, JackTokenizer.IF, JackTokenizer.DO,
                                               JackTokenizer.WHILE, JackTokenizer.LET]:
            self.CompileVarDec()

        #statements
        self.CompileStatements()

        # }
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.add_to_me.append("</subroutineBody>\n")
        self.get_next_tocken()

    def CompileParameterList(self):
        self.add_to_me.append("<parameterList>\n")
        if self.tokenizer.next_word == ")":
            self.add_to_me.append("</parameterList>\n")
            return
        #type
        self.CompileType()

        # varName
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.identifier())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()

        while self.tokenizer.tokenType() == JackTokenizer.SYMBOL:
            if self.tokenizer.symbol() != ",":
                break
            # ,
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.symbol())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            # type
            self.get_next_tocken()
            self.CompileType()

            # varName
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.identifier())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            self.get_next_tocken()
        self.add_to_me.append("</parameterList>\n")

    def CompileVarDec(self):
        #adding varDec
        self.add_to_me.append("<varDec>\n")

        # var
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.keyWord())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        #type
        self.get_next_tocken()
        self.CompileType()

        #varName
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.identifier())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()
        while self.tokenizer.symbol() == ",":
            # ,
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.symbol())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            # varName
            self.get_next_tocken()
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.identifier())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            self.get_next_tocken()

        # ;
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()

        #closing add varDec
        self.add_to_me.append("</varDec>\n")

    def CompileStatements(self):
        self.add_to_me.append("<statements>\n")
        statements_starts = [JackTokenizer.RETURN, JackTokenizer.IF, JackTokenizer.DO,
                                               JackTokenizer.WHILE, JackTokenizer.LET]
        while self.tokenizer.tokenType() == JackTokenizer.KEYWORD:
            if self.tokenizer.keyWord() not in statements_starts:
                break

            if self.tokenizer.keyWord() == JackTokenizer.RETURN:
                self.CompileReturn()

            elif self.tokenizer.keyWord() == JackTokenizer.IF:
                self.CompileIf()

            elif self.tokenizer.keyWord() == JackTokenizer.DO:
                self.CompileDo()

            elif self.tokenizer.keyWord() == JackTokenizer.WHILE:
                self.CompileWhile()

            elif self.tokenizer.keyWord() == JackTokenizer.LET:
                self.CompileLet()

        self.add_to_me.append("</statements>\n")

    def CompileDo(self):
        self.add_to_me.append("<doStatement>\n")
        # do
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.keyWord())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        #subroutineCall
        self.get_next_tocken()
        self.CompilesubroutineCall()

        # ;
        self.add_to_me.append("<symbol>")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</symbol>\n")

        self.add_to_me.append("</doStatement>\n")

        self.get_next_tocken()

    def CompileLet(self):

        self.add_to_me.append("<letStatement>\n")

        # let
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.keyWord())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        # varName
        self.get_next_tocken()
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.identifier())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()

        if self.tokenizer.symbol() == "[":
            # [
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.symbol())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            self.get_next_tocken()
            # expression
            self.CompileExpression()

            # ]
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.keyWord())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            self.get_next_tocken()

        # =
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.keyWord())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()
        #expression
        self.CompileExpression()

        # ;
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.keyWord())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.add_to_me.append("</letStatement>\n")

        self.get_next_tocken()

    def CompileWhile(self):
        self.add_to_me.append("<whileStatement>\n")

        # while
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.keyWord())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        # (
        self.get_next_tocken()
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()
        # expression
        self.CompileExpression()

        # )
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        # {
        self.get_next_tocken()
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        #statements
        self.get_next_tocken()
        self.CompileStatements()

        # }
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.add_to_me.append("</whileStatement>\n")

        self.get_next_tocken()

    def CompileReturn(self):
        self.add_to_me.append("<returnStatement>\n")

        # return
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.keyWord())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()
        if self.tokenizer.tokenType() == JackTokenizer.SYMBOL:
            if self.tokenizer.symbol() ==";":
                # ;
                self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
                self.add_to_me.append(self.tokenizer.keyWord())
                self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")
                self.add_to_me.append("</returnStatement>\n")
                self.get_next_tocken()
                return

        self.CompileExpression()

        # ;
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.keyWord())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.add_to_me.append("</returnStatement>\n")
        self.get_next_tocken()

    def CompileIf(self):
        self.add_to_me.append("<ifStatement>\n")

        # if
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.keyWord())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        # (
        self.get_next_tocken()
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()
        # expression
        self.CompileExpression()

        # )
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        # {
        self.get_next_tocken()
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        # statements
        self.get_next_tocken()
        self.CompileStatements()

        # }
        self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
        self.add_to_me.append(self.tokenizer.symbol())
        self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

        self.get_next_tocken()
        if self.tokenizer.tokenType() == JackTokenizer.KEYWORD:
            if self.tokenizer.keyWord() == JackTokenizer.ELSE:
                # else
                self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
                self.add_to_me.append(self.tokenizer.keyWord())
                self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

                # {
                self.get_next_tocken()
                self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
                self.add_to_me.append(self.tokenizer.symbol())
                self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

                # statements
                self.get_next_tocken()
                self.CompileStatements()

                # }
                self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
                self.add_to_me.append(self.tokenizer.symbol())
                self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")
                self.get_next_tocken()

        self.add_to_me.append("</ifStatement>\n")

    def CompileExpression(self):
        self.add_to_me.append("<expression>\n")


        self.CompileTerm()
        if self.tokenizer.tokenType() == JackTokenizer.SYMBOL:
            if self.tokenizer.symbol() in ['+','-','*','/', '&', '|', '<', '>', '=']:
                if self.tokenizer.symbol() == '<':
                    # <
                    self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
                    self.add_to_me.append("&lt;")
                    self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

                elif self.tokenizer.symbol() == ">":
                    # >
                    self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
                    self.add_to_me.append("&gt;")
                    self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")
                elif self.tokenizer.symbol() == '&':
                    # &
                    self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
                    self.add_to_me.append("&amp;")
                    self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")
                else:
                    # op
                    self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
                    self.add_to_me.append(self.tokenizer.symbol())
                    self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

                self.get_next_tocken()
                self.CompileTerm()

        if self.add_to_me[-2] == "<term>\n":
            self.add_to_me = self.add_to_me[:-3]
            return

        self.add_to_me.append("</expression>\n")

    def CompileTerm(self):

        self.add_to_me.append("<term>\n")

        if self.tokenizer.tokenType() == JackTokenizer.INT_CONST:
            # int_const
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.intVal())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")
            self.get_next_tocken()
        elif self.tokenizer.tokenType() == JackTokenizer.SYMBOL:
            if self.tokenizer.symbol() == "(":
                # (
                self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
                self.add_to_me.append(self.tokenizer.symbol())
                self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

                #expression
                self.get_next_tocken()
                self.CompileExpression()

                # )
                self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
                self.add_to_me.append(self.tokenizer.symbol())
                self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")
                self.get_next_tocken()
            elif self.tokenizer.symbol() in ['-', '~']:
                # adding the unary op
                self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
                self.add_to_me.append(self.tokenizer.symbol())
                self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

                #compile term
                self.get_next_tocken()
                self.CompileTerm()
        elif self.tokenizer.tokenType() == JackTokenizer.STRING_CONST:
            # str_const
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.stringVal())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")
            self.get_next_tocken()

        elif self.tokenizer.tokenType() == JackTokenizer.KEYWORD:
            # keybword_const
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.keyWord())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")
            self.get_next_tocken()
        elif self.tokenizer.tokenType() == JackTokenizer.IDENTIFIER:
            # varName / subroutineCall / varName[Expression]
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.identifier())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            self.get_next_tocken()
            if self.tokenizer.tokenType() == JackTokenizer.SYMBOL:
                if self.tokenizer.symbol()=="[":
                    # [
                    self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
                    self.add_to_me.append(self.tokenizer.symbol())
                    self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

                    self.get_next_tocken()
                    # expression
                    self.CompileExpression()

                    # ]
                    self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
                    self.add_to_me.append(self.tokenizer.symbol())
                    self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")
                    self.get_next_tocken()

                if self.tokenizer.symbol() in ['.', '(']:
                    self.CompilesubroutineCall(have_first=True)

        self.add_to_me.append("</term>\n")

    def CompileExpressionList(self):
        self.add_to_me.append("<expressionList>\n")

        self.CompileExpression()
        while True:
            if self.tokenizer.tokenType() != JackTokenizer.SYMBOL:
                break
            if self.tokenizer.symbol() != ",":
                break
            # ,
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.symbol())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            #expression
            self.get_next_tocken()
            self.CompileExpression()

        self.add_to_me.append("</expressionList>\n")

    def CompilesubroutineCall(self, have_first = False):
        # subroutineName / class name / var name
        if not have_first:
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.identifier())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            self.get_next_tocken()
        if self.tokenizer.symbol()=="(":
            # (
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.symbol())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            #ExpressionList
            self.get_next_tocken()
            self.CompileExpressionList()

            # )
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.symbol())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")
            self.get_next_tocken()
        else:
            #.
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.symbol())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            self.get_next_tocken()
            # subroutineName
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.identifier())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            # (
            self.get_next_tocken()
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.symbol())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")

            # ExpressionList
            self.get_next_tocken()
            self.CompileExpressionList()

            # )
            self.add_to_me.append("<" + self.tokenizer.tokenType() + ">")
            self.add_to_me.append(self.tokenizer.symbol())
            self.add_to_me.append("</" + self.tokenizer.tokenType() + ">\n")
            self.get_next_tocken()

    def write_to_output_file(self):
        file = open(self.output_stream, "w+")
        for word in self.add_to_me:
            file.write(str(word))
        file.close()