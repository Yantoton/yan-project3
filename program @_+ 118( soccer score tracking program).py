def main():
    print("Welcome To .P<T>M. Soccer score")
    goal = 0
    assist = 0
    foul = 0

    while True:
        option ={
             "1.":"goal",
            "2.":"assist",
            "3.":"foul",
            "4.":"calculate Total Score",
            "'e'.":"to Exit"
        }
        print("\n---Menu---")

        for key,value in option.items():
            print(f"{key}: {value.capitalize()}")

        choice = input("Enter your choice:").lower().strip()
        if choice == "e":
            print("Exiting...Program goodbye")
            break
        try:
            if choice == "1":
                goal = int(input("How many goals scored?:"))
                if goal < 0:
                    print(f"\nThe Goal can't be negative")
                    goal = 0

            elif choice == "2":
                assist = int(input("How many assists? in this match:"))
                if assist < 0:
                    print(f"\nThe Assist can't be negative")
                    assist = 0

            elif choice == "3":
                foul = int(input("How many fouls? in this match:"))
                if foul < 0:
                    print(f"\nThe Foul can't be negative")
                    foul = 0

            elif choice == "4":
                total_score = (goal * 5) + (assist * 3) + (foul * -2)
                print(f"\n[Result] Goal:{goal}, Assist:{assist}, Foul:{foul}, Total Score:{total_score}")

                print(f"\nTotal Score:{total_score}")

            else:
                print("Invalid choice ^_! Select 1-4 or 'e' See you next time")


        except ValueError:
            print("[ERROR]Invalid Input You can enter only integers")
        except Exception as e:
            print(f"[ERROR] An Error Occurred:{e}")
if __name__ == "__main__":
    main()
