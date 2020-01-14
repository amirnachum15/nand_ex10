import JackTokenizer

tokenizer = JackTokenizer.JackTokenizer("text.txt")
# string = ""
# while(tokenizer.hasMoreTokens()):
#     tmp = tokenizer.advance()
#     string += tmp
#     print(tmp)

funcput = "out\"comment\"out\"comment\"out\"comment\""
for val in tokenizer.maybe_smart_split(funcput):
    print(val)