# test_formulario_funcional.py
# Edición realizada por Víctor Figueroa
# Prueba funcional usando Selenium para verificar el formulario de actualización de peso

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Obtengo la ruta absoluta del archivo HTML local
ruta_archivo = os.path.abspath("formulario_usuario.html")

# Configuro opciones para Chrome en modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Verifico si estoy en entorno CI/CD (GitHub Actions)
selenium_url = os.getenv("SELENIUM_REMOTE_URL")

if selenium_url:
    # En entorno CI/CD uso Selenium remoto
    driver = webdriver.Remote(command_executor=selenium_url, options=chrome_options)
else:
    # En entorno local utilizo chromedriver desde mi máquina
    servicio = Service("C:/Users/Olivia/selenium_test_funcional/chromedriver.exe")
    driver = webdriver.Chrome(service=servicio, options=chrome_options)

# Abro el archivo HTML en el navegador
driver.get("http://localhost:8000/formulario_usuario.html")

# Espero que cargue el formulario
time.sleep(1)

# Lleno el formulario con los datos
driver.find_element(By.ID, "nombre").send_keys("Victor")
driver.find_element(By.ID, "peso").send_keys("75")

# Hago clic en el botón
driver.find_element(By.TAG_NAME, "button").click()

# Espero la respuesta
time.sleep(1)

# Obtengo el resultado y lo verifico
resultado = driver.find_element(By.ID, "resultado").text
assert resultado == "Usuario: Victor, Peso actualizado: 75 kg"

# Cierro el navegador
driver.quit()

