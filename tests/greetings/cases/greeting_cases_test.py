from greetings.cases import greet
from greetings.errors import NoSupportedError
import pytest

class TestGreetingCases:
  def test_greet_en(self):
    assert greet("en", "Viet") == "Hello, Viet!"

  def test_greet_es(self):
    assert greet("es", "Viet") == "Hola, Viet!"

  def test_greet_fr(self):
    assert greet("fr", "Viet") == "Bonjour, Viet!"

  def test_greet_nosupport(self):
    with pytest.raises(NoSupportedError):
      greet("xx", "Viet")
