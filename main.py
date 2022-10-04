import random
import zipfile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
import os

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

file_path = "./sources.txt"

if os.path.isfile(file_path):
    text_file = open(file_path, "r")
    data = text_file.readlines()
    text_file.close()
count = 0

def makeRequest(line):
    driver.get(line)
    driver.implicitly_wait(20)
    time.sleep(20)
    driver.find_element(By.XPATH, "//button[@class='tvf2evcx oq44ahr5 lb5m6g5c svlsagor p2rjqpw5 epia9gcq']").click()
    sleeping = random.randint(250,360)
    print(sleeping)
    time.sleep(sleeping)
    print("Request: {}".format(line.strip()))


for line in data:
    count += 1
    makeRequest(line.replace("api", "web", 1))
