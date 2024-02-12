from selenium import webdriver
import sys
# adding Folder_2 to the system path
sys.path.insert(0,r'C:\Users\pundalik.mhamal\OneDrive - ClaySys Technologies\Desktop\Selenium\Automation_Projects\SwagLabs_Automation')
from python_components import PythonComponents

driver = webdriver.Chrome()

#`open the website
PythonComponents.open_website(driver, 'https://www.saucedemo.com/')
PythonComponents.maximize_window(driver)
PythonComponents.sleep(3)

#login
# PythonComponents.send_texts(driver, 'id', 'user-name', 'standard_user')    #enter username
# PythonComponents.sleep(2)
# PythonComponents.send_texts(driver, 'id', 'password', 'secret_sauce')    #enter password
# PythonComponents.sleep(2)
# PythonComponents.click_element(driver, 'id', 'login-button')    #click login button

# PythonComponents.sleep(3)

# # login using custom component
PythonComponents.login(driver, 'standard_user', 'xpath', '//*[@id="user-name"]',
                                'secret_sauce', 'xpath', '//*[@id="password"]', 
                                'id', 'login-button')

PythonComponents.sleep(3)

#click on sort options
PythonComponents.click_element(driver, 'xpath', '//select[@class="product_sort_container"]')

PythonComponents.sleep(3)

#sort by price (high to low)
PythonComponents.click_element(driver, 'xpath', '//option[@value="hilo"]')

PythonComponents.sleep(3)

#add to cart
PythonComponents.click_element(driver, 'xpath','//button[@id="add-to-cart-sauce-labs-backpack"]')
PythonComponents.sleep(2)

#click on the cart icon
PythonComponents.click_element(driver, 'xpath', '//a[@class="shopping_cart_link"]')
PythonComponents.sleep(2)

#click on checkout button
PythonComponents.click_element(driver, 'id', 'checkout')
PythonComponents.sleep(2)

#enter personal details
PythonComponents.send_texts(driver, 'xpath', '', 'atharva')    #enter username
PythonComponents.send_texts(driver, 'id', 'last-name', 'malpekar')    #enter password
PythonComponents.send_texts(driver, 'id', 'postal-code', '123456')    #enter password
PythonComponents.sleep(2)

# PythonComponents.click_element(driver,'id', 'continue')     #click on continue button

# PythonComponents.sleep(2)

# #click on finish button
# PythonComponents.click_element(driver,'id', 'finish')
# PythonComponents.sleep(2)

# #click on sidebar menu
# PythonComponents.click_element(driver,'id', 'react-burger-menu-btn')
# PythonComponents.sleep(2)

# #click on logout
# PythonComponents.click_element(driver,'id', 'logout_sidebar_link')
# PythonComponents.sleep(2)

#closes the browser
PythonComponents.close_browser(driver)