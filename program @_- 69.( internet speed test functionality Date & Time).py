import speedtest as st

from datetime import datetime

def test_Speed_Test():
    print("Welcome P.T.M. Checking Internet Speed Test")
    try:
        test = st.Speedtest()

        print("Checking Internet Download Speed Test")
        down_speed = test.download()
        down_speed = round(down_speed / 10 ** 6, 2)


        print("Checking Internet Upload Speed Test")
        up_speed = test.upload()
        up_speed = round(up_speed / 10**6, 2)


        ping = test.results.ping

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        print(f"Current Time : {current_time}")

        print(f"Download Speed :{down_speed} Mbps")

        print(f"Upload Speed :{up_speed} Mbps")

        print(f"Ping:{ping} Ms")

        with open ("speed_test.txt","a") as file:
            file.write(f"\n___Current Checking The Internet Connection Date&Time___---{current_time}---")
            file.write(f"\nDownload Speed :{down_speed} Mbps"
                       f"\nUpload Speed :{up_speed} Mbps"
                       f"\nPing :{ping} ")
    except Exception as e:
        print(f"Error Occured{e}")
    else:
        print("Testing Completed\nData Store in File successfully")
    finally:
        print("Thank You For Using This Program")

if __name__ == "__main__":
    test_Speed_Test()
