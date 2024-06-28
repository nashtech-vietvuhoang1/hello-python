
from typing import Callable
from ..errors import IllegalArgumentError, NoSupportedError

GreetingRegistry = dict[str, Callable[[str], str]]

__globalRegistry = GreetingRegistry()

def register(lang: str, func: Callable[[str], str]) -> None:
  if not lang or not func: 
    raise IllegalArgumentError("illegal language")
  
  __globalRegistry[lang] = func

def greet(lang: str, name: str) -> str:
  func = __globalRegistry.get(lang)
  if not func:
    raise NoSupportedError(lang)
  return func(name)
