# 🔐 Login Seguro en Python

Sistema de autenticación CLI desarrollado como práctica de ciberseguridad aplicada.

---

## 🚀 Características

- Autenticación de usuario y contraseña
- Hashing seguro con bcrypt
- Variables de entorno (.env)
- Límite de intentos de login
- Bloqueo temporal tras fallos
- Delay progresivo contra fuerza bruta
- Persistencia con JSON

---

## 🛡️ Seguridad implementada

- Hashing unidireccional con bcrypt
- Protección contra ataques de fuerza bruta
- Separación de credenciales del código
- Bloqueo temporal por seguridad
- Principio de mínima exposición

---

## 📁 Estructura del proyecto

login-seguro/
│
├── login_seguro.py
├── generar_hash.py
├── .env
├── .env.example
├── lockout.json
└── README.md

---

## ⚙️ Instalación

pip install bcrypt python-dotenv

---

## ▶️ Ejecución

python login_seguro.py

---

## 🔒 ¿Cómo funciona?

La contraseña nunca se guarda directamente:

password → bcrypt → hash irreversible

El sistema solo valida con checkpw()

---

## 📚 Conceptos aplicados

- Ciberseguridad
- Hashing de contraseñas
- Variables de entorno
- Control de acceso
- Rate limiting
- Persistencia de datos

---

## 👨‍💻 Autor

Wilson Valverde  
Estudiante de Ingeniería de Sistemas – 4º semestre



## 📁 Estructura del proyecto
