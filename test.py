from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.lcbo.com/en/josh-cellars-paso-robles-reserve-cabernet-sauvignon-2017-412320")


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="my_store_find_store_button"]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-cookie-allow"]/span'))).click()

driver.get("https://www.lcbo.com/en/josh-cellars-paso-robles-reserve-cabernet-sauvignon-2017-412320")


similar_wines_array = []
similar_products_elements = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ol[class=\"products list items product-items\"]")))
similar_images = similar_products_elements.find_elements(By.TAG_NAME, 'img')
print("sdfsdfsfwerwerWWWWWWWWWWWWWWWWWWWWWWWW")
print(len(similar_images))
for img in similar_images:
    similar_wines_array.append(img.get_attribute('src'))
    
similar_wines_array = [url for url in similar_wines_array if url is not None]
similar_wines = ', '.join(similar_wines_array)
print(similar_wines)



sleep(1000)