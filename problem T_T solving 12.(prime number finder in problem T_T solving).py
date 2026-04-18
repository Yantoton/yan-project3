lower = int(input("Enter lower limit number here:"))

upper = int(input("Enter upper limit number here:"))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(f"This is a prime number:{num}")
