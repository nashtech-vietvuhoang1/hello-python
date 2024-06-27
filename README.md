# hello-python
Learn Python

# Install 

```sh
poetry install
```

# Run test

Run all test 

```sh
pytest
```

Run Test for Cases

```sh
pytest tests/greetings/case
```
Run Test for OCP

```sh
pytest tests/greetings/ocp
```

Add more language to OCP tests/greetings/ocp/greeting_ocp_test.py

```python
  def test_support_new_lang(self):
    register("vi", lambda name: f"Xin Chao, {name}!")
    assert greet("vi", "Viet") == f"Xin Chao, Viet!"
```
