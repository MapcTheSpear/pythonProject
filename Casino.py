from random import randint
from decouple import config

class CasinoGame:
    def __init__(self):
        self.__my_money = config('My_MONEY', cast=int)

    def play_game(self):
        while self.__my_money > 0:
            bet = int(input("Enter your bet, enter 0 for exit: "))
            if bet == 0:
                print(f'Your final account is {self.__my_money}.')
                print('Exiting...')
                break
            elif bet <= self.__my_money:
                win = randint(1, 30)
                select_slot = int(input("Enter slot you want to bet on: "))
                if select_slot <= 0 or select_slot > 30:
                    print('INVALID VALUE, PLEASE TRY AGAIN!')
                    continue
                elif select_slot == win:
                    self.__my_money += bet
                    print(f'You won. Slot is {win}. Your account is {self.__my_money} now')
                else:
                    self.__my_money -= bet
                    print(f'You lost. Slot was {win}. Yout account is {self.__my_money} now')



if __name__ == "__main__" :
    casino = CasinoGame()
    casino.play_game()
