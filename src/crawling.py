from selenium import webdriver
import os
import time
from pymongo import MongoClient
from datetime import datetime

def selenium_test():
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


def mongodb_test():
    client = MongoClient(host='localhost', port=27017)
    db = client['coin']

    db.coin.delete_many({})

    for i in range(0, 5):
        data = {
            'coin_name' : 'XRP',
            'date' : datetime.now(),
            'price' : 0
        }

        db.coin.insert_one(data)

    print("count : " + str(db['coin'].count_documents({})))
    for d in db['coin'].find():
        print(d)

    db.coin.delete_many({})

    print("count : " + str(db['coin'].count_documents({})))


if __name__ == '__main__':
    # selenium_test()
    mongodb_test()