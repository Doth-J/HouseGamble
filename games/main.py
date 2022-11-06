from roulette import Roulette
from blackjack import Blackjack

print("\n"+"* ~ "*5+"HOUSE GAMBLE"+" ~ *"*5+"\n")
money = int(input("Enter initial amount: "))
choice = "none"
while choice != "exit":
    choice = input("Choose game: ")
    if choice == "R":
        game = Roulette()
        money = game.play(money)
    elif choice == "B":
        game = Blackjack()
        money = game.play(money)