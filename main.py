import random


#Seleccion de opciones
def choice_func():
  options = ("piedra", "papel", "tijera")
  user_option = input("piedra, papel o tijera -> ")
  user_option = user_option.lower().strip()

  if user_option not in options:
    print("Esa opcion no es valida")
    return None, None

  computer_option = random.choice(options)

  return user_option, computer_option


#Reglas del juego
def rules_func(user_option, computer_option, user_count=0, computer_count=0):
  if user_option == computer_option:
    input("Empate!")
  elif user_count == "piedra":
    if computer_option == "papel":
      print("Papel gano a piedra. Computer won!")
      computer_count += 1
    else:
      print("Piedra gano a tijera. User won!")
      user_count += 1
  elif user_option == "papel":
    if computer_option == "tijera":
      print("Tijera gano a papel. Computer won!")
      computer_count += 1
    else:
      print("Papel gano a piedra. User won!")
      user_count += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("Tijera gano a papel. User won!")
      user_count += 1
    else:
      print("Piedra gano a tijera. Computer won!")
      computer_count += 1

  print("Puntos usuario -> ", user_count)
  print("Puntos PC -> ", computer_count)

  return user_count, computer_count


#Verifica ganador
def winner_func(user_count, computer_count, rounds):
  if user_count == rounds:
    winner = "user"

  if computer_count == rounds:
    winner = "pc"

    print("*" * 20)
    print(f"El ganador es -> {winner}")
    breakpoint()


#Funcion principal del juego
def game_func():
  user_count = 0
  computer_count = 0
  rounds = 2
  contador = 0

  while True:
    contador += 1
    user_option, computer_option = choice_func()
    print("*" * 5, "ronda ", contador, "*" * 5)
    user_count, computer_count = rules_func(user_option,
                                            computer_option,
                                            user_count=user_count,
                                            computer_count=computer_count)
    winner_func(user_count, computer_count, rounds=rounds)


#Ejecucion del juego
game_func()
