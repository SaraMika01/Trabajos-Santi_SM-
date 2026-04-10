#Grupo de Molina y Naz

def mostrar_cartelera(lista_peliculas, salas_disponibles, mensaje_bienvenida):
    print(f"--- {mensaje_bienvenida} ---")
    for i in range(salas_disponibles):
        print(f"Sala {i + 1}: {lista_peliculas[i]}")

def calcular_precio(edad, cantidad, dia_semana):
    precio = 10.0 * cantidad

    if edad < 12 or edad > 60:
        precio = precio - 3.0

    if dia_semana.lower() == "viernes":
        precio = precio - 2.0

    return precio

def imprimir_ticket(pelicula, cantidad_boletos, costo_total):
    print("**** TICKET DE CINE ****")
    print(f"Película: {pelicula}")
    print(f"Cantidad: {cantidad_boletos} entradas")
    print(f"Total a pagar: {costo_total:.2f}")
    print("************")

peliculas = ["Batman", "Avatar", "Spiderman", "Mario Bros"]
mostrar_cartelera(peliculas, 4, "Bienvenido a CineStar")

user_edad = int(input("¿Cuántos años tienes? : "))
user_peli_index = int(input("Selecciona la película (ingresa el número de sala): ")) - 1
user_entradas = int(input("¿Cuántas entradas quieres? : "))
dia = str(input("Por último, ¿Qué día es hoy? : "))

selected_movie = peliculas[user_peli_index]

precio_total = calcular_precio(user_edad, user_entradas, dia)

imprimir_ticket(selected_movie, user_entradas, precio_total)




def entrevista_jugadores():
    contador= 0

    while True:
        name= str(input("Nombre: "))
        age= int(input("Edad: "))
        contador= contador +1

        if contador==6:
            break

entrevista_jugadores()

def promedio(nota1, nota2, nota3):
    suma= nota1 + not2 + nota3
    prom= suma/3

    if prom == 10:
        print("Excelente! Te sacaste ",prom "!!")
    elif prom== 9 or prom == 8:
        print("Haz aprobado! Te sacaste ",prom)
    elif prom== 7:
        print("Haz aprobado... Por poco... Te sacaste ",prom)
    else:
        print("Haz desaprobado con " , prom)


import math

def calcular_pitagoras_dinamico():

    cantidad = int(input("¿Cuántos triángulos deseas calcular?: "))
    
    resultados = []
    for i in range(cantidad):
        print(f"\n--- Triángulo {i+1} ---")
        
        cateto_a = float(input("Ingresa el valor del primer cateto: "))
        cateto_b = float(input("Ingresa el valor del segundo cateto: "))

        hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
        
        resultados.append(round(hipotenusa, 2))
        print(f"La hipotenusa es: {round(hipotenusa, 2)}")

    return resultados
lista_final = calcular_pitagoras_dinamico()
print("\n------------------------------------")
print(f"Lista completa de resultados: {lista_final}")