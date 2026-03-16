
import requests

def check_url():
      print("checking the valid url 'OR' Type 'q' to Stop The program ")
      while True:
            check_side = input("Enter url to check:")
            if check_side .lower() in ["Exit","quit"]:
                  print("Exiting program>>>💔🔚❕")
                  break
            if not check_side.startswith(('http://','https://')):
                  print("Error...❌: URl start with 'https://' or 'http://'")
                  continue
            try:
                  response = requests.get(check_side,timeout=5)
                  if response.status_code == 200:
                        print(f"Entry {check_side} valid URL...✔🐱‍💻")
                        with open ("URL.txt","a") as f:
                              f.write(f"This is a valid:' {check_side} ':URl site\n")
                  else:
                        print(f"Error {check_side} invalid URL..❌")

            except requests.exceptions.ConnectionError:
                  print("Warning:Failed to establish connection to server..❌")
            except requests.exceptions.Timeout:
                  print("Request timed out.Try again later..❌")
            except requests.exceptions.TooManyRedirects:
                  print("Request :TooManyRedirect..❌")
            except requests.exceptions.MissingSchema:
                  print("Request invalid format....: MissingSchema..❌")
            else:
                  print("Successfully connected to server💻✔👩🏻‍💻")
            finally:
                  print("🔚 Out from the program")


if __name__ == "__main__":
      check_url()
  
