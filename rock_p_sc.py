import random
import functools
import time
import datetime

def registrar_tiempo(func):
    @functools.wraps(funcs)
    def wraper(*args,**kwargs):
        return
    return

def contador_juegos(func):
    @functools.wraps(funcs)
    def wraper(*args,**kwargs):
        return
    return

def registrar_fecha_hora(func):
    @functools.wraps(funcs)
    def wraper(*args,**kwargs):
        return
    return

def contador_victorias(func):
    @functools.wraps(funcs)
    def wraper(*args,**kwargs):
        return
    return

def contador_derrotas(func):
    @functools.wraps(funcs)
    def wraper(*args,**kwargs):
        return
    return

def contador_empates(func):
    @functools.wraps(funcs)
    def wraper(*args,**kwargs):
        return
    return

def limite_de_partidas(func):
    @functools.wraps(funcs)
    def wraper(*args,**kwargs):
        return
    return

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijeras = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_img =[piedra, papel, tijeras]
ask = input("Quieres jugar? ").lower()
while ask != "no":

    opcion = int(input("Que elijes? Piedra (0), Papel (1), Tijeras (2).\n"))
    if (opcion >= 3 or opcion< 0):
        print("Elejiste un numero erroneo, pierdes!")
    else:
        print(game_img[opcion])
        computer_pick = random.randint(0,2)
        print("Eleccion del contrincante:"); print(game_img[computer_pick])
        if opcion == 0 and computer_pick == 2 or opcion > computer_pick: print("Ganas!")
        elif computer_pick == 0 and opcion == 2 or computer_pick > opcion: print("Pierdes")
        elif computer_pick == opcion: print("Empate")
    ask = input("Quieres seguir jugando? ").lower()
        

