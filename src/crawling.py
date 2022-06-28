from selenium import webdriver
import os
import time

if __name__ == '__main__':
    chromedriver = os.path.dirname(os.path.abspath(__file__)) + "/../chromedriver.exe" # download chromedriver path
    driver = webdriver.Chrome(chromedriver)

    driver.get('https://www.binance.com/ko/futures/XRPUSDT') # open url
    driver.implicitly_wait(5) # wait page loading

    time.sleep(10) # wait 10 sec
    driver.close()