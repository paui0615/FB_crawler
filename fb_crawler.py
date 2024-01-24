import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def Initialize_Chrome():
    options = webdriver.ChromeOptions()
    prefs = {
        'profile.default_content_setting_values':
        {
            'notifications': 2
        }
    }
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-extensions')

# Setting username, password and image path
url = 'https://www.facebook.com'
username = "username"
password = "password"
image = "image path"
fb_group = ""fb group url

Initialize_Chrome()
driver = webdriver.Chrome(options= options)

# Login system
driver.get(url)
driver.maximize_window()
time.sleep(2)
element = driver.find_element("name", "email")
element.send_keys(username)
element = driver.find_element("name", "pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
time.sleep(5)


# Click on the post area
driver.get('fb_group')
element = driver.find_element(By.XPATH, "//div[@class='xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe']")
time.sleep(3)

# Attach the image file
file_input = driver.find_element(By.XPATH, "//input[@accept='image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv']")
file_input.send_keys(image)
time.sleep(3)

# Leave a message
element = driver.find_element(By.XPATH, "//div[@aria-label='留個言吧......']")
element.send_keys('TEST')

# Click the publish button
element = driver.find_element(By.XPATH, "//div[@aria-label='發佈']")
driver.execute_script("arguments[0].click();", element)

time.sleep(5)
driver.quit()

