class Nivel1:
    var = 100
    def fun(self):
        return 101

class Nivel2:
    var = 200
    def fun(self):
        return 201

class Nivel3(Nivel2):
    pass

obj = Nivel3()

print(obj.var, obj.fun())