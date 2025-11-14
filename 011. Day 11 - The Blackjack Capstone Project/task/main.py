from art import logo
import random

# ----- CONSTANTS -----
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Return a random card from the deck."""
    return random.choice(cards)


def calculate_score(hand):
    """Calculate the score of a hand.

    - If the hand is a 'Blackjack' (21 with 2 cards), return 0 as a special code.
    - Handle Aces (11 -> 1) if over 21.
    """
    score = sum(hand)

    # Check for a Blackjack (21 with 2 cards)
    if score == 21 and len(hand) == 2:
        return 0  # special code for Blackjack

    # Handle Aces: turn 11 into 1 if we bust
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)

    return score


def compare(user_score, computer_score):
    """Compare the user and computer scores and return the game result string."""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []

    # Deal initial 2 cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Show current state
        print(f"Your cards: {user_cards}, current score: {user_score if user_score != 0 else 21}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for blackjack or busts
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if draw == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Dealer's turn: draw until 17 or more (unless already Blackjack)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final hands
    final_user_score = user_score if user_score != 0 else 21
    final_computer_score = computer_score if computer_score != 0 else 21

    print(f"Your final hand: {user_cards}, final score: {final_user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {final_computer_score}")
    print(compare(user_score, computer_score))


# Main game loop
while True:
    play_game_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game_input == 'y':
        print("\n" * 20)
        play_game()
    elif play_game_input == 'n':
        break
    else:
        print("ERROR! Enter a valid input")
