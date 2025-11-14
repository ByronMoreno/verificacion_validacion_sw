
# 🌈📘 **Clase: Cómo Elaborar un Plan de Pruebas para Calidad de Software**  

Bienvenido a esta guía completa y colorida para enseñar a tus estudiantes a crear un **Plan de Pruebas profesional**, con ejemplos, emojis y secciones visualmente atractivas. ✨  

---

## 🎯 **Objetivos de la Clase**

- 📌 Comprender qué es un Plan de Pruebas y su importancia en QA.  
- 🧩 Identificar todas sus secciones clave.  
- 🛠️ Elaborar un Plan de Pruebas completo.  
- 🧪 Diseñar casos de prueba bien estructurados.  
- 📊 Reconocer métricas, riesgos y cronograma.

---

## 🧠 **1. ¿Qué es un Plan de Pruebas?**

Un **Plan de Pruebas** es un documento formal que define:  
👉 **qué, cómo, cuándo y quién** realizará las pruebas para garantizar la calidad del software.  

Sirve como **mapa guía** para que el equipo de QA ejecute el proceso de testing de manera organizada y profesional.  

---

## 📄 **2. Secciones del Plan de Pruebas**

### 🏷️ **2.1 Portada**
- 📘 Título del documento  
- 🧪 Proyecto bajo prueba  
- 👥 Autor(es)  
- 🗓️ Fecha y versión  

### 📝 **2.2 Introducción**
- Descripción general del sistema  
- Propósito del documento  

### 🎯 **2.3 Alcance**
- ✅ Qué se prueba  
- ❌ Qué no se prueba  

### 🎯 **2.4 Objetivos de Pruebas**
- Validar requisitos funcionales  
- Evaluar rendimiento  
- Detectar regresiones  

### 🚪 **2.5 Criterios de Entrada (Entry Criteria)**
- ✔️ Build estable  
- ✔️ Casos de prueba listos  
- ✔️ Datos disponibles  

### 🚪 **2.6 Criterios de Salida (Exit Criteria)**
- 🚫 Defectos críticos corregidos  
- 🟩 Casos críticos aprobados  

### 🧭 **2.7 Enfoque de Pruebas**
- 🧪 Tipos: unitarias, integración, sistema, aceptación  
- ✋ Pruebas manuales vs 🤖 automatizadas  
- 🛠️ Herramientas (Postman, Selenium, JMeter, etc.)  

### 🧪 **2.8 Casos de Prueba**
Estructura:  
- ID  
- Título  
- Prioridad  
- Precondiciones  
- Pasos  
- Datos  
- Resultado esperado  
- Resultado real  
- Estado  

### 👥 **2.9 Recursos y Roles**
- 👑 QA Lead  
- 🧪 Testers  
- 👨‍💻 Developers de apoyo  
- ⚙️ Herramientas  

### 📅 **2.10 Cronograma**
Fechas y duración de actividades clave.  

### 📦 **2.11 Entregables**
- 📄 Plan de Pruebas  
- 🧪 Casos de Prueba  
- 📊 Informe de ejecución  
- 🐞 Reporte de defectos  

### ⚠️ **2.12 Riesgos y Mitigación**
Identificación y medidas preventivas.  

### 📈 **2.13 Métricas**
- Pass Rate  
- Defect Density  
- Cobertura  
- MTTR  

### 🐞 **2.14 Gestión de Defectos**
Flujo:  
**Crear → Asignar → Corregir → Verificar → Cerrar**

### ✔️ **2.15 Aprobaciones**
Firmas y responsables.

---

## 📋 **3. Plantilla Lista para Usar**

```
Plan de Pruebas — [Proyecto]
Versión:
Fecha:
Autor(es):

1. Introducción
2. Alcance
3. Objetivos
4. Criterios de Entrada
5. Criterios de Salida
6. Estrategia
7. Casos de Prueba
8. Recursos
9. Cronograma
10. Entregables
11. Defectos
12. Riesgos
13. Métricas
14. Aprobaciones
```

---

## 🧑‍💻 **4. Ejemplo Rellenado — Sistema de Reservas**

✨ **Alcance:** Registro, login, agendamiento, notificaciones  
⛔ **Exclusiones:** Pagos  
🧪 **Tipos de pruebas:** Funcional, integración, regresión  
⚠️ **Riesgo principal:** Fallo en SMTP → uso de mock  
📅 **Cronograma:** 1 semana  
- 2 días diseño  
- 3 días ejecución  
- 1 día reporte  

---

## 🧪 **5. Ejemplo de Caso de Prueba**

```
ID: CP-001
Título: Crear usuario con datos válidos
Prioridad: Alta
Precondición: Página funcional
Pasos:
 1. Ingresar nombre
 2. Ingresar correo
 3. Ingresar contraseña
 4. Clic en Registrar
Datos de prueba: Juan, juan@example.com, Abcd1234
Resultado esperado: Usuario creado y correo enviado
Resultado real:
Estado:
```

---

## 🧠 **6. Actividad Práctica**

Crea un **plan de pruebas para una tienda en línea** que incluya:  
- 🏷️ Alcance  
- 🧪 5 Casos de prueba  
- 📅 Cronograma de 1 semana  
- ⚠️ 3 Riesgos  

---

## 📊 **7. Métricas Recomendadas**

- 📈 Pass Rate  
- 🐞 Defect Density  
- ⏱️ MTTR  
- 📌 Cobertura de requisitos  

---

## 📝 **8. Rúbrica de Evaluación (20 puntos)**

| Criterio | Puntos |
|---------|--------|
| Alcance y objetivos | 4 |
| Casos de prueba | 6 |
| Cronograma | 3 |
| Riesgos | 3 |
| Presentación | 4 |

---

## 🎒 **9. Tarea**

Crea un **Plan de Pruebas (3 páginas)** + **10 casos de prueba** + métricas simuladas.  

---

## 📚 **10. Recursos Recomendados**

- 📘 ISTQB Syllabus  
- 🔐 OWASP Testing Guide  
- 🧪 IEEE 829  
