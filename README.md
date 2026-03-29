# 🔐 Login Seguro en Python

Sistema de autenticación CLI desarrollado como práctica de seguridad aplicada.  
Implementa hashing con `bcrypt`, variables de entorno y bloqueo persistente
-----

## ✅ Soluciones implementadas

- **`bcrypt`** — hashea la contraseña de forma irreversible
- **`python-dotenv`** — separa credenciales del código fuente
- **`lockout.json`** — persiste el bloqueo entre ejecuciones del programa
- **Delay progresivo** — aumenta el tiempo de espera tras cada intento fallido (2s → 4s → 6s)

-----

## 📁 Estructura del proyecto

```
login-seguro/
│
├── login_seguro.py      # Script principal de autenticación
├── generar_hash.py      # Utilidad para hashear tu contraseña (correr una sola vez)
├── .env                 # Credenciales — NO subir a Git
├── .env.example         # Plantilla del archivo .env
├── lockout.json         # Generado automáticamente al haber intentos fallidos
└── README.md
```

-----

## 🚀 Instalación y uso

### 1. Clonar o descargar el proyecto

```bash
git clone https://github.com/tu-usuario/login-seguro
cd login-seguro
```

### 2. Instalar dependencias

```bash
pip install bcrypt python-dotenv
```

### 3. Generar el hash de tu contraseña

```bash
python generar_hash.py
```

Ejemplo de salida:

```
Ingresa la contraseña que quieres hashear: ****

── Copia esta línea en tu archivo .env ──
APP_PASSWORD_HASH=$2b$12$abc123...
```

### 4. Configurar el archivo `.env`

Renombra `.env.example` a `.env` y complétalo:

```env
APP_USERNAME=tu_usuario
APP_PASSWORD_HASH=$2b$12$HASH_GENERADO_EN_EL_PASO_ANTERIOR
```

> **Importante:** Agrega `.env` y `lockout.json` a tu `.gitignore`

### 5. Ejecutar el login

```bash
python login_seguro.py
```

-----

## 🔒 ¿Cómo funciona bcrypt?

```
Contraseña original → bcrypt → $2b$12$xyz...abc  (hash)
                                        ↓
                         No se puede revertir al original
                         Solo se puede verificar con checkpw()
```

Nunca se almacena la contraseña real. El sistema solo guarda el hash y verifica si lo que ingresa el usuario coincide con él.

-----

## 🛡️ Flujo de seguridad

```
Inicio
  │
  ├─ ¿lockout.json existe y bloqueado = true?
  │     └─ Sí → Mostrar mensaje de bloqueo y salir
  │
  └─ No → Solicitar usuario y contraseña
              │
              ├─ ¿Credenciales correctas?
              │     └─ Sí → Acceso concedido, resetear contador
              │
              └─ No → Incrementar contador + guardar en JSON + esperar Ns
                           │
                           └─ ¿Llegó a 3 intentos? → Bloquear cuenta permanentemente
```

-----

## 📦 Dependencias

|Librería       |Versión|Uso                            |
|---------------|-------|-------------------------------|
|`bcrypt`       |≥ 4.0  |Hashing de contraseñas         |
|`python-dotenv`|≥ 1.0  |Lectura de variables de entorno|

Librerías estándar usadas: `getpass`, `os`, `time`, `json`

-----

## .gitignore recomendado

```
.env
lockout.json
__pycache__/
*.pyc
```

-----

## 📚 Conceptos aplicados

- **Hashing unidireccional** con salt automático (bcrypt)
- **Variables de entorno** para separar configuración del código
- **Persistencia de estado** con archivos JSON
- **Rate limiting** mediante delays progresivos
- **Principio de mínima exposición** — el código nunca conoce la contraseña real

-----

> Proyecto de práctica — Ingeniería de Sistemas · 4to Semestre  
> Tema: Seguridad en autenticación CLI con Python

## Autor
Estudiante de Ingeniería de Sistemas - Semestre 4