
# 🧪✨ **Clase Completa: Casos de Prueba en Calidad de Software**

## 🎯 **Objetivos de la Clase**
- 🧠 Comprender qué es un caso de prueba  
- 🧩 Identificar su estructura y componentes  
- ✍️ Diseñar casos efectivos y reproducibles  
- 🧪 Ejecutar pruebas y documentar resultados  
- 🔗 Construir trazabilidad entre requisitos y test  
- ⭐ Aplicar buenas prácticas en diseño de pruebas  

---

# 🔍 **1. ¿Qué es un Caso de Prueba?**

Un **Caso de Prueba (Test Case)** es un documento que define:  
✔ Condiciones  
✔ Pasos  
✔ Datos  
✔ Resultado esperado  

…para validar una funcionalidad del software.  

Es la unidad mínima y fundamental del proceso de testing.

---

# 🎯 **2. ¿Para qué sirve?**

- 🔎 Validar funcionalidades  
- 🐞 Detectar errores  
- 🔐 Asegurar calidad  
- 📚 Documentar ejecución  
- 🔗 Mantener trazabilidad  
- 🤖 Base para automatización  

---

# 🧱 **3. Componentes Esenciales de un Caso de Prueba**

| 🏷 Campo | 📘 Descripción |
|---------|----------------|
| **ID** | Identificador único |
| **Título** | Acción o funcionalidad a validar |
| **Descripción** | Detalle del propósito del caso |
| **Precondiciones** | Requisitos previos |
| **Datos de prueba** | Valores necesarios |
| **Prioridad** | Alta / Media / Baja |
| **Tipo** | Funcional, regresión, negativa, etc. |
| **Pasos** | Lista numerada |
| **Resultado esperado** | Lo que debería ocurrir |
| **Resultado real** | Se completa al ejecutar |
| **Estado** | PASS / FAIL / BLOCKED |
| **Evidencia** | Capturas o enlaces |
| **Observaciones** | Comentarios |

---

# 🧭 **4. ¿Cómo crear un Caso de Prueba? (Paso a Paso)**

### 📝 Paso 1: Analizar el requisito  
Ejemplo: *“El usuario debe iniciar sesión con email y contraseña válidos.”*

### 🎭 Paso 2: Identificar escenarios  
- Positivos ✨  
- Negativos ❌  

### 🔢 Paso 3: Definir datos  
- email: **juan@example.com**  
- password: **Abc12345**  

### 🔐 Paso 4: Establecer precondiciones  
- Usuario registrado  
- Página accesible  

### 👣 Paso 5: Documentar pasos  
1️⃣ Abrir la URL  
2️⃣ Ingresar email  
3️⃣ Ingresar contraseña  
4️⃣ Clic en *Iniciar sesión*  

### 🎯 Paso 6: Resultado esperado  
“Debe ir al dashboard y mostrar mensaje de bienvenida.”

---

# 🧪 **5. Tipos de Casos de Prueba**

- ✔ Funcionales  
- ❌ Negativos  
- 🔁 Regresión  
- 🔗 Integración  
- 👤 Aceptación (UAT)  
- 🎨 UI/UX  
- 🚀 Rendimiento  

---

# 📘 **6. Caso de Prueba Completo (Ejemplo Profesional)**

```
ID: CP-LOGIN-001
Título: Login con credenciales válidas
Descripción: Validar que el usuario puede ingresar al sistema.

Precondiciones:
 - Usuario registrado.
 - Página accesible.

Datos:
 - email: juan@example.com
 - password: Abc12345

Prioridad: Alta
Tipo: Funcional - positivo

Pasos:
 1. Ingresar email válido.
 2. Ingresar contraseña válida.
 3. Presionar “Iniciar sesión”.

Resultado Esperado:
 - Redirección al dashboard.
 - Mensaje “Bienvenido Juan”.

Resultado Real:
Estado:
Evidencia:
Observaciones:
```

---

# ⭐ **7. Buenas Prácticas**

✔ Casos simples y claros  
✔ Validar un solo comportamiento por caso  
✔ Incluir datos de prueba  
✔ Pasos secuenciales y precisos  
✔ Priorizar casos críticos  
✔ Mantener trazabilidad  

---

# ❌ **8. Errores Comunes**

- Casos muy genéricos  
- Falta de resultados esperados  
- Pasos ambiguos  
- Varios escenarios mezclados  
- No actualizar pruebas  

---

# 🔗 **9. Matriz de Trazabilidad**

| Requisito | Descripción | Casos Asociados |
|-----------|-------------|------------------|
| RF-01 | Login | CP-LOGIN-001, CP-LOGIN-002 |
| RF-02 | Registro | CP-REG-001, CP-REG-002 |

---

# 🧪 **10. Actividades Prácticas**

### ✍️ Actividad 1  
Crear **5 casos de prueba** para el módulo de registro.

### 🧩 Actividad 2  
Crear una **matriz de trazabilidad** para login + registro.

### 🖼 Actividad 3  
Ejecutar casos y documentar resultados + evidencia.

---

# 📝 **11. Rúbrica (20 puntos)**

| Criterio | Puntos |
|----------|--------|
| Estructura correcta | 4 |
| Claridad de pasos | 4 |
| Datos de prueba | 3 |
| Resultados esperados | 3 |
| Cobertura | 3 |
| Presentación | 3 |
| **Total** | **20 pts** |

---

# 📚 **12. Recursos**

- 📘 ISTQB Foundation Syllabus  
- 📄 IEEE 829 Standard Test Documentation  
- 🔐 OWASP Testing Guide  

---

# 📄 **13. Plantilla Editable**

```
ID:
Título:
Descripción:
Precondiciones:
Datos de Prueba:
Prioridad:
Tipo:
Pasos:
Resultado Esperado:
Resultado Real:
Estado:
Evidencia:
Observaciones:
```

