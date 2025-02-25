from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = "C:\PROYECTOS\selenium-tutorial\scripts\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")
time.sleep(2)

busqueda_id = driver.find_element(By.ID, "searchInput")
busqueda_id.send_keys("Python (programming language)")
time.sleep(2)
busqueda_id.clear()

busqueda_name = driver.find_element(By.NAME, "search")
busqueda_name.send_keys("Selenium WebDriver")
time.sleep(2)
busqueda_name.clear()

busqueda_class = driver.find_element(By.CLASS_NAME, "search-input input")
busqueda_class.send_keys("Automation Testing")
time.sleep(2)
busqueda_class.clear()

logo = driver.find_element(By.TAG_NAME, "img")
print("Tag Name - Class Text del Logo:", logo.get_attribute("class"))

time.sleep(2)

partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Español")
partial_link_text.click()
time.sleep(2)

driver.back()
time.sleep(2)

busqueda_css = driver.find_element(By.CSS_SELECTOR, "input#searchInput")
busqueda_css.send_keys("CSS Selectors in Selenium")
time.sleep(2)
busqueda_css.clear()

busqueda_xpath = driver.find_element(By.XPATH, "//input[@id='searchInput']")
busqueda_xpath.send_keys("XPath en Selenium")
time.sleep(2)

busqueda_xpath.submit()
time.sleep(4)

driver.quit()
