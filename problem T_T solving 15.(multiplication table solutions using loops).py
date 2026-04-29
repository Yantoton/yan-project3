# Solving-1 (Using For Loop)
user_num = int(input("Enter any number to Multiplication:"))

for i in range(1,11):
  
    print(f"{i} x {user_num} = {i * user_num}")

#Solving-2 (Using While Loop)

num = int(input("Enter any number to Multiplication:"))

y = 1
while y <= 10:
    print(f"{num} x{y} = {num * y}")
    y += 1
