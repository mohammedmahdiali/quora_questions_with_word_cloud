from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd

def get_questions(keyword):

    CONST_MAIN_URL = "https://ar.quora.com/search?q="
    CONST_SCROLL_PAUSE_TIME = 20
    keyword = keyword

    opts = webdriver.ChromeOptions()
    opts.add_argument("--window-size=400,400")
    driver = webdriver.Chrome('chromedriver.exe', chrome_options=opts)

    driver.get(CONST_MAIN_URL+keyword)

    counter = 0
    while counter < 40:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(CONST_SCROLL_PAUSE_TIME)
        counter += 1

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    spans = soup.find_all('span', class_='qu-userSelect--text')

    questions = []
    for span in spans:
        questions.append(span.text)

    pd.Series(questions).to_excel("data.xlsx")
    driver.close()

if __name__ == '__main__':
    get_questions("بغداد")