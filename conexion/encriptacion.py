# ============================================================
# MÓDULO DE ENCRIPTACIÓN
# Usa Fernet (encriptación simétrica) de la librería cryptography
# La misma llave encripta y desencripta
# ============================================================
 
from cryptography.fernet import Fernet;
 
# ⚠️ IMPORTANTE: Esta llave NUNCA debe cambiar después de guardar datos
# Si la cambias, no podrás leer los datos ya encriptados en la BD
LLAVE: bytes = b"mxsAtVo8HwXz_TzjVlsC7lluujOygUoObGRu8vql9eo=";
 
# Genera una llave válida la primera vez (corre esto una sola vez)
# LLAVE = Fernet.generate_key()
# print(LLAVE)  # copia y pega el resultado arriba
 
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
 