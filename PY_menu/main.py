from pickle import TRUE
import game
import pulpit

def move(Gra):
    while TRUE:
        action = input("[CH]ECK / [P]ASS / [R]AISE \n").lower()  # Wybór ruchu gracza
        if action == 'p':
            Gra.players_list[0].passed = True
            break
        elif action == 'ch':
            break
        elif action == 'r':
            while TRUE:
                new_bet = int(input("Podaj ilość podnoszenia stawki: \n"))
                if new_bet <= Gra.players_list[0].bet:
                    print("Podano zbyt niską wartość!")
                else:
                    Gra.players_list[0].bet = new_bet
                    break
            break
        else:
            print("Zła komenda, proszę spróbować ponownie.")
