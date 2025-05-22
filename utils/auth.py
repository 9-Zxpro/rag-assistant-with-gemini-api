from flask import Response


# Simple auth decorator
def check_auth(username, password):
    return username == "admin" and password == "password123"

def authenticate():
    return Response("Authentication required", 401, {"WWW-Authenticate": 'Basic realm="Login Required"'})

def requires_auth(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route("/upload", methods=["POST"])
@requires_auth
def upload_file():
    pass
