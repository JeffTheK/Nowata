import lang

code = "(print (str hello))"

print(lang.tokenize(code))
print(lang.parse(code))
lang.exec_file('testfile.nv')