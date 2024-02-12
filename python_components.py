import sys
sys.path.insert(0,r'C:\Users\pundalik.mhamal\OneDrive - ClaySys Technologies\Desktop\Selenium\Automation_Projects\SwagLabs_Automation')
from action import Action

class PythonComponents:

    step=1

    # print step and increment
    def display_step():
        print(f'Step {PythonComponents.step} => ', end =" ")
        PythonComponents.step+=1

    # Open website
    def open_website(driver, url):
        PythonComponents.display_step()
        Action.open_url(driver, url)
        print('Website opened = '+ url)

    # find element
    def find_element(driver, by, element):
        PythonComponents.display_step()
        Action.find_element(driver,by, element)
        print('Element found = '+ by +":"+element)

    # find elements
    def find_elements(driver, by, element):
        PythonComponents.display_step()
        Action.find_elements(driver,by, element)
        print('Elements found = '+ by +":"+element)

    # click element
    def click_element(driver, by, element):
        PythonComponents.display_step()
        Action.click_element(driver,by, element)
        print('Element clicked = '+ by +":"+element)

    # send text
    def send_texts(driver, by, element, text):
        PythonComponents.display_step()
        Action.send_text(driver, by, element, text)
        print('Text sent = '+text+'\n'+"\t\t\t"+ by +":"+element)

    # send keys
    def send_keys(driver, by, element, key):
        PythonComponents.display_step()
        Action.send_key(driver, by, element, key)
        print('Keys sent = '+key+'\n'+ by +":"+element)

    # select radio button
    def select_radio_button(driver, by, element):
        PythonComponents.display_step()
        Action.click_element(driver, by, element)
        print('Radio button selected = '+ by +":"+element)

    # select checkbox
    def select_checkbox(driver, by, element):
        PythonComponents.display_step()
        Action.click_element(driver, by, element)
        print('Checkbox selected = '+ by +":"+element)

    # maximize window
    def maximize_window(driver):
        PythonComponents.display_step()
        Action.max_window(driver)
        print('Window maximized')
        
    # move down
    def move_down(driver):
        PythonComponents.display_step()
        Action.move_down(driver)
        print('Moved down')

    # move up
    def move_up(driver):
        PythonComponents.display_step()
        Action.move_up(driver)
        print('Moved up')

    # get text
    def get_text(driver, by, element):
        PythonComponents.display_step()
        print("Text : "+Action.get_texts(driver, by, element)+'\n'+"\t\t\t"+ by +":"+element)

    # verify text
    def verify_text(driver, by, element, text):
        PythonComponents.display_step()
        if Action.get_texts(driver, by, element) == text:
            print('Text verified = '+ text +'\n'+"\t\t\t"+ by +":"+element)
        else:
            raise Exception("Text not verified")

    # get title
    def get_title(driver):
        PythonComponents.display_step()
        print(Action.get_title(driver))
        print('Got title')

    # verify title
    def verify_title(driver, title):
        PythonComponents.display_step()
        if Action.get_title(driver) == title:
            print('Title verified = '+ title)
        else:
            raise Exception("Title not verified")

    # Verify checkbox is selected
    def verify_checkbox_selected(driver, by, element):
        PythonComponents.display_step()
        if Action.verify_selected(driver, by, element):
            print('Checkbox selected = '+ by +":"+element)
        else:
            raise Exception("Checkbox not selected")

    # Verify radio button is selected
    def verify_radio_button_selected(driver, by, element):
        PythonComponents.display_step()
        if Action.verify_selected(driver, by, element):
            print('Radio button selected = '+ by +":"+element)
        else:
            raise Exception("Radio button not selected")

    # sleep
    def sleep(time):
        Action.sleep(time)
        print('Sleeping = '+ str(time))

    # switch to tab
    def switch_to_tab(driver, tab):
        PythonComponents.display_step()
        Action.switch_tab(driver, tab)
        print(f'Switched tab : {tab}')

    # close browser
    def close_browser(driver):
        PythonComponents.display_step()
        Action.close_browser(driver)
        print('Browser closed')
    
    # close tab
    def close_current_tab(driver):
        PythonComponents.display_step()
        Action.close_tab(driver)
        print('Current tab closed')

    #login
    def login(driver, username, username_method, username_element, password, password_method, password_element, submit_method, submit_element):
        PythonComponents.display_step()
        Action.send_text(driver, username_method, username_element, username)
        Action.send_text(driver, password_method, password_element, password)
        Action.click_element(driver, submit_method, submit_element)
        print('Login successful')


# assert "No results found." not in driver.page_source