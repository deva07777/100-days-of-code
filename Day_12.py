import random

def play_blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = random.choices(cards, k=2)
    computer_card = random.choice(cards)
    
    # Use a loop instead of calling the function inside itself
    game_over = False
    while not game_over:
        current_score = sum(player_hand)
        print(f"\nYour cards: {player_hand}, current score: {current_score}")
        print(f"Computer's first card: {computer_card}")

        if current_score > 21:
            print("You went over. You lose! 😤")
            game_over = True
        elif current_score == 21:
            print("Blackjack! You win! 🥳")
            game_over = True
        else:
            user_should_continue = input("Type 'y' to hit, 'n' to stand: ").lower()
            if user_should_continue == 'y':
                player_hand.append(random.choice(cards))
            else:
                game_over = True
                print(f"Your final score is {current_score}. Dealer's turn...")

play_blackjack()