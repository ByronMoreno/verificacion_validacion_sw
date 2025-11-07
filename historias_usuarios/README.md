# 🧠 Clase: Historias de Usuario

## 🎯 Objetivo de la clase
Al finalizar esta clase, el estudiante será capaz de:
- Comprender qué son las historias de usuario.  
- Redactar historias de usuario efectivas usando el formato estándar.  
- Definir criterios de aceptación claros y verificables.  
- Aplicar ejemplos reales para el desarrollo de software ágil.  

---

## 🧩 1. ¿Qué es una Historia de Usuario?

Una **Historia de Usuario (User Story)** es una descripción **breve y simple** de una funcionalidad del sistema escrita desde la perspectiva del **usuario final o cliente**.

> 💬 Es una forma ágil de capturar qué necesita el usuario y por qué lo necesita.

Se usa principalmente en metodologías **ágiles** (como **Scrum o Kanban**) para comunicar requerimientos de manera clara entre el equipo técnico y el negocio.

---

## 💬 2. Estructura básica

El formato más común es el siguiente:

> **Como** [tipo de usuario]  
> **quiero** [una funcionalidad o acción]  
> **para** [obtener un beneficio o resultado].

Ejemplo:

> **Como** estudiante de una plataforma educativa,  
> **quiero** ver mis calificaciones de cada materia,  
> **para** conocer mi desempeño académico.

---

## 🔍 3. Características de una buena historia de usuario (INVEST)

| Letra | Significado | Descripción |
|:------|:-------------|:-------------|
| **I** | **Independiente** | Puede desarrollarse por separado. |
| **N** | **Negociable** | Puede modificarse en función del diálogo con el cliente. |
| **V** | **Valiosa** | Aporta valor al usuario o negocio. |
| **E** | **Estimable** | Se puede calcular el esfuerzo requerido. |
| **S** | **Small (Pequeña)** | No debe ser demasiado grande. |
| **T** | **Testable** | Se puede comprobar su cumplimiento. |

---

## 🧱 4. Criterios de aceptación

Los **criterios de aceptación** definen cuándo una historia de usuario se considera **terminada y correcta**.

Ejemplo:

Historia de usuario:
> **Como** cliente del sistema,  
> **quiero** recuperar mi contraseña por correo electrónico,  
> **para** poder acceder nuevamente si la olvido.

Criterios de aceptación:
1. El usuario debe poder ingresar su correo registrado.  
2. El sistema debe enviar un enlace de recuperación válido durante 15 minutos.  
3. El usuario puede crear una nueva contraseña desde ese enlace.  
4. Si el correo no está registrado, debe mostrar un mensaje claro.

---

## 💻 5. Ejemplos prácticos

### 🧑‍💼 Ejemplo 1: Aplicación de ventas

**Historia de usuario:**
> Como vendedor,  
> quiero registrar nuevas ventas en la aplicación,  
> para mantener actualizado mi historial de transacciones.

**Criterios de aceptación:**
- El formulario debe tener campos de producto, cantidad y valor.  
- Debe calcular automáticamente el total.  
- Se debe guardar la venta en la base de datos.

---

### 👩‍🎓 Ejemplo 2: Plataforma educativa

**Historia de usuario:**
> Como docente,  
> quiero subir calificaciones de mis estudiantes,  
> para que ellos puedan ver sus resultados en línea.

**Criterios de aceptación:**
- El docente debe poder seleccionar el curso y la materia.  
- Puede cargar las notas mediante un formulario o archivo CSV.  
- Los estudiantes ven las calificaciones inmediatamente después de ser publicadas.

---

### 📱 Ejemplo 3: App móvil de hábitos saludables

**Historia de usuario:**
> Como usuario de la app,  
> quiero registrar mis comidas diarias,  
> para llevar control de mi alimentación.

**Criterios de aceptación:**
- Debe permitir registrar desayuno, almuerzo y cena.  
- Mostrar resumen diario de calorías.  
- Permitir editar y eliminar comidas.

---

## 🧮 6. Cómo crear Historias de Usuario (paso a paso)

1. **Identificar los actores** → ¿Quiénes usan el sistema?  
   Ejemplo: estudiante, profesor, cliente, administrador.

2. **Detectar sus necesidades o problemas**  
   Ejemplo: el estudiante necesita conocer sus calificaciones.

3. **Escribir la historia con el formato estándar**  
   Ejemplo:  
   > Como estudiante, quiero ver mis calificaciones para conocer mi desempeño.

4. **Agregar criterios de aceptación**  
   Ejemplo:  
   - El sistema muestra las notas organizadas por materia.  
   - Solo el estudiante autenticado puede ver sus calificaciones.

5. **Priorizar las historias** según el valor al negocio o usuario.

6. **Dividir historias grandes** en historias más pequeñas (épicas → historias → tareas).

---

## 🗂️ 7. Ejercicio en clase

Crea tres historias de usuario para una **aplicación bancaria móvil**.

### Requisitos:
- Usa el formato estándar.  
- Incluye al menos **2 criterios de aceptación** por historia.  
- Que sean **claras, valiosas y medibles.**

💡 **Ejemplo de respuesta esperada:**

> **Como** cliente del banco,  
> **quiero** ver mi saldo actualizado,  
> **para** conocer el estado de mis cuentas.  
>
> **Criterios de aceptación:**  
> - El sistema debe mostrar el saldo de cada cuenta corriente y de ahorros.  
> - La información se actualiza en tiempo real al iniciar sesión.

---

## 🧠 8. Buenas prácticas

- Evita historias muy técnicas ("como desarrollador quiero refactorizar código").  
- Usa lenguaje natural, no jerga técnica.  
- Prioriza la **claridad y el valor para el usuario final**.  
- Las historias se complementan con tareas técnicas en el backlog.

---

## 🧩 9. Actividad final

🎯 **Desafío:**  
Elige una aplicación que uses todos los días (por ejemplo: WhatsApp, Spotify, Moodle, Gmail).  
Redacta **3 historias de usuario** con **criterios de aceptación** para nuevas funciones que te gustaría tener.

---

## 📘 10. Resumen

| Concepto | Descripción breve |
|-----------|-------------------|
| Historia de usuario | Descripción corta de una funcionalidad desde la perspectiva del usuario. |
| Formato | “Como [usuario], quiero [acción], para [beneficio].” |
| Criterios de aceptación | Reglas que definen cuándo una historia está terminada. |
| INVEST | Independiente, Negociable, Valiosa, Estimable, Pequeña, Testeable. |

---
