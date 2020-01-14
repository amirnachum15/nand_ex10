# import JackTokenizer
#
# tokenizer = JackTokenizer.JackTokenizer("text.txt")
# # string = ""
# # while(tokenizer.hasMoreTokens()):
# #     tmp = tokenizer.advance()
# #     string += tmp
# #     print(tmp)
#
# funcput = "out\"comment\"out\"comment\"out\"comment\""
# for val in tokenizer.maybe_smart_split(funcput):
#     print(val)

import SymbolTable

table = SymbolTable.SymbolTable()
table.start_subroutine()
table.define('x', 'int', SymbolTable.VAR)
table.define('y', 'int', SymbolTable.VAR)
print(table.index_of('x'))
print(table.type_of('x'))
print(table.kind_of('x'))
print(table.index_of('y'))
table.start_subroutine()
table.define('x', 'boolean', SymbolTable.VAR)
print(table.index_of('x'))
print(table.type_of('x'))
print(table.kind_of('x'))