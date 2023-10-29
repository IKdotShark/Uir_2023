import random

def whowins(player1, player2):
    if (player1 == 1 and player2 == 3):
        out = "Компьютер выйграл (("
    elif (player1 == 2 and player2 == 1):
        out = "Компьютер выйграл (("
    elif (player1 == 3 and player2 == 2):
        out = "Компьютер выйграл (("
    elif (player1 == player2):
        out = "Ничья"
    else:
        out = "Вау, да ты молодец, ты победил"
    return out

def cheker(k):
    flag = 0;
    if k == 1:
        while (flag == 0):
            player_input = input("Введите число от 1 до 3: ")
            if (player_input == '1' or player_input == '2' or player_input == '3'):
                flag = 1
    else:
        while (flag == 0):
            player_input = input("Введите 1 для продолжения, 0 для выхода: ")
            if (player_input == '1' or player_input == '0'):
                flag = 1
    return player_input

def whatsim(inp):
    if inp == 1: s = 'камень'
    elif inp == 2: s = 'ножницы'
    else: s = 'бумага'
    return s

def standart():
    flag = 1
    while (flag == 1):
        print("КАМЕНЬ-НОЖНИЦЫ-БУМАГА")
        print("Правила:"
              " 1 - камень, 2 - ножницы, 3 - бумага")
        print("Камень бьет ножницы, ножницы бьют бумагу, бумага бьет камень")
        player_input = int(cheker(1))
        pc_input = random.randint(1, 3)
        print("Комппьютер выбрал ", pc_input, " - ", whatsim(pc_input))
        whowins(player_input, pc_input)
        flag = int(cheker(2))

def tournir(i):
    player_wins = 0
    pc_wins = 0
    draw = 0
    while (i != 0):
        print("КАМЕНЬ-НОЖНИЦЫ-БУМАГА")
        print("Правила:"
              " 1 - камень, 2 - ножницы, 3 - бумага")
        print("Камень бьет ножницы, ножницы бьют бумагу, бумага бьет камень")
        player_input = int(cheker(1))
        pc_input = random.randint(1, 3)
        print("Комппьютер выбрал ", pc_input, " - ", whatsim(pc_input))
        i -= 1
        s = whowins(player_input,pc_input)
        if (s == "Компьютер выйграл (("): pc_wins += 1
        elif (s == "Ничья"): draw += 1
        else: player_wins += 1
    print("Ты выйграл ", player_wins, "матчей; "
                                      "Компьютер выйиграл", pc_wins, "матчей; ",
          "Ничья ", draw)
    if (player_wins == pc_wins):
        print("Итог ничья, играй еще")
        standart()
    elif (player_wins > pc_wins): print("Ты выйграл турнир")
    else: print("Компьютер восстал")

print("Турнир - 1 или стандарт - 2, выход 0")
flag = input()
if flag.isdigit():
    flag = int(flag)
while (flag != 1 and flag != 2 and flag != 0):
    print("Турнир - 1 или стандарт -2, выход 0")
    flag = input()
    if flag.isdigit():
        flag = int(flag)
if flag == 1:
    rounds = int(input("Сколько раундов: "))
    tournir(rounds)
elif flag == 2:
    standart()