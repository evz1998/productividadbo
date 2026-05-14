# ============================================================
# MÓDULO DE ENCRIPTACIÓN
# Usa Fernet (encriptación simétrica) de la librería cryptography
# La misma llave encripta y desencripta
# ============================================================
 
from cryptography.fernet import Fernet;

LLAVE: bytes = b"mxsAtVo8HwXz_TzjVlsC7lluujOygUoObGRu8vql9eo=";
 
fernet = Fernet(LLAVE);
 
# ============================================================
# FUNCIÓN: encriptar
# Recibe un texto y lo devuelve encriptado
# ============================================================
def encriptar(texto: str) -> str:
    if not texto:
        return texto;
    return fernet.encrypt(texto.encode()).decode();
 
# ============================================================
# FUNCIÓN: desencriptar
# Recibe un texto encriptado y lo devuelve en texto normal
# ============================================================
def desencriptar(texto: str) -> str:
    if not texto:
        return texto;
    try:
        return fernet.decrypt(texto.encode()).decode();
    except:
        return texto;  # Si falla, devuelve el texto tal cual
 