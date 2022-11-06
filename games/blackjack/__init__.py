import random

class Blackjack:
    def __init__(self):
        nums = [k for k in range(2,11)]
        figs = ["A","J","Q","K"]
        symbs = ["C|B","D|R","H|R","S|B"]
        index = 0
        cards = {}
        for symb in symbs:
            for num in nums:
                cards[index] = str(num)+"|"+symb
                index+=1
            for fig in figs:
                cards[index] = fig+"|"+symb
                index+=1
        random.shuffle(cards)
        self.deck = [cards[key] for key in cards.keys()]
    
    def deal_cards(self, hand:int):
        return [self.deck.pop() for _ in range(hand)]

    def get_card(self):
        return self.deck.pop()
    
    def reward(self, bet:str, chip:int):
        pass

    def play(self, money:int):
        print("\n"+"* "*3+"BLACKJACK"+" *"*3)
        chip = int(input("Set chip value: "))
        bet = "cards"
        while bet != "exit":
            print("[-] Chip value: "+ str(chip))
            money -= chip
            dealer = self.deal_cards(2)
            table = self.deal_cards(3)
            you = self.deal_cards(2)
            print("[&] Dealer: *, " + str(dealer[0]))
            print("[^] Table: " + str(table))
            while bet.isalpha():
                if bet == "table":
                    print("[^] Table: " + str(table))
                elif bet == "dealer":
                    print("[&] Dealer: *, " + str(dealer[0]))
                elif bet == "cards":
                    print("[*] You: " + str(you))
                elif bet == "deck":
                    print(str(self.deck))
                elif bet == "chip":
                    chip = int(input("Change chip value: "))
                elif bet == "money":
                    print(money)
                else:
                    print("Invalid bet!")
                bet = input("Place your bet: ")
            money =- int(bet)*chip
            table.append(self.get_card())
            print("[^] Table: " + str(table))
            bet = input("Place your bet: ")
            while bet.isalpha():
                if bet == "table":
                    print("[^] Table: " + str(table))
                elif bet == "dealer":
                    print("[&] Dealer: *, " + str(dealer[0]))
                elif bet == "cards":
                    print("[*] You: " + str(you))
                elif bet == "chip":
                    chip = int(input("Change chip value: "))
                elif bet == "money":
                    print(money)
                else:
                    print("Invalid bet!")
                bet = input("Place your bet: ")
            money =- int(bet)*chip
            table.append(self.get_card())
            print("[^] Table: " + str(table))
            bet = input("Place your bet: ")
            while bet.isalpha():
                if bet == "table":
                    print("[^] Table: " + str(table))
                elif bet == "dealer":
                    print("[&] Dealer: *, " + str(dealer[0]))
                elif bet == "cards":
                    print("[*] You: " + str(you))
                elif bet == "chip":
                    chip = int(input("Change chip value: "))
                elif bet == "money":
                    print(money)
                else:
                    print("Invalid bet!")
                bet = input("Place your bet: ")
            


        return money   
            
