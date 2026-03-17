prime_num = int(input("Enter A Prime_number:"))
if prime_num == 1:
      print(f"{prime_num} is not a prime number")
if prime_num > 1:
      for prime in range(2, prime_num):
            if prime_num % prime == 0:
                  print(f"{prime_num} is not a prime number")
                  break
      else:
            print(f"{prime_num} is a prime number")
