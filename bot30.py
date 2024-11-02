from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import re
import quickstart
import main

url = "https://www.lcbo.com/en/products/beer-cider/ale#t=clp-products-beer_%26_cider-ale&sort=relevancy&layout=card"
class_ = "Beer & Cider"
subtype = "Ale"

main.start(url, class_, subtype)