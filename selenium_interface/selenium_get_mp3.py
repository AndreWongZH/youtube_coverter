"""
Input youtube_link in textfield and navigate to the download button
"""
import time
from selenium import webdriver


def youtube_to_mp3(youtube_link):

    # Change the default download location to Desktop
    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": r"C:\Users\cascasm\Desktop\\"}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(executable_path="A:\Coding projects\main projects folder\youtube_converter\\venv\chromedriver.exe",
                              chrome_options=chrome_options)
    driver.get("http://convert2mp3.net/en/index.php")

    elem = driver.find_element_by_id(id_="urlinput")
    elem.clear()
    elem.send_keys(youtube_link)
    elem.submit()

    # Processing the youtube video (give 15sec)
    print("Processing youtube video now ...")
    time.sleep(15)

    elem = driver.find_element_by_partial_link_text("Skip this page")
    elem.click()

    # Downloading the mp3 file (give 30sec)
    print("Downloading mp3 file right now ...")
    elem = driver.find_element_by_partial_link_text("Download")
    elem.click()
    time.sleep(30)
    print("Download complete :D")

    driver.close()
