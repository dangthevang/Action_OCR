from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import numpy as np
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
pd.set_option('mode.chained_assignment', None)


class setup():
    
    def __init__(self):
        self.amount = 0
        self.driver = None
        self.path="C:/webdrive/chromedriver.exe"
        pass

    def reset_driver(self):
        self.driver = webdriver.Chrome(executable_path=self.path)

    def push_something_by_id(self, something, path):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, something))
            )
            element.send_keys(path)
        except:
            pass

    def click_something_by_id(self, something):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, something))
            )
            element.click()
        except:
            pass

    def select(self):
        select = Select(self.driver.find_element_by_name(
            'ctl00$MainContent$comboOutput'))
        select.select_by_value("Microsoft Excel (xlsx)")

    def get(self,path_image):
        if self.amount%15 == 0:
            self.reset_driver()
            self.driver.get("https://www.onlineocr.net")
        self.push_something_by_id("fileupload", path_image)
        time.sleep(5)
        self.select()
        time.sleep(5)
        self.click_something_by_id("MainContent_btnOCRConvert")
        time.sleep(5)
        self.click_something_by_id("MainContent_lnkBtnDownloadOutput")
        self.amount+=1