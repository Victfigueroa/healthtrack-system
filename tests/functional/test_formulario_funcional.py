# test_formulario_funcional.py
# Edición realizada por Víctor Figueroa
# Prueba funcional usando Selenium para verificar el formulario de actualización de peso

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

SELENIUM_REMOTE_URL = os.environ.get("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")

options = webdriver.ChromeOptions()
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")

# Habilitar acceso a localhost desde contenedor
options.add_argument("--host-resolver-rules=MAP localhost 127.0.0.1")

driver = webdriver.Remote(
    command_executor=SELENIUM_REMOTE_URL,
    options=options
)

url = "http://localhost:8000/formulario_usuario.html"
driver.get(url)

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

