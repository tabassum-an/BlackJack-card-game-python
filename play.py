import random
import art

def deal_start():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a draw!"
    elif c_score == 0:
        return "opponent has a blackjack. you lose"
    elif u_score > 21:
        return "You went over. you lose"
    elif u_score == 0:
        return "You Win! with a blackjack"
    elif c_score > 21:
        return "opponent went over. you win"
    elif u_score > c_score:
        return "you scored higher. you win"
    else:
        return "You Lose!"


def star_the_game():
    print(art.logo)
    user_card = []
    user_score = -1
    computer_card = []
    computer_score = -1
    is_game_over = False

    for _ in range(2):
       user_card.append(deal_start())
       computer_card.append(deal_start())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            deal_continue = input("Type 'y' to get another card. Type 'n' to pass. ")

            if deal_continue == "y":
                user_card.append(deal_start())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_start())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n"*10)
    star_the_game()