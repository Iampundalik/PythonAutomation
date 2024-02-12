from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Action:
    
    # find element:
    def find_element_(driver, by, element):
        try:
            match by:
                case "id":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, element)))
                    return driver.find_element(By.ID, element)
                case "xpath":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, element)))
                    return driver.find_element(By.XPATH, element)
                case "name":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, element)))
                    return driver.find_element(By.NAME, element)
                case "class":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, element)))
                    return driver.find_element(By.CLASS_NAME, element)
                case "tag":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, element)))
                    return driver.find_element(By.TAG_NAME, element)
                case "link":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, element)))
                    return driver.find_element(By.LINK_TEXT, element)
                case "partial_link":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, element)))
                    return driver.find_element(By.PARTIAL_LINK_TEXT, element)
                case "css":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
                    return driver.find_element(By.CSS_SELECTOR, element)
        except:
            raise Exception("Element not found")

    # find elements
    def find_elements_(driver, by, element):
        try:
            match by:
                case "id":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, element)))
                    return driver.find_element(By.ID, element)
                case "xpath":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, element)))
                    return driver.find_element(By.XPATH, element)
                case "name":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, element)))
                    return driver.find_element(By.NAME, element)
                case "class":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, element)))
                    return driver.find_element(By.CLASS_NAME, element)
                case "tag":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, element)))
                    return driver.find_element(By.TAG_NAME, element)
                case "link":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, element)))
                    return driver.find_element(By.LINK_TEXT, element)
                case "partial_link":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, element)))
                    return driver.find_element(By.PARTIAL_LINK_TEXT, element)
                case "css":
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
                    return driver.find_element(By.CSS_SELECTOR, element)
        except:
            raise Exception("Element not found")

    # Open website
    def open_url(driver, url):
        try:
           driver.get(url)
           WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        except:
            raise Exception("Could not open url")

    # click element
    def click_element(driver, by, element):
        try:
            Action.find_element_(driver, by, element).click()
        except:
            raise Exception("Element not found")

    # send text
    def send_text(driver, by, element, text):
        try:
            Action.find_element_(driver, by, element).send_keys(text)
        except:
            raise Exception("Could not send text")

    # send keys
    def send_key(driver, by, element, key):
        try:
            Action.find_element_(driver, by, element).send_keys(Keys.ENTER)
        except:
            raise Exception("Could not send keys")

    # get text
    def get_texts(driver, by, element):
        try:
            return Action.find_element_(driver, by, element).text
        except:
            raise Exception("Could not get text")

    # move down
    def move_down(driver):
        try:
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        except:
            raise Exception("Could not move down")

    # move up
    def move_up(driver):
        try:
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
        except:
            raise Exception("Could not move up")

    def sleep(seconds):
        try:
            import time
            time.sleep(seconds)
        except:
            raise Exception("Could not sleep")

    # maximize window
    def max_window(driver):
        try:
            driver.maximize_window()
        except:
            raise Exception("Could not maximize window")
            
    # switch tab
    def switch_tab(driver, tab):
        try:
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(tab+1))
            driver.switch_to.window(driver.window_handles[tab])
        except:
            raise Exception("Could not switch tab")

    # close tab
    def close_tab(driver):
        try:
            driver.close()
        except:
            raise Exception("Could not close tab")

    # refresh page
    def refresh_page(driver):
        try:
            driver.refresh()
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        except:
            raise Exception("Could not refresh page")

    # close browser
    def close_browser(driver):
        try:
            driver.close()
        except:
            raise Exception("Could not close browser")

    # get title
    def get_title(driver):
        try:
            return driver.title
        except:
            raise Exception("Could not get title")

    # verify if selected
    def verify_selected(driver, by, element):
        try:
            return Action.find_element_(driver, by, element).is_selected()
        except:
            raise Exception("Could not verify")

    # take screenshot
    def take_screenshot(driver, name):
        try:
            driver.save_screenshot(name)
        except:
            raise Exception("Could not take screenshot")