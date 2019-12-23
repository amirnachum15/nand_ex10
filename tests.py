import JackTokenizer

tokenizer = JackTokenizer.JackTokenizer("text.txt")
string = ""
while(tokenizer.hasMoreTokens()):
    tmp = tokenizer.advance()
    string += tmp
    print(tmp)