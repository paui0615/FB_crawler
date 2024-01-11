import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = 'https://www.facebook.com'
username = "0952983135"
password = "paui06151226"

image = "/home/paui0615/Github/FB_crawler/DYSB_HV_spec.png"

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-notifications')

driver = webdriver.Chrome(options= options)
driver.get(url)
driver.maximize_window()
time.sleep(2)
element = driver.find_element("name", "email")
element.send_keys(username)
element = driver.find_element("name", "pass")
element.send_keys(password)

element.send_keys(Keys.RETURN)
time.sleep(5)
driver.get('https://www.facebook.com/groups/6873393272716214')


#element = driver.find_element("id", "")"//input[@name='username']"
element = driver.find_element(By.XPATH, "//div[@class='xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe']").click()
time.sleep(8)
element = driver.find_element(By.XPATH, "//div[@aria-label='留個言吧......']")
element.send_keys('Hello world again amd agian!!')
time.sleep(2)
#element = driver.find_element(By.XPATH, "//div[@aria-label='發佈']").click()
#time.sleep(4)
element = driver.find_element(By.XPATH, "//div[@aria-label='相片／影片']").click()
time.sleep(6)

driver.quit()

