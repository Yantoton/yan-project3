def make_even(num):
    if num % 2 == 1:
        return num+1
    else:
        return num
numbers = [111,221,331,43,669,13,5,85,34]
convert_even_numbers = list(map(make_even, numbers))
print(convert_even_numbers)
