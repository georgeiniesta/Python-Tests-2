class ClaseEjemplo:
    attr = 1

print(hasattr(ClaseEjemplo, 'attr'))
print(hasattr(ClaseEjemplo, 'prop'))

class ClaseEjemplo:
    a = 1
    def __init__(self):
        self.b = 2

objetoEjemplo = ClaseEjemplo()

print(hasattr(objetoEjemplo, 'b'))
print(hasattr(objetoEjemplo, 'a'))
print(hasattr(ClaseEjemplo, 'b'))
print(hasattr(ClaseEjemplo, 'a'))