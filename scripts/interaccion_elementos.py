from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Ruta del ChromeDriver (ajústala según tu sistema)
driver_path = "./scripts/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Abre la página de Wikipedia
driver.get("https://www.wikipedia.org/")

# Hacer clic en el botón "English" para ir a la versión en inglés
english_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "English"))
)
english_button.click()

time.sleep(2)

# Hacer clic en "Log in" en la esquina superior derecha
login_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Log in"))
)
login_link.click()

time.sleep(2)

# Esperar que aparezca el formulario de inicio de sesión
username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "wpName1"))
)
password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "wpPassword1"))
)

# Ingresar texto en los campos (NO presionar "Submit" por seguridad)
username_field.send_keys("usuario_prueba")
password_field.send_keys("contraseña_prueba")

time.sleep(2)

# Encontrar y hacer clic en la casilla "Mantener sesión iniciada"
keep_logged_in = driver.find_element(By.ID, "wpRemember")
keep_logged_in.click()

time.sleep(2)

# Encontrar el botón de inicio de sesión y mostrar su estado
login_button = driver.find_element(By.ID, "wpLoginAttempt")
print("¿El botón de inicio de sesión está habilitado?", login_button.is_enabled())

# No enviamos el formulario para evitar intentos de inicio de sesión real

# Espera 3 segundos para visualizar los cambios
# WebDriverWait(driver, 3)

# Cerrar el navegador
driver.quit()
