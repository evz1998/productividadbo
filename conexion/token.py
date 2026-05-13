import jwt
import flask

key: str = "976457hsdgfst8723643gsfhg"

def validarToken() -> bool:
    
    try:
        token = flask.request.args.get("Token")
        if not token:
            return False
        jwt.decode(token, key, algorithms=["HS512"])
        return True
    except:
        return False    
    
def generarToken() -> str:
    return jwt.encode({"Usuario":"backoffice"}, key, algorithm="HS512")