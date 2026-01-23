# 📘 Verificación y Validación de Software

Este repositorio contiene un **conjunto completo y progresivo de ejercicios** para la asignatura **Verificación y Validación de Software**, pensados para clases en **institutos tecnológicos y universidades**.

El enfoque va más allá de escribir pruebas: se busca que el estudiante **analice requisitos, diseñe casos de prueba, detecte errores y valide sistemas reales**, combinando teoría y práctica.

---

## 🎯 Objetivos de Aprendizaje

- Diferenciar claramente **Verificación vs Validación**
- Diseñar **casos de prueba efectivos**
- Aplicar técnicas clásicas de testing
- Identificar errores, riesgos y ambigüedades
- Automatizar pruebas usando **pytest**
- Evaluar la calidad del software

---

## 🧩 1. Verificación de Requisitos

### Enunciado
Dado el siguiente requisito:

> *"El sistema debe permitir registrar estudiantes mayores de 17 años."*

### Actividades
- Identificar casos válidos
- Identificar casos inválidos
- Identificar casos límite
- Determinar si el requisito es **claro o ambiguo**

📌 **Objetivo:** verificar si el requisito está bien definido y es comprobable.

---

## 🧪 2. Diseño de Casos de Prueba (sin código)

### Enunciado
```python
def calcular_descuento(edad, es_estudiante):
    pass
```

### Actividades
- Diseñar una **tabla de casos de prueba**
- Definir entradas, salidas esperadas y tipo de prueba
- Identificar pruebas positivas y negativas

📌 **Objetivo:** pensar antes de programar.

---

## 🎯 3. Partición de Equivalencia

### Enunciado
Sistema que recibe una **nota entre 0 y 10**.

### Actividades
- Identificar clases de equivalencia válidas
- Identificar clases inválidas
- Seleccionar un valor representativo por clase

📌 **Objetivo:** reducir el número de pruebas sin perder cobertura.

---

## 🧱 4. Análisis de Valores Límite

### Enunciado
El sistema acepta edades entre **18 y 65 años**.

### Casos sugeridos
- 17, 18, 19
- 64, 65, 66

📌 **Objetivo:** detectar errores en los bordes del sistema.

---

## 🧨 5. Pruebas Negativas

### Enunciado
```python
def registrar_usuario(email, password):
    pass
```

### Actividades
- Email vacío
- Email sin @
- Password muy corta
- Tipos de datos incorrectos

📌 **Objetivo:** validar robustez y manejo de errores.

---

## 🔄 6. Pruebas de Regresión

### Enunciado
1. Se entrega una versión funcional del sistema
2. Se modifica una función existente
3. Una funcionalidad deja de funcionar

📌 **Objetivo:** entender el valor real del testing automatizado.

---

## 🧪 7. Verificación vs Validación

### Actividad
Clasificar como **Verificación** o **Validación**:
- Revisión de código fuente
- Pruebas unitarias
- Pruebas con usuarios reales
- Validación de requisitos

---

## 🧠 8. Detección de Errores

### Enunciado
```python
def dividir(a, b):
    return a / b
```

### Actividades
- Identificar errores
- Proponer pruebas
- Mejorar la función

---

## 🧰 9. Matriz de Trazabilidad

Relacionar **requisitos ↔ casos de prueba** y verificar cobertura.

---

## 🔐 10. Pruebas de Seguridad (Básico)

Diseñar pruebas para una función de login considerando entradas inválidas.

---

## 🧪 11. Pruebas Manuales vs Automáticas

Comparar cuándo usar cada tipo de prueba y justificar.

---

## 🧪 12. Automatización con Pytest

Implementar pruebas automáticas para validaciones, cálculos y excepciones.

---

## 🎓 13. Mini Proyecto Integrador

Sistema simple de gestión de notas académicas con requisitos, pruebas y reporte de errores.

---

📘 **Asignatura:** Verificación y Validación de Software  
🎓 **Nivel:** Ingeniería en Software  
🧪 **Herramientas:** Pytest, testing manual y automatizado

