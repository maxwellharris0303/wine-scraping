from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import re
import quickstart

def start(url, class_, subtype):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)


    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="my_store_find_store_button"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-cookie-allow"]/span'))).click()

    def scroll_down(driv):
        page_height = driv.execute_script("return document.body.scrollHeight")
        scroll_distance = page_height // 5
        driv.execute_script(f"window.scrollTo(0, {scroll_distance});")
        sleep(0.3)
        driv.execute_script(f"window.scrollTo({scroll_distance}, {scroll_distance * 2});")
        sleep(0.3)
        driv.execute_script(f"window.scrollTo({scroll_distance * 2}, {scroll_distance * 3});")
        sleep(0.3)
        driv.execute_script(f"window.scrollTo({scroll_distance * 3}, {scroll_distance * 4});")
        sleep(0.3)
        driv.execute_script(f"window.scrollTo({scroll_distance * 4}, {page_height});")

    driver.get(url)

    # while(True):
    #     try:
    #         scroll_down(driver)
    #         loadMoreButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id=\"loadMore\"]")))
    #         if loadMoreButton.get_attribute('style') == "display: block;":
    #             loadMoreButton.click()
    #         # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loadMore"]'))).click()
    #     except:
    #         break
    scroll_down(driver)
    list_contaier = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"coveo-result-list-container coveo-card-layout-container\"]")))

    products_list_elements = list_contaier.find_elements(By.CSS_SELECTOR, "div[class=\"coveo-product-items\"]")

    product_driver = webdriver.Chrome()
    product_driver.maximize_window()
    product_driver.get("https://www.lcbo.com/en/products#t=clp-products&sort=relevancy&layout=card")

    WebDriverWait(product_driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="my_store_find_store_button"]'))).click()
    WebDriverWait(product_driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-cookie-allow"]/span'))).click()
    for product in products_list_elements:
        try:
            product_url = product.find_element(By.TAG_NAME, 'a').get_attribute('href')
            # print(product_url)
            # sleep(100)
            product_driver.get(product_url)
            scroll_down(product_driver)
            # sleep(5)
            try:
                name = WebDriverWait(product_driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[3]/div[2]/div/div[2]/h1/span'))).text   
            except:
                name = "None"
            # print(f'Name: {name}')
            try:
                description = WebDriverWait(product_driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[3]/div[4]/div[1]/div/div/div'))).text   
            except:
                description = "None"
            # print(f'Description: {description}')
            try:
                volume_string = WebDriverWait(product_driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[3]/div[2]/div/div[7]/div[1]'))).text
                # volumes = re.findall(r'\d+(?:\.\d+)?', volume_string)
                # volume = volumes[0]

                # string = "3 x 50 ml bottle"

                matches = re.findall(r"\d+\s*x\s*\d+", volume_string)
                if matches:
                    volume = matches[0]
                    print(volume)
                else:
                    volumes = re.findall(r'\d+(?:\.\d+)?', volume_string)
                    volume = volumes[0]

            except:
                volume = "None"
            # print(f'Volume: {volume}')
            # sleep(1000)
            try:
                food_paring_parent = WebDriverWait(product_driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"lcbo-product-details-container desktop-view-container\"]")))
                # print(moredetail_parent)
                food_paring_child = food_paring_parent.find_element(By.CSS_SELECTOR, "div[class=\"foodParings pip-info\"]")
                # print(moredetail_child)
                list_tags = food_paring_child.find_elements(By.TAG_NAME, 'li')
                # print(len(list_tags))
                flavours = ""
                sweetness = None
                body = None
                flavour_intensity = None
                tannins = None
                acidity = None
                for list in list_tags:
                    list_category = list.find_element(By.CSS_SELECTOR, "div[class=\"label\"]")
                    list_value = list.find_element(By.CSS_SELECTOR, "div[class=\"value\"]")
                    if list_category.text == "Flavours":
                        flavours = list_value.text
                    if list_category.text == "Sweetness":
                        darkdot_elements = list_value.find_elements(By.CSS_SELECTOR, "span[class=\"darkdot dot\"]")
                        sweetness = len(darkdot_elements)
                    if list_category.text == "Body":
                        darkdot_elements = list_value.find_elements(By.CSS_SELECTOR, "span[class=\"darkdot dot\"]")
                        body = len(darkdot_elements)
                    if list_category.text == "Flavour Intensity":
                        darkdot_elements = list_value.find_elements(By.CSS_SELECTOR, "span[class=\"darkdot dot\"]")
                        flavour_intensity = len(darkdot_elements)
                    if list_category.text == "Tannins":
                        darkdot_elements = list_value.find_elements(By.CSS_SELECTOR, "span[class=\"darkdot dot\"]")
                        tannins = len(darkdot_elements)
                    if list_category.text == "Acidity":
                        darkdot_elements = list_value.find_elements(By.CSS_SELECTOR, "span[class=\"darkdot dot\"]")
                        acidity = len(darkdot_elements)     
            except:
                pass
            
            try:
                moredetail_parent = WebDriverWait(product_driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"lcbo-product-details-container desktop-view-container\"]")))
                # print(moredetail_parent)
                moredetail_child = moredetail_parent.find_element(By.CSS_SELECTOR, "div[id=\"moredetail\"]")
                # print(moredetail_child)
                list_tags = moredetail_child.find_elements(By.TAG_NAME, 'li')
                # print(len(list_tags))
                abv = None
                location = None
                country = None
                producer = None
                sugar = None
                varietal = None
                release_date = None
                for list in list_tags:
                    list_category = list.find_element(By.CSS_SELECTOR, "div[class=\"label\"]")
                    list_value = list.find_element(By.CSS_SELECTOR, "div[class=\"value\"]")
                    if list_category.text == "Alcohol/Vol":
                        abv_text = list_value.text
                        abvs = re.findall(r'\d+(?:\.\d+)?', abv_text)
                        abv = abvs[0]
                    if list_category.text == "Made In":
                        country_string = list_value.text
                        parts = country_string.split(", ")
                        try:
                            location = parts[0]
                            country = parts[1]
                        except:
                            location = country_string
                            country = country_string
                    if list_category.text == "By":
                        producer = list_value.text
                    if list_category.text == "Sugar Content":
                        sugar = list_value.text
                    if list_category.text == "Varietal":
                        varietal = list_value.text
                    if list_category.text == "Release Date":
                        release_date = list_value.text     
            except:
                pass
            
            try:
                vintage_parent = WebDriverWait(product_driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"product attribute sku\"]")))
                vintage_string = vintage_parent.find_element(By.CSS_SELECTOR, "strong[class=\"type\"]").text
                if vintage_string == "VINTAGES#:":
                    vintage = True
                else:
                    vintage = False
            except:
                vintage = False

            try:
                best_seller_parent = WebDriverWait(product_driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"product-info-main\"]")))
                best_seller_string = best_seller_parent.find_element(By.CSS_SELECTOR, "div[class=\"amlabel-text\"]").text
                if best_seller_string == "Best Seller":
                    best_seller = True
                else:
                    best_seller = False
            except:
                best_seller = False
            try:
                price_parent = WebDriverWait(product_driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class=\"price-container price-final_price tax weee\"]")))
                price_elements = price_parent.find_elements(By.CSS_SELECTOR, "span[class=\"price\"]")
                for price_element in price_elements:
                    try:
                        price_text = price_element.text
                    except:
                        pass

            # Check if the text contains the "$" symbol
                if "$" in price_text:
                    price = price_text
                # print(f'Price: {price}')
            except:
                price = "None"

            try:
                total_alcohol_ml = float(volume) * float(abv) / 100
            except:
                total_alcohol_ml = "None"
            # print(f'Total_alcohol_ml: {total_alcohol_ml}')
            
            
            try:
                rating_element = WebDriverWait(product_driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"bv_avgRating_component_container notranslate\"]")))
                rating = rating_element.text
            except:
                rating = "0"
            # print(f'Rating: {rating}')

            try:
                image_element = WebDriverWait(product_driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[class=\"fotorama__img\"]")))
                image = image_element.get_attribute('src')
            except:
                image = "None"
            # print(f'Image: {image}')

            # try:
            #     similar_wines_array = []
            #     similar_products_elements = WebDriverWait(product_driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ol[class=\"products list items product-items\"]")))
            #     similar_images = similar_products_elements.find_elements(By.TAG_NAME, 'img')
            #     print("sdfsdfsfwerwerWWWWWWWWWWWWWWWWWWWWWWWW")
            #     print(len(similar_images))
            #     for img in similar_images:
            #         similar_wines_array.append(img.get_attribute('src'))
            #     similar_wines_array = [url for url in similar_wines_array if url is not None]
            #     similar_wines = ', '.join(similar_wines_array)
            # except:
            #     similar_wines = "None"
            # # print(similar_wines)
            try:
                similar_wines_sku_array = []
                similar_products_elements = WebDriverWait(product_driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ol[class=\"products list items product-items\"]")))
                similar_skus = similar_products_elements.find_elements(By.CSS_SELECTOR, "a[class=\"product photo product-item-photo\"]")
                print(len(similar_skus))
                for sku in similar_skus:
                    similar_wines_sku_array.append(sku.get_attribute('data-sku'))
                similar_wines_sku_array = [sku for sku in similar_wines_sku_array if sku is not None]
                similar_wines = ', '.join(similar_wines_sku_array)
            except:
                similar_wines = "None"

            try:
                product_id = WebDriverWait(product_driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[itemprop=\"sku\"]"))).text
            except:
                product_id = "None"

            try:
                print(f'Product_id: {product_id}')
            except:
                product_id = "None"
                print("None")
            try:
                print(f'Name: {name}')
            except:
                name = "None"
                print("None")
            try:
                print(f'Description: {description}')
            except:
                description = "None"
                print("None")
            try:
                print(f'Volume: {volume}')
            except:
                volume = "None"
                print("None")
            try:
                print(f'ABV: {abv}')
            except:
                abv = "None"
                print("None")
            try:
                print(f'Location: {location}')
            except:
                location = "None"
                print("None")
            try:
                print(f'Country: {country}')
            except:
                country = "None"
                print("None")
            try:
                print(f'Producer: {producer}')
            except:
                producer = "None"
                print("None")
            try:
                print(f'Release_date: {release_date}')
            except:
                release_date = "None"
                print("None")
            try:
                print(f'Vintage: {vintage}')
            except:
                vintage = "None"
                print("None")
            try:
                print(f'Best Seller: {best_seller}')
            except:
                best_seller = "None"
                print("None")
            try:
                print(f'Price: {price}')
            except:
                price = "None"
                print("None")
            try:
                print(f'Sugar content: {sugar}')
            except:
                sugar = "None"
                print("None")
            try:
                print(f'Flavours: {flavours}')
            except:
                flavours = "None"
                print("None")
            try:
                print(f'Sweetness: {sweetness}')
            except:
                sweetness = "None"
                print("None")
            try:
                print(f'Body: {body}')
            except:
                body = "None"
                print("None")
            try:
                print(f'Flavour Intensity: {flavour_intensity}')
            except:
                flavour_intensity = "None"
                print("None")
            try:
                print(f'Tannins: {tannins}')
            except:
                tannins = "None"
                print("None")
            try:
                print(f'Acidity: {acidity}')
            except:
                acidity = "None"
                print("None")
            try:
                print(f'Total_alcohol_ml: {total_alcohol_ml}')
            except:
                total_alcohol_ml = "None"
                print("None")
            try:
                print(f'Varietal: {varietal}')
            except:
                varietal = "None"
                print("None")
            try:
                print(f'Class: {class_}')
            except:
                class_ = "None"
                print("None")
            try:
                print(f'Subtype: {subtype}')
            except:
                subtype = "None"
                print("None")
            try:
                print(f'Rating: {rating}')
            except:
                rating = "None"
                print("None")
            try:
                print(f'Image: {image}')
            except:
                image = "None"
                print("None")
            try:
                print(f'Similar Wines: {similar_wines}')
            except:
                similar_wines = "None"
                print("None")

            quickstart.main()
            columnCount = quickstart.getColumnCount()
            RANGE_DATA = f'wine!A{columnCount + 2}:AH'

            quickstart.insert_data(RANGE_DATA,
                                    product_id, name, description, volume, abv, location, country, producer, release_date, vintage, best_seller, "", price, sugar, flavours,
                                    sweetness, body, flavour_intensity, tannins, acidity, total_alcohol_ml, varietal, "", "", class_, subtype, rating, "", "", "", "", image, "", similar_wines)
        except:
            pass

    driver.quit()
    print("Done!")