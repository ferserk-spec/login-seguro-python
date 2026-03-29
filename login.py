import getpass
import bcrypt
import os
import time
import json
from dotenv import load_dotenv


load_dotenv()


MAX_INTENTOS = 3
LOCKOUT_FILE = "lockout.json"     
DELAY_BASE   = 2                  


USUARIO_CORRECTO = os.environ.get("APP_USERNAME")
HASH_CORRECTO    = os.environ.get("APP_PASSWORD_HASH").encode()


def cargar_estado():
    if os.path.exists(LOCKOUT_FILE):
        with open(LOCKOUT_FILE) as f:
            return json.load(f)
    return {"intentos_fallidos": 0, "bloqueado": False}

def guardar_estado(estado):
    with open(LOCKOUT_FILE, "w") as f:
        json.dump(estado, f)


def verificar_password(password_ingresado, hash_guardado):
    return bcrypt.checkpw(password_ingresado.encode(), hash_guardado)


def login():
    estado = cargar_estado()

    if estado["bloqueado"]:
        print("[!] Cuenta bloqueada permanentemente. Contacta al administrador.")
        return

    while estado["intentos_fallidos"] < MAX_INTENTOS:
        nombre    = getpass.getpass("Usuario: ")
        password  = getpass.getpass("Contraseña: ")

        if nombre == USUARIO_CORRECTO and verificar_password(password, HASH_CORRECTO):
            estado["intentos_fallidos"] = 0   
            guardar_estado(estado)
            print(f"\n[✓] Bienvenido, {nombre}.")
            return

        estado["intentos_fallidos"] += 1
        restantes = MAX_INTENTOS - estado["intentos_fallidos"]
        delay     = DELAY_BASE * estado["intentos_fallidos"]   

        print(f"[✗] Credenciales incorrectas. Intentos restantes: {restantes}")
        print(f"    Esperando {delay}s antes del siguiente intento...")
        guardar_estado(estado)  
        time.sleep(delay)

    estado["bloqueado"] = True
    guardar_estado(estado)
    print("\n[✗] Cuenta bloqueada. Demasiados intentos fallidos.")

login()
        
    

   
