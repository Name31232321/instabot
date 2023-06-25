from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)



driver.get("https://wrtn.ai/")
driver.implicitly_wait(3)

driver.find_element(By.NAME,'textarea').send_keys('안녕')