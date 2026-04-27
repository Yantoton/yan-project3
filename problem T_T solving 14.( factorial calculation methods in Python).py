#solving_way -1 Using Forloop

num = int(input("Enter the number here:"))
fact_num = 1

if num < 0:
    print("factorial of 0 dose not exist")
if num == 0:
    print("factorial of 0 is",1)
if num > 0:

    for i in range (1,num + 1):
        fact_num = fact_num * i
print("the factorial of given number is",fact_num)

# solving_way -2  Using Recursion

def fact_(num):
    if num == 0:
        return 1
    else:
        return num * fact_(num - 1)

num = int(input("Enter the number here:"))
print(fact_(num))
