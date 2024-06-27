from greetings.ocp import *
import pytest

class TestGreetingOcp:
  def test_greet_en(self):
    assert greet("en", "Viet") == f"Hello, Viet!"

  def test_greet_es(self):
    assert greet("es", "Viet") == f"Hola, Viet!"

  def test_greet_fr(self):
    assert greet("fr", "Viet") == f"Bonjour, Viet!"

  def test_greet_nosupport(self):
    with pytest.raises(Exception):
      greet("xx", "Viet")

  def test_support_new_lang(self):
    register("vi", lambda name: f"Xin Chao, {name}!")
    assert greet("vi", "Viet") == f"Xin Chao, Viet!"
