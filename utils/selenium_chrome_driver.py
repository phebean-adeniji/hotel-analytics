from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def access_chromdriver():
    """
    Login to LinkedIn using Selenium ChromDriver
    """
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    except:
        print("Error using Chrome Web Driver... Will attempt using the local ChromeDriver. \ You can download it here: http://chromedriver.storage.googleapis.com/index.html and copy path. Path may look like this: C:/Users/username/Downloads/chromedriver_win32/chromedriver.exe", "\n")
         # use local path to the downloaded chromedriver instead (http://chromedriver.storage.googleapis.com/index.html). Download a version that is similar to that of your Chrome web browser
        path_to_chromedriver = input("Enter full path to downloaded chromedriver.exe: http://chromedriver.storage.googleapis.com/index.html")
        driver = webdriver.Chrome(executable_path=f'{path_to_chromedriver}')

    return driver