# BlackJack21
import random

version = "0.9.2"
# Изменяемые переменные
playerpoints = 0
dealerpoints = 0
playercards, dealercards = list(), list()

# Добавить логику добора/перебора кард у дилера

# Правила игры
rules = "Цель игры — набрать 21 очко или близкую к этому сумму.\nЕсли игрок набирает сумму очков, превышающую 21, то его ставка проигрывает.\nЕсли сумма очков на картах дилера больше, чем 21, то все ставки, оставшиеся в игре, выигрывают.\nИгроки, набравшие сумму очков большую, чем дилер, выигрывают, их ставки оплачиваются 1:1."
card_value = "Значения очков каждой карты: от двойки до десятки — от 2 до 10 соответственно, у туза — 1 или 11 (11 пока общая сумма не больше 21, далее 1), у картинок (король, дама, валет) — 10."


# Колода и перетасовка
def shuffle_deck():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A",
            2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    random.shuffle(deck)
    return deck


# Игра (Основная функция)
def game(deck_new):
    # count_p(int(input("Сколько игроков будет?\n"))) # Need to add logic for more players
    chek_win(deck_new)
    # print(playerpoints, dealerpoints)  # DEBUG---------------------
    main()


def menu(deck_new):
    print("1. Начать игру\n2. Значения карт\n3. Правила игры\n4. Выход")
    menu_choice = input()
    if menu_choice == "1":
        game(deck_new)
    elif menu_choice == "2":
        print(card_value)
        menu(deck_new)
    elif menu_choice == "3":
        print(rules)
        menu(deck_new)
    elif menu_choice == "4":
        exit()
    else:
        print("Неверный ввод!")
        menu(deck_new)


# Проверка на победу
def chek_win(deck_new):
    dealer(deck_new)
    player(deck_new)
    global playerpoints, dealerpoints
    if playerpoints > 21:
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
        print(f'playerpoints = {playerpoints}, dealerpoints = {dealerpoints} Error maybe?')  # DEBUG
    print(f'Карты игрока = {playercards}, Карты дилера{dealercards}\nОчки игрока = {playerpoints}, Очки дилера = {dealerpoints}')  # DEBUG
    print('*****************************************************************************************\n\n')


# main  Вызывает menu(), player() dealer() game()
def main():
    playercards.clear()
    dealercards.clear()
    deck_new = shuffle_deck()
    print(f"Hello! U are in BlackJack21_{version}")
    menu(deck_new)
    game(deck_new)


# Подсчёт очков
def points(cards, old_points):
    point = 0
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


# Взять еще
def add_card(deck_s):
    added_card = deck_s.pop(0)
    print(added_card)  # DEBUG---------------------
    return added_card


# -SOON-
# Добавить игрока
# def count_p(count_of_player):
#     pass


# Игрок
# Начальные карты игрока
def player(deck_s):
    global playerpoints, playercards
    # print(f"Получил{deck}") 						#DEBUG---------------------
    cards = [deck_s.pop(0), deck_s.pop(0)]
    # Добавить карты в список карт игрока
    playercards.append(cards)
    print(f"Ваши начальные карты\n{cards[0]} и {cards[1]}\nСумма ваших очков {points(cards, old_points=0)}")
    # Подсчёт очков
    playerpoints = points(cards, old_points=0)
    if playerpoints == 21:
        print("БлекДжек!!!")
        return
    # Взять еще карту или остановиться (пока не перебор)
    choose = input("Взять еще H, Остановится S\n")
    if choose == 'H':
        i = [add_card(deck_s)]
        # Добавить карту в список карт игрока
        playercards.append(i)
        playerpoints += points(i, playerpoints)
        # Проверка на перебор
        if playerpoints > 21:
            print(f"Перебор! Ваши очки {playerpoints}")
            return
        # Взять еще карту или остановится (пока не перебор)
        var = input(f"Новая сумма карт {playerpoints}\nВзять еще H, Остановиться S\n")
        # цикл пока вводят H
        while var == 'H':
            d = [add_card(deck_s)]
            # Добавить карту в список карт игрока
            playercards.append(d)
            playerpoints += points(d, playerpoints)
            if playerpoints == 21:
                print("БлекДжек!!!")
                return
            elif playerpoints > 21:
                print(f"Перебор! Ваши очки {playerpoints}")
                return
            var = input(f"Новая сумма карт {playerpoints}\nВзять еще H, Остановиться S\n")
    print('Ваши карты!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', playercards)
    return playerpoints


# Дилер
# Начальные карты дилера
def dealer(deck_s):
    # print(f"Получил{deck}") 						#DEBUG---------------------
    cards = [deck_s.pop(0), deck_s.pop(0)]  # Первые 2 карты дилера ( одна открытая вторая закрытая)
    print(f'Первая карта дилера {cards[0]}')
    # print(f"Оставил{deck}") 						#DEBUG---------------------
    global dealerpoints
    dealerpoints = points(cards, old_points=0)
    # механика игрока поменять для дилера#DEBUG---------------------
    # if choose == 'H':#DEBUG---------------------
    # dealerpoints += add_card(deck)#DEBUG---------------------
    return dealerpoints, cards


main()
