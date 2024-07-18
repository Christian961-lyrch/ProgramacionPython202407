"""
Calcular el área de una triangulo, solicitar los datos de altura y base al usuario
"""

# 1. Solicitar los datos al usuario
base_triangulo = float (input("Ingrese la base del triangulo :"))
altura_triangulo = float(input("Ingrese la altura del triagulo :"))

# 2. Calcular el área del triangulo
area_triangulo = (base_triangulo*altura_triangulo)/2

# 3. Para el caso de mostrar los resultados

# str -> convierte un valor numérico a cadena

print ("El area del triangulo es " + str (area_triangulo))

#f-string 
print (f"El área del triangulo es {area_triangulo}")

#format
print("El area del triangulo de base {} y altura {} es : {} " .format(base_triangulo, altura_triangulo, area_triangulo))