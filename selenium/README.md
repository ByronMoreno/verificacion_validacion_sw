
# 🧪 Taller de Verificación y Validación con Python y Selenium

Este repositorio contiene un **taller práctico completo** para la asignatura **Verificación y Validación de Software**, orientado a estudiantes de Ingeniería / Tecnología en Software.

El taller está diseñado para que el estudiante aprenda a **automatizar pruebas funcionales reales**, comprendiendo el rol del testing automatizado dentro del ciclo de vida del software.

---

## 📌 Información general

- **Asignatura:** Verificación y Validación de Software  
- **Modalidad:** Taller práctico 
- **Lenguaje:** Python  
- **Herramienta:** Selenium WebDriver  

---

## 🎯 Objetivos de aprendizaje

Al finalizar el taller, el estudiante será capaz de:

- Comprender el rol de Selenium en la Verificación y Validación.
- Automatizar pruebas funcionales sobre aplicaciones web.
- Diseñar y ejecutar casos de prueba automatizados.
- Validar resultados esperados mediante assertions.
- Detectar errores reales en aplicaciones web.
- Aplicar buenas prácticas de testing automatizado.

---

## 🧠 Enfoque en Verificación y Validación

Selenium se utiliza principalmente para:

- Pruebas funcionales
- Pruebas de regresión
- Pruebas de aceptación

> Selenium no reemplaza las pruebas manuales, las complementa.

---

## 📋 Requisitos previos

### Conocimientos

- Programación básica en Python
- Conceptos básicos de testing
- HTML básico (inputs, botones, formularios)

### Software

- Python 3.10 o superior
- Google Chrome o Firefox
- Visual Studio Code

---

## ⚙️ Instalación del entorno

```bash
pip install selenium
pip install webdriver-manager
```

Verificar instalación:

```bash
python -c "import selenium; print(selenium.__version__)"
```

---

## 🧪 Caso de prueba 1: Abrir navegador

**Objetivo:** Verificar que el navegador se abre correctamente.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
driver.maximize_window()
```

**Resultado esperado:** Se abre Google sin errores.

---

## 🔍 Localización de elementos

Métodos más utilizados:

- By.ID
- By.NAME
- By.CLASS_NAME
- By.TAG_NAME
- By.XPATH
- By.CSS_SELECTOR

Ejemplo:

```python
from selenium.webdriver.common.by import By

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.submit()
```

---

## ✅ Validación de resultados (Assertions)

**Caso de prueba 2:** Verificar el título de la página.

```python
assert "Selenium" in driver.title
```

---

## ⏳ Esperas explícitas

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
elemento = wait.until(EC.presence_of_element_located((By.XPATH, "//h3")))
```

---

## 🌐 Sitio de práctica

Se utilizará el siguiente sitio para pruebas:

https://the-internet.herokuapp.com

---

## 🧪 Ejercicios prácticos

### Ejercicio 1: Login válido
- Ingresar credenciales correctas
- Validar acceso exitoso

### Ejercicio 2: Login inválido
- Ingresar credenciales incorrectas
- Validar mensaje de error

```python
error = driver.find_element(By.ID, "flash").text
assert "invalid" in error.lower()
```

---

## 🧱 Estructura de un caso de prueba

1. Precondiciones
2. Pasos
3. Datos de prueba
4. Resultado esperado
5. Resultado obtenido

---

## 🧪 Introducción a Pytest (opcional)

Instalación:

```bash
pip install pytest
```

Ejemplo:

```python
def test_titulo_google(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
```

---

## 🧼 Buenas prácticas

- Un test = una validación
- No usar time.sleep()
- Usar esperas explícitas
- Nombrar correctamente los casos de prueba
- Separar lógica de prueba y lógica de negocio

---

## 📝 Actividad evaluada

Automatizar **3 casos de prueba**:

- 1 caso exitoso
- 1 caso fallido
- 1 caso límite

### Entregables

- Código fuente
- Documento breve con los casos de prueba

---


## 🧠 Reflexión final

> Automatizar pruebas no es solo programar, es **pensar como tester**.
