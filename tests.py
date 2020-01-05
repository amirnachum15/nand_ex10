import JackTokenizer
import re

pattern = re.compile(r"[\w]")
string_test = "a;"
m = pattern.match(string_test)
if not m:
    print("no match")
elif m.end() == len(string_test):
    print("match")
else:
    print("no match")

# tokenizer = JackTokenizer.JackTokenizer("text.txt")
# string = ""
# while(tokenizer.hasMoreTokens()):
#     tmp = tokenizer.advance()
#     string += tmp
#     print(tmp)