import pandas as pd
import numpy as np

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

URL = "https://www.emlakjet.com/satilik-daire/kars/"


driver = webdriver.Firefox()
driver.get(URL)
sleep(60)

verify = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/div/div[1]/table/tbody/tr/td[1]/div[1]/div/label/map/area')
verify.click()