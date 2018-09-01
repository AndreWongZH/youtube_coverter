
"""
Input youtube_link in textfield and navigate to the download button
"""
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def youtube_to_mp3(youtube_link):

    # Change the default download location to Desktop
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : r"C:\Users\cascasm\Desktop"}
    chromeOptions.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(executable_path="A:\Coding projects\main projects folder\youtube_converter\\venv\chromedriver.exe")
    driver.get("http://convert2mp3.net/en/index.php")


    # elem = driver.find_elements_by_tag_name("option")
    # for option in elem:
    #     if option.text == "mp4":
    #         option.click()
    #         break



    select = Select(driver.find_element_by_id("select_main"))
    print(select.options)
    select.select_by_visible_text("mp4")
    time.sleep(20)

    driver.close()

youtube_to_mp3("https://www.youtube.com/watch?v=nNuVX_77FCM&index=110&list=PLNxnuTrgdxoelnHS53ohx6coZY6IwFbnS&t=0s")