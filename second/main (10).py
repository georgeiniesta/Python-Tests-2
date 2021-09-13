hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
#Pasando a minutos
a = hora * 60
b = min
c = dura
#Calculando 
#minutos totales
mintot = a + b + c 
#calculando horas
horafinal = mintot // 60
#min final
minfinal = mintot % 60
#desplegando resultado
print("Salida esperada:", horafinal % 24, ":", minfinal)