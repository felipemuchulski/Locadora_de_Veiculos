class InvalidTypeError(Exception):
    def __init__(self, expected_type, actual_type):
        self.message = f"Tipo inválido: esperado {expected_type}, mas recebeu {actual_type}"
        super().__init__(self.message)

def validate_types(func):
    from functools import wraps
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        ...