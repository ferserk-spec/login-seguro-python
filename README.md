# Login Seguro con Python

Sistema de autenticación seguro desarrollado en Python con protección contra ataques de fuerza bruta, hashing de contraseñas y bloqueo temporal de cuenta.

## Características

- Contraseñas hasheadas con **bcrypt**
- Variables de entorno protegidas con **python-dotenv**
- Bloqueo automático tras 3 intentos fallidos
- Delay progresivo entre intentos fallidos
- Estado persistente en archivo JSON
- Compatible con Windows, Linux y macOS

## Requisitos

- Python 3.9+
- bcrypt
- python-dotenv

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/login-seguro.git
cd login-seguro
```

2. Crea y activa el entorno virtual:

```bash
python -m venv .venv

# Windows
.\.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install bcrypt python-dotenv
```

## Configuración

1. Genera el hash de tu contraseña:

```bash
python generar_hash.py
```

2. Crea el archivo `.env` en la raíz del proyecto:

```env
APP_USERNAME=tu_usuario
APP_PASSWORD_HASH=$2b$12$el_hash_generado
```

## Uso

```bash
python login.py
```

El sistema pedirá usuario y contraseña. Tras 3 intentos fallidos la cuenta se bloquea por 5 minutos.

## Seguridad

- Las contraseñas nunca se almacenan en texto plano
- El archivo `.env` está excluido del repositorio via `.gitignore`
- El bloqueo temporal protege contra ataques de fuerza bruta

## Estructura del proyecto

```
login-seguro/
├── login.py
├── generar_hash.py
├── .env              # No se sube a GitHub
├── .gitignore
└── README.md
```

## Autor

Ferney Valverde
Estudiante de Ingenieria de Sistemas en 4° semestre







