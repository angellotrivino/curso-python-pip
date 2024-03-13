import random

def start(counter):
    print("Choose Piedra Papel o Tijera. 2 de 3 intentos")
    print('*' * 10)
    print('Juego #: ', counter)

def choice_option():
    opciones = ("piedra", "papel", "tijera")
    user = input('Only One option ').lower()
    computer = random.choice(opciones).lower()

    if not user in opciones:
        print('Esa opción no está disponible')

    return user, computer

def game(user, computer, point_man, point_computer):
    if user == computer:
        print('empate')
        counter -=1
    elif user == 'piedra' and computer == 'tijera':
        print('Gana user')
        point_man += 1
    elif user == 'tijera' and computer == 'papel':
        print('user gana')
        point_man += 1
    elif user == 'papel' and computer == 'piedra':
        print('user gana')
        point_man += 1
    else:
        print('computer Gana')
        point_computer += 1
    
    return point_man, point_computer


#Variables
counter = 1
point_man = 0
point_computer = 0

while True:

    start(counter)
    user, computer = choice_option()
    
    print(f"Opcion computer = {computer}")

    # // piedra gana a tijera
    # // tijera gana a papel
    # // papel gana a piedra

    point_man, point_computer = game(user, computer, point_man, point_computer)
    
    if point_man == 2:
        print("El humano gana Todo el Juego")
        break
    elif point_computer == 2:
        print("La maquina gana Todo el juego")
        break

    counter += 1