numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
n = int(input("Dame un numero: "))
if n != numeroSecreto:
    print("HA Ha estas atrapado")
    while True:
        int(input("Dame otro numero :"))
else:
    print("Bien hecho, estas libre")