list = []

while True:
    banner = f"""____________________________________________________
                welcome Programin Language Database:{chr(10).join(list)}
                
                _____________________________________________________"""

    print(banner)
    print("1-Adding The programmin languge in Data_base")
    print("2-Removing The programmin languge in Data_base")

    option_items = {
        1 : "Add Programmin",
        2 : "Remove Programmin",
        #3 : "Change Programmin",
        }

    for key,value in option_items.items():
        print(f"{key}:{value}")

    data_base = input("Enter your choice_(1:2 OR Ouit)_:")
    if data_base == "Quit":
        print("Quiting Program Language Database")
        break

    try:
            option = int(data_base)
            if option ==1:
                add_programmin=input("add a program languge:")
                list.append(add_programmin)
                print(f"successfully '{add_programmin}' language Add in Data_base",list)
                with open("test.txt","a") as file:
                    file.write(f"Added {add_programmin} :program in list{list}\n")
            elif option ==2:
                remove_programmin = input("remove a program languge:")
                if remove_programmin in list:
                    list.remove(remove_programmin)
                    print(f"successfully '{remove_programmin}' language Remove in Data_base", list)
                    with open("test.txt", "a") as file:
                        file.write(f"Removed {remove_programmin}:program in list{list}\n")
                else:
                    print("No Languge Found in list")
            else:
                print("Invalid Choice")
    except ValueError:
            print(f"Invalid_Input\nThe_{ValueError}_String_Is_Not_Definded\nEnter_Only_Integer_OR_Quit_Program\nPlease_Try_Again")
    except Exception as e:
            print("Invalid Input Enter the  Valid Value ")
    else:
            print("Program Language Database Updated")
    finally:
            print("Program Finished Here!!.....*_>")
