lst = [1,True,"Hello",6.9]

lst_of_com = [l for l in lst if l is not None]
print("Not None found in this list",lst_of_com)

if lst[3] == 6.9:
    print(f"this is a float: '{lst[3]}'")
    if lst[2] == "Hello":
        print(f"this is a string: '{lst[2]}'")
        if lst[1] is True:
            print(f"this is a boolean: '{lst[1]}'")
            if lst[0] == 1:
                print(f"this is a integer: '{lst[0]}'")

print("showing the value of list: ",lst)
