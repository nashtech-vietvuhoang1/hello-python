from .registry import register, greet

register("en", lambda name: f"Hello, {name}!")
register("es", lambda name: f"Hola, {name}!")
register("fr", lambda name: f"Bonjour, {name}!")
