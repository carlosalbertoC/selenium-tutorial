from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = "C:\PROYECTOS\selenium-tutorial\scripts\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

english_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "English"))
)
english_button.click()

time.sleep(2)

login_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Log in"))
)
login_link.click()

time.sleep(2)

username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "wpName1"))
)
password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "wpPassword1"))
)

username_field.send_keys("usuario_prueba")
password_field.send_keys("contraseña_prueba")

time.sleep(2)

keep_logged_in = driver.find_element(By.ID, "wpRemember")
keep_logged_in.click()

time.sleep(2)

login_button = driver.find_element(By.ID, "wpLoginAttempt")
print("¿El botón de inicio de sesión está habilitado?", login_button.is_enabled())

driver.quit()
