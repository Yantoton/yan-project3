user_input = int(input("Enter The Number:"))
sum = 0
temp = user_input

while temp > 0:
    digit = temp % 10
    cube = digit ** 3
    sum = sum + cube
    temp //= 10
if sum == user_input:
    print("It is an armstrong number.")
else:
    print("Not an armstrong number!..")
