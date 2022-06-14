from termcolor import cprint
from pyfiglet import Figlet
import game
import os

def clear_line():
    #Kasuje ostatnią linię
    print("                                                         ")

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')
        
def print_players()

def start_pulpit():
    global wins
    global losses
    players_list = []  # lista graczy [Pleyer()]
    number_of_decks = 0

    while True:
        print("     P O K E R \n    Texas Hold'em")

        # pętla obsługująca dodawanie graczy
        while True:
            age = input("Wpisz wiek gracza: ")
            # sprawdzam czy gracz jest pełnoletni
            if int(age) < 18:
                print("Przepraszamy, ale poker jest  tylko dla pełnoletnich, zapraszamy za ")
                if 18-int(age) == 1:
                    print("rok :)")
                else:
                    print("{} lat :)".format(18-int(age)))
                con = input("[K]ontynuuj\n").lower()
                if con == 'k':
                    continue
            # Dodanie gracza do gry
            players_list.append(game.Player([],0))
            break
        # Pytanie czy można podejść do gry

        temp = input("[R]ozpocznij grę / [W]róć do menu\n").lower()


        if temp == 'r':
            clear()
            break
        else:
            clear()
            continue
    return (players_list, number_of_decks)


def end_pulpit():
    pass
