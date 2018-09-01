"""
Youtube to mp3 downloader
Uses the website: http://convert2mp3.net/en/index.php to download youtube files

Two ways to pass inputs:
    1) Command-line Interface
            Just type in the youtube link you want to download (you can download only one)
    2) Text file
            Type in the .txt file location and the program will read from it

    Choose either "cli" or "txt"

"""
from selenium_interface.selenium_get_mp3 import youtube_to_mp3

while True:
    try:
        print("Do you want to pass input through Command-line Interface or Text file?")
        option = input("Type <cli> or <txt>: ").lower()
        print("\n")

        # Raise an error if input is not cli or txt
        if (option == "cli" or option == "txt"):
            break
        else:
            print("Incorrect input, please choose either <cli> or <txt>\n")
            raise Exception()
    except:
        pass

if option == "cli":
    youtube_link = input("Enter youtube link here: \n")
    youtube_to_mp3(youtube_link=youtube_link)

elif option == "txt":
    path_link = input("Enter path to your .txt file: \n")

    # Opening and reading of file lines
    text_file = open(file=path_link, mode='r')
    list_of_link = [link.strip() for link in text_file.readlines()]
    text_file.close()

    for each_link in list_of_link:
        youtube_to_mp3(youtube_link=each_link)
