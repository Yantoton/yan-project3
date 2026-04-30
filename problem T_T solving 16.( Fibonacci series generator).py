x = 0
y = 1

num = int(input("Enter the fibonacci series number:"))

if num == 0:
    print(x)
else:
    print(x)
    print(y)
    for count in range(1, num + 1):
        z = x + y
        x = y
        y = z
        print(z)

