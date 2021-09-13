import time

class VehiculoOruga:
    def control_de_pista(izquierda, alto):
        pass

    def girar(izquierda):
        control_de_pista(izquierda, True)
        time.sleep(0.25)
        control_de_pista(izquierda, False)


class VehiculoTerrestre:
    def girar_ruedas_delanteras(izquierda, on):
        pass

    def girar(izquierda):
        girar_ruedas_delanteras(izquierda, True)
        time.sleep(0.25)
        girar_ruedas_delanteras(izquierda, False)