from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

file = open('log.txt', 'w')
#driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument('--headless')
driver = webdriver.Chrome(options=option)

driver.get('https://html5css.ru/howto/howto_js_rangeslider.php')
driver.maximize_window()

sleep(1)

slider = driver.find_element(By.XPATH, '//*[@id="id2"]')
action = ActionChains(driver)
sleep(2)
action.click_and_hold(slider).move_by_offset(-300, 0).release().perform()

file.close()