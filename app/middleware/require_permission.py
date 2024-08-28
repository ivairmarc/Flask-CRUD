from flask import Flask, request, abort
from flask_login import current_user
from functools import wraps


# Decorador para verificar se o usuário tem a permissão necessária
def requires_permission(permission):
    def decorator(f):
        def decorated_function(*args, **kwargs):
            if not current_user.has_permission(permission):
                abort(403)  # Forbidden
            return f(*args, **kwargs)
        return decorated_function
    return decorator