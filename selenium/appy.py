from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

try: 
    driver = webdriver.Chrome()
    driver.get("https://github.com/login")

    # Ingresar datos inválidos
    driver.find_element(By.ID, "login_field").send_keys("usuario_invalido")
    #driver.find_element(By.ID, "password").send_keys("123")
    password = driver.find_element(By.ID, "password")
    actions = ActionChains(driver)
    actions.click(password)
    actions.send_keys("123")
    actions.perform()
    driver.find_element(By.NAME, "commit").click()

    # Esperar el mensaje de error
    wait = WebDriverWait(driver, 10)
    error_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "flash-error"))
    )

    error_message = error_element.text
    assert "Incorrect username or password." in error_message

    print("Login fallido correctamente detectado")

except Exception as e:
    # Mantener navegador abierto 30 segundos
    time.sleep(30)

    driver.quit()
