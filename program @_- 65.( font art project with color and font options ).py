import pyfiglet
from termcolor import colored

def font_art():
    print("<<< Welcome To Font Art Project ! >>>")
    valid_colors = ['blue','red','green','yellow']
    while  True:
        text = input("Type your text(OR type 'quit' to exit):").strip()
        if text.lower() == "quit":
            print("Quitting...👋🏻 Goodbye..!")
            break
        font = input("Enter font you want to use(press enter to default):").strip()
        color = input(f"Enter valid color{valid_colors}:").strip().lower()
        try:
            if font:
                formated_text = pyfiglet.figlet_format(text,font=font)
            else:
                formated_text = pyfiglet.figlet_format(text)
            if color in valid_colors:
               print(colored(formated_text,color))
            else:
                if color:
                    print(f"Invalid:'{color}' is not supported. color for this program")
                print(formated_text)
        except pyfiglet.FontError:
            print(f"Invalid font type:_Error_:Font '{font}' is not supported.\nPlease Try Again Using default font")
        except Exception as e:
            print(f"An Error Occurred :_{e}")
        except ValueError:
            print("invalid programing massage .\nenter a valid font text .\nyou can enter only STR text.")

if __name__ == "__main__":
    font_art()
