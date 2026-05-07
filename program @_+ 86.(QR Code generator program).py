import qrcode
from PIL import Image
import requests
from datetime import datetime
def generate_qr():
    print("cofarm QR Code Generator")
    while True:
        current_time = datetime.now().strftime("%d-%m-%Y_%H%M%S")
        print("Current Date/Time:",current_time)

        data_link = input("Enter anything URL to generate QR Code(q to quite):").strip()


        if data_link.lower() == "q":
            print("Quiting The Cofarm QR Code Generator")
            break

        if not data_link.startswith(("http://","https://")):
            print("Error...: QR Code Data_link URL Must Start with 'https://' or 'http://'")
            continue

        try:
            print("Validating URL...")
            response = requests.get(data_link,timeout = 5)

            if response.status_code == 200:
                print(f"URL is valid  and live >>>")

                qr = qrcode.QRCode(version = 3,box_size = 8,border = 4)
                qr.add_data(data_link)
                qr.make(fit=True)

                img = qr.make_image(fill_color = "black", back_color = "blue")

                filename = f"qr{current_time}.png"
                img.save(filename)
                print(f"File Saved as: {filename}")


                # img.save("qr_code.png")
                #
                # img = Image.open("qr_code.png")

                img.show()

                with open ("qr_code.txt", "a",encoding="utf-8") as file:
                    file.write(f"Generated_Current_Date/Time:[{current_time}\n"
                               f"QR_Code_Generator_URL_Link:{data_link} |Successfully Saved:{filename}\n")
                    print("Successfully Generated Link into QR Code")
            else:
                print(f"Error...website link is not valid and doesn't exist{response.status_code}")

        except requests.exceptions.ConnectionError:
            print("Warning: Failed to establish connection to server..... Check your Internet.")
        except Exception as e:
                 print(f"An unexpected Error Occured: {e}")
        else:
            print("Thank you useing Cofarm QR Code Generator")

if __name__ == "__main__":
    generate_qr()
