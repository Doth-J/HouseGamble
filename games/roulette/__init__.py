import random

class Roulette:

    def __init__(self):
        self.rnums = [k for k in range(37)]
        rcols = [' ','B','R']
        self.board = {}
        for num in self.rnums:
            if num==0:
                self.board[num] = str(num)+rcols[num]
            elif num > 10 and num <20 or num > 27:
                self.board[num] = str(num)+rcols[1] if num % 2 == 1 else str(num)+rcols[2]
            else:
                self.board[num] = str(num)+rcols[1] if num % 2 == 0 else str(num)+rcols[2]
                
    def print_board(self):
        for key in self.board.keys():
            if key == 0:
                print('\t'+self.board[key],end='\t')
            else:
                if key % 3 == 1:
                    print()
                print(self.board[key],end="\t")
        print('\n')

    def throw_ball(self):
        return self.board[random.choice(self.rnums)]

    def reward(self,bet:str,chip:int):
        if bet =="B" or bet=="R":
            return chip*2
        else:
            return chip*35

    def play(self,money:int):
        print("\n"+"* "*3+"ROULETTE"+" *"*3)
        self.print_board()
        chip = int(input("Set chip value: "))
        bet = input("Place your bet: ")
        valid = False
        while bet != "exit":
            
            # Bet checking
            if bet.isdigit() and int(bet) >= 0 and int(bet)<37:
                bet = self.board[int(bet)]
                valid = True
            elif bet.isalpha() and (bet=="B" or bet=="R"):
                valid = True
            elif bet == "show":
                self.print_board()
                valid = False
            elif bet == "chip":
                chip = int(input("Change chip value: "))
                valid = False
            elif bet == "money":
                print(money)
                valid = False
            else:
                print("Invalid bet!")
                valid = False
            
            # Spin Roulette
            if valid:
                print("[-] Chip value: "+ str(chip))
                money -= chip
                print("[^] Your bet: "+ bet)
                res = self.throw_ball()
                print("[*] Lucky Number: "+ res)
                if res == bet or ((bet=="B" or bet=="R") and bet in res):
                    money += self.reward(bet,chip)
                    print("Winner winner chicken dinner!")
                else:
                    print("Better luck next time...")

            # Money check
            if money <=0:
                print("No money left!")
                break

            bet = input("Place your bet: ")
        return int(money)


