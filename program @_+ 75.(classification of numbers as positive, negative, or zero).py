number = [-7,0,786]

result = list(map(lambda x: "positive" if x > 0 else ("Negative" if x < 0 else "Zero"),number))
print(result)
