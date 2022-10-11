# BlackJack21
import random  # Импорт модуля рандома

version = "0.9.9_dev_more_p_WORK"  # Версия программы
print(f"Hello! U are in BlackJack21_{version}")

# Изменяемые переменные
pc_1, pc_2, pc_3, pc_4, dealercards = list(), list(), list(), list(), list()  # Карты
pp_1, pp_2, pp_3, pp_4, dealerpoints = int(), int(), int(), int(), int()  # Очки


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
        chek_win(shuffle_deck(), count_p())
        menu()
    elif menu_choice == "2":
        print(card_value)
        menu()
    elif menu_choice == "3":
        print(rules)
        menu()
    elif menu_choice == "4":
        exit()
    else:
        print("Неверный ввод!")
        menu()


# Проверка на победу и инициализация игроков и дилера
def chek_win(deck_new, count_players):
    player_number = 1
    dealer(deck_new)
    while player_number <= count_players:
        print(f"Игрок {player_number}")
        player(deck_new, player_number)
        player_number += 1
    print(f"Дилер: {dealercards} = {dealerpoints}")
    print(f"Игрок 1: {pc_1} = {pp_1}")
    if count_players >= 2:
        print(f"Игрок 2: {pc_2} = {pp_2}")
    if count_players >= 3:
        print(f"Игрок 3: {pc_3} = {pp_3}")
    if count_players >= 4:
        print(f"Игрок 4: {pc_4} = {pp_4}")
    if dealerpoints > 21:
        print("Дилер проиграл!")
        if pp_1 > 21:
            print("Игрок 1 проиграл!")
        else:
            print("Игрок 1 выиграл!")
        if count_players >= 2:
            if pp_2 > 21:
                print("Игрок 2 проиграл!")
            else:
                print("Игрок 2 выиграл!")
        if count_players >= 3:
            if pp_3 > 21:
                print("Игрок 3 проиграл!")
            else:
                print("Игрок 3 выиграл!")
        if count_players >= 4:
            if pp_4 > 21:
                print("Игрок 4 проиграл!")
            else:
                print("Игрок 4 выиграл!")
    elif dealerpoints == 21:
        print("Дилер выиграл!")
        if pp_1 > 21:
            print("Игрок 1 проиграл!")
        else:
            print("Игрок 1 проиграл!")
        if count_players >= 2:
            if pp_2 > 21:
                print("Игрок 2 проиграл!")
            else:
                print("Игрок 2 проиграл!")
        if count_players >= 3:
            if pp_3 > 21:
                print("Игрок 3 проиграл!")
            else:
                print("Игрок 3 проиграл!")
        if count_players >= 4:
            if pp_4 > 21:
                print("Игрок 4 проиграл!")
            else:
                print("Игрок 4 проиграл!")
    elif dealerpoints < 21:
        if pp_1 > 21:
            print("Игрок 1 проиграл!")
        elif pp_1 > dealerpoints:
            print("Игрок 1 выиграл!")
        elif pp_1 == dealerpoints:
            print("Игрок 1 проиграл!")
        else:
            print("Игрок 1 проиграл!")
        if count_players >= 2:
            if pp_2 > 21:
                print("Игрок 2 проиграл!")
            elif pp_2 > dealerpoints:
                print("Игрок 2 выиграл!")
            elif pp_2 == dealerpoints:
                print("Игрок 2 проиграл!")
            else:
                print("Игрок 2 проиграл!")
        if count_players >= 3:
            if pp_3 > 21:
                print("Игрок 3 проиграл!")
            elif pp_3 > dealerpoints:
                print("Игрок 3 выиграл!")
            elif pp_3 == dealerpoints:
                print("Игрок 3 проиграл!")
            else:
                print("Игрок 3 проиграл!")
        if count_players >= 4:
            if pp_4 > 21:
                print("Игрок 4 проиграл!")
            elif pp_4 > dealerpoints:
                print("Игрок 4 выиграл!")
            elif pp_4 == dealerpoints:
                print("Игрок 4 проиграл!")
            else:
                print("Игрок 4 проиграл!")
    menu()


# Подсчёт очков
def points(cards, old_points):
    point = int()
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
    # print(old_points)
    return point


# Добавить игрока
def count_p():
    count = int(input("Сколько игроков будет?(Максимум 4)\n"))
    if count <= 4:
        return count
    else:
        print("Неверный ввод!")
        menu()


# Логика игроков
def player(deck_s, player_number):
    global pp_1, pp_2, pp_3, pp_4, pc_1, pc_2, pc_3, pc_4
    if player_number == 1:
        pc_1 = [deck_s.pop(0), deck_s.pop(0)]
        print(f"Ваши карты: {pc_1}")
        pp_1 = points(pc_1, 0)
        print(f"Ваши очки: {pp_1}")
        if pp_1 == 21:
            print("БлекДжек!")
            return
        while pp_1 < 21:
            print("H - Взять еще\nS - Стоп")
            choice = input()
            if choice == "H":
                pc_1.append(deck_s.pop(0))
                print(f"Ваши карты: {pc_1}")
                pp_1 = points(pc_1, pp_1)
                print(f"Ваши очки: {pp_1}")
            elif choice == "S":
                print("Стоп")
                break
            else:
                print("Неверный ввод!")
        if pp_1 > 21:
            print("Перебор!")

    elif player_number == 2:
        pc_2 = [deck_s.pop(0), deck_s.pop(0)]
        print(f"Ваши карты: {pc_2}")
        pp_2 = points(pc_2, 0)
        print(f"Ваши очки: {pp_2}")
        if pp_2 == 21:
            print("БлекДжек!")
            return
        while pp_2 < 21:
            print("H - Взять еще\nS - Стоп")
            choice = input()
            if choice == "H":
                pc_2.append(deck_s.pop(0))
                print(f"Ваши карты: {pc_2}")
                pp_2 = points(pc_2, pp_2)
                print(f"Ваши очки: {pp_2}")
            elif choice == "S":
                print("Стоп")
                break
            else:
                print("Неверный ввод!")
        if pp_2 > 21:
            print("Перебор!")

    elif player_number == 3:
        pc_3 = [deck_s.pop(0), deck_s.pop(0)]
        print(f"Ваши карты: {pc_3}")
        pp_3 = points(pc_3, 0)
        print(f"Ваши очки: {pp_3}")
        if pp_3 == 21:
            print("БлекДжек!")
            return
        while pp_3 < 21:
            print("H - Взять еще\nS - Стоп")
            choice = input()
            if choice == "H":
                pc_3.append(deck_s.pop(0))
                print(f"Ваши карты: {pc_3}")
                pp_3 = points(pc_3, pp_3)
                print(f"Ваши очки: {pp_3}")
            elif choice == "S":
                print("Стоп")
                break
            else:
                print("Неверный ввод!")
        if pp_3 > 21:
            print("Перебор!")

    elif player_number == 4:
        pc_4 = [deck_s.pop(0), deck_s.pop(0)]
        print(f"Ваши карты: {pc_4}")
        pp_4 = points(pc_4, 0)
        print(f"Ваши очки: {pp_4}")
        if pp_4 == 21:
            print("БлекДжек!")
            return
        while pp_4 < 21:
            print("H - Взять еще\nS - Стоп")
            choice = input()
            if choice == "H":
                pc_4.append(deck_s.pop(0))
                print(f"Ваши карты: {pc_4}")
                pp_4 = points(pc_4, pp_4)
                print(f"Ваши очки: {pp_4}")
            elif choice == "S":
                print("Стоп")
                break
            else:
                print("Неверный ввод!")
        if pp_4 > 21:
            print("Перебор!")


# Дилер
def dealer(deck_s):
    global dealerpoints, dealercards
    dealercards = [deck_s.pop(0), deck_s.pop(0)]  # Первые 2 карты дилера ( одна открытая вторая закрытая )
    print(f"Карты дилера\n{dealercards[0]} и закрытая")
    dealerpoints = points(dealercards, 0)
    while dealerpoints <= 11:
        dealercards.append(deck_s.pop(0))    # Добавить карту в список карт дилера
        dealerpoints = points(dealercards, dealerpoints)
    if dealerpoints <= 14:
        if random.randint(0, 1) == 1:
            dealercards.append(deck_s.pop(0))    # Добавить карту в список карт дилера
            dealerpoints = points(dealercards, dealerpoints)
    elif dealerpoints <= 17:
        if random.randint(0, 1) == 1:
            dealercards.append(deck_s.pop(0))    # Добавить карту в список карт дилера
            dealerpoints = points(dealercards, dealerpoints)
        else:
            print("Дилер пропускает ход")
    else:
        print("Дилер пропускает ход")
    return


menu()
