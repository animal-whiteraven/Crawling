from selenium import webdriver
import os
import time

if __name__ == '__main__':
    chromedriver = os.path.dirname(os.path.abspath(__file__)) + "/../chromedriver.exe" # download chromedriver path
    driver = webdriver.Chrome(chromedriver)

    driver.get('https://www.binance.com/ko/futures/XRPUSDT') # open url
    driver.implicitly_wait(5) # wait page loading

    for i in range(0, 5):
        price = driver.find_element('xpath' ,'//*[@id="futuresOrderbook"]/div[3]/div[2]/div[1]') # get xpath element
        print(price.text) # print price
        time.sleep(5) #wait 5 sec

    time.sleep(10) # wait 10 sec
    driver.close()