from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # Importa Service
import time

# Ruta del ChromeDriver
driver_path = "./scripts/chromedriver.exe"

# Crea una instancia de Service con la ruta del ChromeDriver
service = Service(driver_path)

# Inicializa el navegador con el servicio
driver = webdriver.Chrome(service=service)

# Abre Google
driver.get("https://www.google.com")

# Espera 2 segundos para que cargue la página
time.sleep(2)

# Encuentra el cuadro de búsqueda y escribe "Selenium con Python"
busqueda = driver.find_element(By.NAME, "q")
busqueda.send_keys("Selenium con Python")

# Envía la búsqueda
busqueda.submit()

# Espera 3 segundos para ver los resultados
time.sleep(3)

# Cierra el navegador
driver.quit()
