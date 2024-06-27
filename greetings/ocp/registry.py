
from typing import Callable

GreetingRegistry = dict[str, Callable[[str], str]]

__globalRegistry = GreetingRegistry()

def register(lang: str, func: Callable[[str], str]) -> None:
  if not str or not func: 
    raise Exception("illegal language")
  
  __globalRegistry[lang] = func

def greet(lang: str, name: str) -> str:
  func = __globalRegistry.get(lang)
  if not func:
    raise Exception(f"language '{lang}' not supported")
  return func(name)
