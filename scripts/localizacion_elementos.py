from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Ruta del ChromeDriver (ajusta según tu sistema operativo)
driver_path = "./scripts/chromedriver.exe"

# Crear un objeto Service para el ChromeDriver
service = Service(driver_path)

# Inicializa el navegador utilizando el servicio
driver = webdriver.Chrome(service=service)

# Abre Wikipedia
driver.get("https://www.wikipedia.org/")

# Espera 2 segundos para que cargue la página
time.sleep(2)

# Localización por ID
busqueda_id = driver.find_element(By.ID, "searchInput")
busqueda_id.send_keys("Python (programming language)")
time.sleep(2)
busqueda_id.clear()  # Limpiar el cuadro de búsqueda

# Localización por NAME
busqueda_name = driver.find_element(By.NAME, "search")
busqueda_name.send_keys("Selenium WebDriver")
time.sleep(2)
busqueda_name.clear()

# Localización por CLASS_NAME
busqueda_class = driver.find_element(By.CLASS_NAME, "search-input input")
busqueda_class.send_keys("Automation Testing")
time.sleep(2)
busqueda_class.clear()

# Localización por TAG_NAME
logo = driver.find_element(By.TAG_NAME, "img")
print("Tag Name - Class Text del Logo:", logo.get_attribute("class"))

# Localización por LINK_TEXT(ESTA DENTRO DE UN STRONG DENTRO DEL A POR ESO USARE PARTIAL_LINK_TEXT)
# link_text = driver.find_element(By.LINK_TEXT, "English")
# link_text.click()
# time.sleep(2)

# #Volver a la página principal
# driver.back()
time.sleep(2)

# Localización por PARTIAL_LINK_TEXT
partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Español")
partial_link_text.click()
time.sleep(2)

# Volver a la página principal
driver.back()
time.sleep(2)

# Localización por CSS_SELECTOR
busqueda_css = driver.find_element(By.CSS_SELECTOR, "input#searchInput")
busqueda_css.send_keys("CSS Selectors in Selenium")
time.sleep(2)
busqueda_css.clear()

# Localización por XPATH
busqueda_xpath = driver.find_element(By.XPATH, "//input[@id='searchInput']")
busqueda_xpath.send_keys("XPath en Selenium")
time.sleep(2)

# Enviar la búsqueda
busqueda_xpath.submit()

# Espera para ver los resultados
time.sleep(4)

# Cierra el navegador
driver.quit()
