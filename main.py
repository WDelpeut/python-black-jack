import random
from art import logo
from replit import clear

def deal_card(player_cards):
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    if card == 11 and card + sum(player_cards) > 21:
        card = 1
    return card

wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
while wanna_play == "y":
    clear()
    print(logo)
    
    winner = ""
    message = ""
    guest_cards = []
    computer_cards = []

    for _ in range(2):
        guest_cards.append(deal_card(guest_cards))
        computer_cards.append(deal_card(computer_cards))

    print(f"Your cards: {guest_cards}, current score: {sum(guest_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    # Guest's turn
    guests_turn = True

    while guests_turn:
        next_try = input("Type 'y' to get another card, type 'n' to pass: ")
        
        if next_try == "n":
            guests_turn = False
            continue

        guest_cards.append(deal_card(guest_cards))
        
        if sum(guest_cards) > 21:
            winner = "computer"
            message = "You went over."
            guests_turn = False
            continue
        elif sum(guest_cards) == 21:
            guests_turn = False
            continue

        print(f"Your cards: {guest_cards}, current score: {sum(guest_cards)}")
        

    # Computer's turn
    computers_turn = True
    
    while computers_turn:
        if winner == "computer":
            computers_turn = False
            continue
        elif sum(computer_cards) > 21:
            winner = "guest"
            computers_turn = False
        elif sum(computer_cards) > sum(guest_cards):
            winner = "computer"
            computers_turn = False
        elif sum(computer_cards) == sum(guest_cards):
            computers_turn = False
        else:
            computer_cards.append(deal_card(computer_cards))

    # Result
    print(f"Your final hand: {guest_cards}, final score: {sum(guest_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    
    if winner == "guest":
        print(f"{message} You win!")
    elif winner == "computer":
        print("You lose")
    else:
        print("It's a draw")

    wanna_play = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
        