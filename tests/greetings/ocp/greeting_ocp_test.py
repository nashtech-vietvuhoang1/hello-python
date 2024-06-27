from greetings.ocp import greet, register
from greetings.errors import NoSupportedError
import pytest

class TestGreetingOcp:
  def test_greet_en(self):
    assert greet("en", "Viet") == "Hello, Viet!"

  def test_greet_es(self):
    assert greet("es", "Viet") == "Hola, Viet!"

  def test_greet_fr(self):
    assert greet("fr", "Viet") == "Bonjour, Viet!"

  def test_greet_nosupport(self):
    with pytest.raises(NoSupportedError):
      greet("xx", "Viet")

  def test_support_new_lang(self):
    register("vi", lambda name: f"Xin Chao, {name}!")
    assert greet("vi", "Viet") == "Xin Chao, Viet!"
