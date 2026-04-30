a = 0
b = 1
fibo_num = int(input("Enter Number Here:"))

for count in range(1, fibo_num + 1):
    c = a+b
    a = b
    b = c
    print(c)
