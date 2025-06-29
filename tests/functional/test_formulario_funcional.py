# test_formulario_funcional.py
# Edición realizada por Víctor Figueroa
# Prueba funcional usando Selenium para verificar el formulario de actualización de peso

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Configurar el driver para usar el Selenium Grid (Docker) en GitHub Actions
SELENIUM_REMOTE_URL = "http://localhost:4444/wd/hub"

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor=SELENIUM_REMOTE_URL,
    options=options
)

# URL del formulario servido en el runner (puerto 8000)
url = "http://localhost:8000/formulario_usuario.html"

driver.get(url)

wait = WebDriverWait(driver, 10)  # espera hasta 10 segundos

# Esperar y llenar el campo nombre
nombre_input = wait.until(EC.visibility_of_element_located((By.ID, "nombre")))
nombre_input.send_keys("Victor")

# Esperar y llenar el campo peso
peso_input = wait.until(EC.visibility_of_element_located((By.ID, "peso")))
peso_input.send_keys("75")

# Esperar y clicar el botón
boton = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
boton.click()

# Esperar a que aparezca el resultado
resultado = wait.until(EC.visibility_of_element_located((By.ID, "resultado"))).text

assert resultado == "Usuario: Victor, Peso actualizado: 75 kg"

driver.quit()
