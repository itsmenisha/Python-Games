from art import logo
import random
import os


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        print("Its a Blackjack")
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, server_score, card_u, card_s):
    if user_score == server_score:
        return ("Its a Draw")
    elif user_score > server_score and user_score <= 21:
        return ("You Win")
    elif user_score == 21 and len(card_u) == 2:
        return ("You Win")
    elif server_score == 21 and len(card_s) == 2:
        return ("You Loose")
    elif server_score == 0:
        return ("You win. You have a blackjack")
    elif user_score == 0:
        return ("You Loose. Opponent has a blackjack")
    elif user_score == 0 and server_score == 0:
        return ("Both went over 21")
    elif server_score > 21:
        return ("You win. Opponent went over 21")
    elif user_score > 21:
        print("You Loose. You went over 21")
    elif user_score > 21 and server_score > 21:
        return ("Both went over 21")
    else:
        return ("You Loose")


def play_game():
    card_u = []
    card_s = []
    is_game_over = False

    for _ in range(2):
        card_u.append(deal_cards())
        card_s.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(card_u)
        server_score = calculate_score(card_s)
        print(f'''
            Your card {card_u} and your score is {user_score}
    ''')
        print(f'''
            The computers first card {card_s[0]}
    ''')

        if user_score == 0 or server_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input(
                "type 'y' to get another card and type 'n' to pass:").lower()
            if user_deal == "y":
                card_u.append(deal_cards())
            else:
                is_game_over = True
    while server_score != 0 and server_score < 17:
        card_s.append(deal_cards())
        server_score = calculate_score(card_s)
        print(f'''
            Computer card is {card_s} and its score is {server_score}
        ''')

    os.system('cls')
    print(logo)
    print(f"Your final hand {card_u}")
    print(f"the total: {user_score}")
    print(f"The computers  final hand {card_s} ")
    print(f"the total: {server_score}")
    result = compare(user_score, server_score, card_u, card_s)
    print(result)


while input("do you want to play a  Blakcjack game:(y or n)").lower() == "y":
    os.system('cls')
    print(logo)
    play_game()
