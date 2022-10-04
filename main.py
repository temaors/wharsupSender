from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
import os
import pickle

options = webdriver.FirefoxOptions()
options.add_argument('--allow-profiles-outside-user-dir')
options.add_argument('--enable-profile-shortcut-manager')
options.add_argument(r'user-data-dir=C:\Users\temao\AppData\Roaming\Mozilla\Firefox\Profiles\vvvw94wi.default-release')
options.add_argument('--profile-directory=Profile 1')
options.add_argument('--profiling-flush=30')
options.add_argument('-enable-aggressive-domstorage-flushing')

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)


file_path = "D:/proj/sources.txt"

if os.path.isfile(file_path):
    text_file = open(file_path, "r")
    data = text_file.readlines()
    text_file.close()
count = 0


def makeRequest(line):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    driver.get(line)
    for cookie in cookies:
        print("loaded cookie")
        driver.add_cookie(cookie)
    driver.implicitly_wait(20)
    time.sleep(40)
    #driver.find_element(By.XPATH, "//button[@class='tvf2evcx oq44ahr5 lb5m6g5c svlsagor p2rjqpw5 epia9gcq']").click()
    print("Reference : {}".format(line.strip()))
    print(driver.get_cookies())
    print("Cookie")
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

for line in data:
    count+=1
    makeRequest(line)
    time.sleep(10)

    print("Reference {}: {}".format(count, line.strip()))

