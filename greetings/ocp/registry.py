
from typing import Callable
from ..errors import NoSupportedError

GreetingRegistry = dict[str, Callable[[str], str]]

__globalRegistry = GreetingRegistry()

def register(lang: str, func: Callable[[str], str]) -> None:
  if not str or not func: 
    raise NoSupportedError("illegal language")
  
  __globalRegistry[lang] = func

def greet(lang: str, name: str) -> str:
  func = __globalRegistry.get(lang)
  if not func:
    raise NoSupportedError(f"language '{lang}' not supported")
  return func(name)
