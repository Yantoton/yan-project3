import re
for i in dir(__builtins__):
    if re.match("^__.*__$",i):
        print(i)
for x in dir(__builtins__):
    if re.match(r'^[A-Z]',x):
        print(x)
