#Calcular impuestos
ingreso=float(input("Ingrese el ingreso anual:"))
impuesto = 0 #delcarando impuesto
# Coloca tu código aquí.
if ingreso <= 85528:
    impuesto = (ingreso *0.18) -556.02
else:
    ingreso >= 85528
    impuesto = 14838.02+ (ingreso - 85528)*0.32
if impuesto<0:
    impuesto = 0



impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
