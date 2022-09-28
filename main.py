# BlackJack21
import random
version = "0.7"
playerpoints = 0
dealerpoints = 0

# TASK_LIST
#	Реализовать Туз, когда он 11 когда 1
#	Добавить логику добора/перебора кард у дилера

#Правила игры 
rules = "Цель игры — набрать 21 очко или близкую к этому сумму. Если игрок набирает сумму очков, превышающую 21, то его ставка проигрывает. Если сумма очков на картах дилера больше, чем 21, то все ставки, оставшиеся в игре, выигрывают. Игроки, набравшие сумму очков большую, чем дилер, выигрывают, их ставки оплачиваются 1:1."
card_value = "Значения очков каждой карты: от двойки до десятки — от 2 до 10 соответственно, у туза — 1 или 11 (11 пока общая сумма не больше 21, далее 1), у т. н. картинок (король, дама, валет) — 10."

# Колода и перетасовка
deck = ["J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "Ace", "Ace", "Ace", "Ace", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]
random.shuffle(deck)

def menu():
	menu = input("Меню правил 0|Для пропуска введите пробел\n")
	if menu == '0':
			r = input("Для просмотра правил введите 1\nДля просмотра значения карт 2\n")
			if r == '1':
				print(rules)
				if input("Чтобы вернуться назад введите 1\n") == '1':
					main()
			elif r == '2':
				print(card_value)
				if input("Чтобы вернуться назад введите 1\n") == '1':
					main()

def game():
	count_p(int(input("Сколько игроков будет?\n")))
	chek_win()
	print(playerpoints, dealerpoints) 						#DEBUG---------------------


# Проверка победы
def chek_win():
	player(deck)
	dealer(deck)
	global playerpoints
	global dealerpoints
	if playerpoints > 21:
		print("Проигрыш! игрока, дилер победил!(перебор)")
	elif dealerpoints > 21:
		print("Проигрыш! дилера, игрок победил!(перебор)")
	elif playerpoints == 21:
		print("БлекДжек Игрока!!!!")
	elif dealerpoints == 21:
		print("БлекДжек Дилера!!!")
	elif playerpoints > dealerpoints and playerpoints < 21 and dealerpoints < 21:
		print("Победа игрока!!!!(по очкам до 21)")
	elif dealerpoints > playerpoints and dealerpoints < 21 and playerpoints < 21:
		print("Победа дилера! (по очкам до 21)")
	else:
		print(playerpoints, dealerpoints)


# main  Вызывает Меню правил(), Вызывает player() dealer() game()
def main():
	print(f"Hello! U are in BlackJack21_{version}")
	menu()
	game()


# Подсчет очков
def points(cards):
	point = 0
	for i in cards:
		if i != "Ace":
			if type(i) == str:
				point += 10
			else:
				point += i
		else:
			pass
	return point


# Взять еще
def add_card(deck):
	add_card = deck.pop(0)
	print(add_card) 						#DEBUG---------------------
	return add_card

#-SOON-
# Добавить игрока
def count_p(countPlayer):
	pass
	#print(f"{countPlayer} каунт плейеров") 						#DEBUG---------------------


# Игрок
# Начальные карты игрока
def player(deck):
	#print(f"Получил{deck}") 						#DEBUG---------------------
	cards = [deck.pop(0), deck.pop(0)]
	print(f"Ваши начальные карты\n{cards[0]} и {cards[1]}\nСумма ваших очков {points(cards)}")
	global playerpoints
	playerpoints = points(cards)
	choose = input("Взять еще H, Остановится S\n")
	if choose == 'H':
		i = [add_card(deck)]
		playerpoints += points(i)
		var = input(f"Новая сумма карт {playerpoints}\nВзять еще H, Останивится S\n")
		while(var == 'H'):
			d = [add_card(deck)]
			playerpoints += points(d)
			if playerpoints >= 21:
				break
			var = input(f"Новая сумма карт {playerpoints}\nВзять еще H, Останивится S\n")
	return playerpoints
	#print(f"Оставил{deck}") 						#DEBUG---------------------

# Дилер
# Начальные карты дилера
def dealer(deck):
	#print(f"Получил{deck}") 						#DEBUG---------------------
	cards = [deck.pop(0), deck.pop(0)]
	print(f'Карты дилера{cards} сумма очков {points(cards)}') 						#DEBUG---------------------
	#print(f"Оставил{deck}") 						#DEBUG---------------------
	global dealerpoints
	dealerpoints = points(cards)
	#механика игрока поменять для дилера#DEBUG---------------------
	#if choose == 'H':#DEBUG---------------------
	#	dealerpoints += add_card(deck)#DEBUG---------------------
	return dealerpoints


main()
