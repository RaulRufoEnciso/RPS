import random
import time
import datetime
from functools import wraps

def registrar_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        with open('log_tiempo_juego.txt', 'a') as file:
            file.write(f"Tiempo: {duration:.2f} sec\n")
        return result
    return wrapper

def contador_juego(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open("log_contador_juego.txt", "a") as file:
            file.write(f"Juego jugado: {func.__name__}\n")
        return func(*args, **kwargs)
    return wrapper

def registrar_fecha_hora(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        date = datetime.datetime.now()
        result = func(*args, **kwargs)
        with open("log_fecha_hora.txt", "a") as file:
            file.write(f"Fecha {date} \n")
        return result
    return wrapper

victorias = 0
def contador_victorias(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global victorias
        resultado = func(*args, **kwargs)
        if resultado == "victoria":
            victorias += 1
            with open('log_victorias.txt', 'a') as f:
                f.write(f"Victorias: {victorias}\n")
        return resultado
    return wrapper

derrotas = 0
def contador_derrotas(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global derrotas
        resultado = func(*args, **kwargs)
        if resultado == "derrota":
            derrotas += 1
            with open('log_derrotas.txt', 'a') as f:
                f.write(f"Derrotas: {derrotas}\n")
        return resultado
    return wrapper

empates = 0
def contador_empates(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global empates
        resultado = func(*args, **kwargs)
        if resultado == "empate":
            empates += 1
            with open('log_empates.txt', 'a') as f:
                f.write(f"Empates: {empates}\n")
        return resultado
    return wrapper

def limitar_partidas(partidas):
    partidas_jugadas = 0

    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal partidas_jugadas
            if partidas_jugadas < partidas:
                partidas_jugadas += 1
                return func(*args, **kwargs)
            else:
                print("Has alcanzado el límite de partidas para esta sesión.")
        return wrapper
    return decorador

@registrar_tiempo
@contador_juego
@registrar_fecha_hora
@contador_victorias
@contador_empates
@contador_derrotas
@limitar_partidas(10)
def piedra_papel_tijera():

    opciones =["piedra", "papel", "tijera"]

    user_pick = input("Elige: piedra, papel o tijera: \n").lower()
    if user_pick not in opciones:
        print("Opcion no valida")
        return

    computer_pick = random.randint(0,2)
    computer_pick_str = opciones[computer_pick]
    print(f"Ordenador elegido: {computer_pick_str}")
    print(opciones[computer_pick])

    if user_pick == computer_pick_str:
        print("Es un empate! ")
        return "empate"
    elif (user_pick == "piedra" and computer_pick_str == "tijera") or \
         (user_pick == "papel" and computer_pick_str == "piedra") or \
         (user_pick == "tijera" and computer_pick_str == "papel"):
        print("Has ganado! ")
        return "victoria"
    else:
        print("Has perdido! ")
        return "derrota"

def menu():
    while True:
        print("\nSeleccione si quieres jugar: ")
        print("1. Piedra, Papel o Tijera")
        print("2. Salir")

        opcion = input("Elige: \n").lower()

        if opcion == "1":
            piedra_papel_tijera()
        elif opcion == "2":
            print("Salir")
            break
        else:
            print("Opcion no valida")

menu()