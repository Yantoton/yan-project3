import os
from pytube import YouTube
from datetime import datetime

def yt_download ():

    print("P.T.M YouTube Downloader")
    while True:
        current = datetime.now().strftime("%Y_%m_%d +_- %H_%M_%S")
        print(current)
        video_link = input("Enter YouTube Video Link (q to quit):").strip()
        if video_link.lower() in ["q", "quit"]:
              print("Quitting P.T.M YouTube Downloader...")
              break
        if not video_link.startswith(("http://","https://")):
                print("Error....: Downloding Link URl Start with 'http://' or 'https://'")
                continue
        try:

            yt = YouTube(video_link)
            print(f"Title:{yt.title}")

            stream =  yt.streams.get_highest_resolution()
            stream.download()
            with open ("Video_Downloaded.txt" , "a",encoding="utf-8") as file:
                    file.write(f"Download_Current DateTime: [{current}]"
                               f"\nVideo Title:{yt.title}"
                              f"\n Download video Link:{video_link}")
            print("Download Completed Successfully")




        except Exception as e:
            print(f"Error Occured: {e}")
            print("Tip: if you get Regex errors,pytube might be outdated.Try 'pip Install ++upgrade pytube'")
        except pytube.exceptions.connectionError:
            print("Warning: Connection Error")

        else:
            print("program is working")

if __name__ == "__main__":
    yt_download()
