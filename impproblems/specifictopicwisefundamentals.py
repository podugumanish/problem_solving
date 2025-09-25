# functools wrapping benefits
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greets a user by name"""
    print(f"Hello {name}!")

print(greet.__name__)  # ⚠️ Output: wrapper (lost original name)
print(greet.__doc__)   # ⚠️ Output: None (lost docstring)


import functools

def my_decorator(func):
    @functools.wraps(func)  # ✅ Preserves metadata
    def wrapper(*args, **kwargs):
        print("Before function")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greets a user by name"""
    print(f"Hello {name}!")

print(greet.__name__)  # ✅ Output: greet
print(greet.__doc__)   # ✅ Output: Greets a user by name


    
import functools
import logging
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# --- Decorator 1: Exception Handler ---
def exception_handler(default_return=None, raise_exception=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error(f"Error in {func.__name__}: {e}", exc_info=True)
                if raise_exception:
                    raise
                return default_return
        return wrapper
    return decorator


# --- Decorator 2: Logger ---
def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper


# --- Decorator 3: Execution Timer ---
def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = (time.perf_counter() - start) * 1000
        logging.info(f"{func.__name__} took {duration:.2f} ms")
        return result
    return wrapper


# --- Using Multiple Decorators ---
@time_it
@log_calls
@exception_handler(default_return="Something went wrong!")
def divide(a, b):
    return a / b


# --- Testing ---
print(divide(10, 2))   # ✅ Works fine, logs calls and timing
print(divide(10, 0))   # ✅ Logs error, returns default value




# MRO