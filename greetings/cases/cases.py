def greet(lang: str, name: str) -> str:
  match lang:
    case "en":
      return f"Hello, {name}!"
    case "es":
      return f"Hola, {name}!"
    case "fr":
      return f"Bonjour, {name}!"
    case _:
      raise Exception(f"language '{lang}' not supported")
