class NoSupportedError(Exception):
  def __init__(self, lang: str):
    super().__init__(f"language '{lang}' not supported")
