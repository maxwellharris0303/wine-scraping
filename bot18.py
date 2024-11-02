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

url = "https://www.lcbo.com/en/products/spirits/gin#t=clp-products-spirits-gin&sort=relevancy&layout=card"
class_ = "Spirits"
subtype = "Gin"

main.start(url, class_, subtype)