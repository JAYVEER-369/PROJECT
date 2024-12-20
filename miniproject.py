import random

symbols = ["@", "#", "!", "^", "~"]

tokens = 100
print("Welcome to the Slot Machine Game")

while tokens > 0:
    print(f"You have {tokens} tokens")
    try:
        bet = int(input("Enter your bet: "))
        if bet <= 0 or bet > tokens:
            print("Invalid bet amount")
            continue
    except ValueError:
        print("Enter a valid number")
        continue

    tokens -= bet
    row = [random.choice(symbols) for _ in range(3)]
    print("|", " | ".join(row), "|")

    if row[0] == row[1] == row[2]:
        winnings = bet * 2
        print(f"You won {winnings} tokens!")
        tokens += winnings
    else:
        print("You lost this round")

print("You ran out of tokens. Better luck next time!")
