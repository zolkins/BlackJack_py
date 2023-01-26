# BlackJack21
import random  # Импорт модуля рандома
import sys

version = "0.9.9|Single_Player"  # Версия программы
print(f"Hello! U are in BlackJack21_{version}")

# Изменяемые переменные
playerpoints, dealerpoints = int(), int()
playercards, dealercards = list(), list()

# Правила игры
rules = "Цель игры — набрать 21 очко или близкую к этому сумму.\nЕсли игрок набирает сумму очков, превышающую 21, то его ставка проигрывает.\n" \
        "Если сумма очков на картах дилера больше, чем 21, то все ставки, оставшиеся в игре, выигрывают." \
        "\nИгроки, набравшие сумму очков большую, чем дилер, выигрывают, их ставки оплачиваются 1:1."
card_value = "Значения очков каждой карты: от двойки до десятки — от 2 до 10 соответственно, у туза — 1 или 11\n" \
             "(11 пока общая сумма не больше 21, далее 1), у картинок (король, дама, валет) — 10."


# Колода и перетасовка
def shuffle_deck():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4  # Создание колоды из 52 карт (4 масти по 13 карт)
    random.shuffle(deck)  # Перетасовка колоды
    return deck


def menu():
    menu_choice = input("1. Начать игру\n2. Значения карт\n3. Правила игры\n4. Выход\n")
    if menu_choice == "1":
        chek_win(shuffle_deck())
        while input("Хотите еще раз? - 1\nВыход - 0\n") == "1":
            chek_win(shuffle_deck())
        else:
            sys.exit()
    elif menu_choice == "2":
        print(card_value)
        menu()
    elif menu_choice == "3":
        print(rules)
        menu()
    elif menu_choice == "4":
        sys.exit()
    else:
        print("Неверный ввод!")
        menu()


# Проверка на победу и инициализация игроков и дилера
def chek_win(deck_new):
    playercards.clear(), dealercards.clear()    # Очистка карт игроков и дилера перед началом игры
    dealer(deck_new)
    player(deck_new)
    global playerpoints, dealerpoints
    if playerpoints == dealerpoints:
        print("Ничья!")
    elif playerpoints > 21:
        print("Проигрыш! игрока, дилер победил!(перебор)")
    elif dealerpoints > 21:
        print("Проигрыш! дилера, игрок победил!(перебор)")
    elif playerpoints == 21:
        print("БлекДжек Игрока!!!!")
    elif dealerpoints == 21:
        print("БлекДжек Дилера!!!")
    elif dealerpoints < playerpoints < 21 and dealerpoints < 21:
        print("Победа игрока!!!!(по очкам до 21)")
    elif playerpoints < dealerpoints < 21 and playerpoints < 21:
        print("Победа дилера! (по очкам до 21)")
    elif playerpoints == dealerpoints:
        print("Ничья! (по очкам до 21)")
    else:
        print(f' \t\tplayerpoints = {playerpoints}, dealerpoints = {dealerpoints} Error maybe?')  # DEBUG
    print(
        f'Карты игрока = {playercards}, Карты дилера{dealercards}\nОчки игрока = {playerpoints}, Очки дилера = {dealerpoints}')  # DEBUG
    print('*****************************************************************************************\n')


# Подсчёт очков
def points(cards, old_points):
    point = 0
    if cards.count("A") == 2:
        point = 12
        return point
    for i in cards:
        if i != "A":
            if type(i) == str:
                point += 10
            else:
                point += i

    if "A" in cards:
        if old_points + 11 <= 21:
            point += 11
        else:
            point += 1
    return point


# Игрок
def player(deck_s):
    global playerpoints, playercards
    playercards = [deck_s.pop(0), deck_s.pop(0)]
    playerpoints = points(playercards, 0)   # Подсчёт очков
    print(f"\nВаши начальные карты\n{playercards[0]} и {playercards[1]}\nСумма ваших очков {playerpoints}\n")
    if playerpoints == 21:
        print("БлекДжек!!!")
        return
    # Взять еще карту или остановиться (пока не перебор)
    while playerpoints < 21:
        print("H - Взять еще\nS - Стоп")
        choice = input()
        if choice == "H":
            playercards.append(deck_s.pop(0))
            playerpoints = points(playercards, playerpoints)
            print(f"Ваши карты {playercards}\nСумма ваших очков {playerpoints}")
        elif choice == "S":
            print("Стоп")
            break
    if playerpoints > 21:
        print("Перебор!")
    return playerpoints


# Дилер
def dealer(deck_s):
    global dealerpoints, dealercards
    dealercards = [deck_s.pop(0), deck_s.pop(0)]  # Первые 2 карты дилера ( одна открытая вторая закрытая)
    print(f"Карты дилера:\t{dealercards[0]} и закрытая")
    dealerpoints = points(dealercards, 0)
    while dealerpoints <= 11:
        dealercards.append(deck_s.pop(0))   # Добавить карту в список карт дилера
        dealerpoints = points(dealercards, dealerpoints)
    if dealerpoints <= 14:
        if random.randint(0, 1) == 1:
            dealercards.append(deck_s.pop(0))   # Добавить карту в список карт дилера
            dealerpoints = points(dealercards, dealerpoints)
    elif dealerpoints <= 17:
        if random.randint(0, 1) == 1:
            dealercards.append(deck_s.pop(0))   # Добавить карту в список карт дилера
            dealerpoints = points(dealercards, dealerpoints)
        else:
            print("Дилер пропускает ход")
    else:
        print("Дилер пропускает ход")
    return dealerpoints


menu()
