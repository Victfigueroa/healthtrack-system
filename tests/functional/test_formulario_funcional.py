# test_formulario_funcional.py
# Edición realizada por Víctor Figueroa
# Prueba funcional usando Selenium para verificar el formulario de actualización de peso

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Ruta local del archivo HTML
ruta_archivo = os.path.abspath("formulario_usuario.html")

# Configuración del driver de Chrome usando Service 
servicio = Service("C:/Users/Olivia/selenium_test_funcional/chromedriver.exe")
driver = webdriver.Chrome(service=servicio)

# Abrir el archivo HTML en el navegador
driver.get("file://" + ruta_archivo)

# Esperar a que cargue
time.sleep(1)

# Llenar el formulario
driver.find_element(By.ID, "nombre").send_keys("Victor")
driver.find_element(By.ID, "peso").send_keys("75")

# Enviar el formulario
driver.find_element(By.TAG_NAME, "button").click()

# Esperar a que aparezca el resultado
time.sleep(1)

# Obtener el resultado
resultado = driver.find_element(By.ID, "resultado").text

# Verificación
assert resultado == "Usuario: Victor, Peso actualizado: 75 kg"

# Finalizar
driver.quit()
