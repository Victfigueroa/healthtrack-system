# test_formulario_funcional.py
# Edición realizada por Víctor Figueroa
# Prueba funcional usando Selenium para verificar el formulario de actualización de peso

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920x1080")

service = Service("/usr/bin/google-chrome")  # Chrome ya está instalado con apt

driver = webdriver.Chrome(options=options)
driver.get("http://localhost:8000/formulario_usuario.html")

wait = WebDriverWait(driver, 10)

nombre_input = wait.until(EC.visibility_of_element_located((By.ID, "nombre")))
nombre_input.send_keys("Victor")

peso_input = wait.until(EC.visibility_of_element_located((By.ID, "peso")))
peso_input.send_keys("75")

boton = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
boton.click()

resultado = wait.until(EC.visibility_of_element_located((By.ID, "resultado"))).text
assert resultado == "Usuario: Victor, Peso actualizado: 75 kg"

driver.quit()
