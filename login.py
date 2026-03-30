import getpass
import bcrypt
import os
import time
import json
from dotenv import load_dotenv

load_dotenv()

MAX_INTENTOS = 3
LOCKOUT_FILE = "lockout.json"
DELAY_BASE = 2
LOCKOUT_TIME = 300   

USUARIO_CORRECTO = os.environ.get("APP_USERNAME")
HASH_ENV = os.environ.get("APP_PASSWORD_HASH")

if not USUARIO_CORRECTO or not HASH_ENV:
    raise ValueError("Faltan variables de entorno en el archivo .env")

HASH_CORRECTO = HASH_ENV.encode()


def cargar_estado():
    if os.path.exists(LOCKOUT_FILE):
        with open(LOCKOUT_FILE) as f:
            return json.load(f)
    return {"intentos_fallidos": 0, "bloqueado": False, "timestamp": 0}


def guardar_estado(estado):
    with open(LOCKOUT_FILE, "w") as f:
        json.dump(estado, f)


def verificar_password(password, hash_guardado):
    return bcrypt.checkpw(password.encode(), hash_guardado)


def esta_bloqueado(estado):
    if not estado["bloqueado"]:
        return False

    tiempo_actual = time.time()
    if tiempo_actual - estado["timestamp"] > LOCKOUT_TIME:
        estado["bloqueado"] = False
        estado["intentos_fallidos"] = 0
        guardar_estado(estado)
        return False

    return True


def login():
    estado = cargar_estado()

    if esta_bloqueado(estado):
        print(" Cuenta bloqueada temporalmente. Intenta más tarde.")
        return

    while estado["intentos_fallidos"] < MAX_INTENTOS:
        usuario = input("Usuario: ")
        password = getpass.getpass("Contraseña: ")

        if usuario == USUARIO_CORRECTO and verificar_password(password, HASH_CORRECTO):
            estado["intentos_fallidos"] = 0
            guardar_estado(estado)
            print(f"\n Bienvenido, {usuario}")
            return

        estado["intentos_fallidos"] += 1
        restantes = MAX_INTENTOS - estado["intentos_fallidos"]
        delay = DELAY_BASE * estado["intentos_fallidos"]

        print(f"Credenciales incorrectas. Intentos restantes: {restantes}")
        print(f"    Esperando {delay}s...")
        guardar_estado(estado)
        time.sleep(delay)

    estado["bloqueado"] = True
    estado["timestamp"] = time.time()
    guardar_estado(estado)
    print("\n Cuenta bloqueada temporalmente por múltiples intentos fallidos.")


if __name__ == "__main__":
    login()
