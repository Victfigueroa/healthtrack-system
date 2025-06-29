# test_formulario_funcional.py
# Edición realizada por Víctor Figueroa
# Prueba funcional usando Selenium para verificar el formulario de actualización de peso

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
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
time.sleep(1)

driver.find_element(By.ID, "nombre").send_keys("Victor")
driver.find_element(By.ID, "peso").send_keys("75")

driver.find_element(By.TAG_NAME, "button").click()

time.sleep(1)

resultado = driver.find_element(By.ID, "resultado").text

assert resultado == "Usuario: Victor, Peso actualizado: 75 kg"

driver.quit()
