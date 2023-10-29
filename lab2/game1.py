import random

def whowins(player1, player2):
    if (player1 == 1 and player2 == 3):
        print("Компьютер выйграл ((")
    elif (player1 == 2 and player2 == 1):
        print("Компьютер тебя победил ((")
    elif (player1 == 3 and player2 == 2):
        print("Востание машин, тебя сильно оскорбила машина и да, ты проиграл")
    elif (player1 == player2):
        print("Ничья")
    else: print("Вау, да ты молодец, ты победил")

def cheker():
    flag = 0;
    while (flag == 0):
        player_input = input("Введите число от 1 до 3: ")
        if (player_input == '1' or player_input == '2' or player_input == '3'):
            flag = 1
    return player_input
    #player_input = input("Введите число от 1 до 3: ")
    #while type(player_input) != int:
        #if type(player_input) != int:
            #print("Дружочек цифры от , не буквы")
        #player_input = input("Введите число от 1 до 3: ")
    #return player_input
def whatsim(inp):
    if inp == 1: s = 'камень'
    elif inp == 2: s = 'ножницы'
    else: s = 'бумага'
    return s

print("КАМЕНЬ-НОЖНИЦЫ-БУМАГА")
print("Правила:"
      " 1 - камень, 2 - ножницы, 3 - бумага")
print("Камень бьет ножницы, ножницы бьют бумагу, бумага бьет камень")
player_input = int(cheker())
pc_input = random.randint(1,3)
print("Комппьютер выбрал ", pc_input, whatsim(pc_input))
whowins(player_input,pc_input)
