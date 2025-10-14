import datetime
from functools import wraps
from typing import Any
from typing import Callable


def log(filename: str = None):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                msg = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"{datetime.datetime.now()}: {msg}\n")
                else:
                    print(msg)
                return result
            except Exception as e:
                msg = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"{datetime.datetime.now()}: {msg}\n")
                else:
                    print(msg)
                raise
        return wrapper
    return decorator
