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

def main():
    n = pulpit.start_pulpit() #Odebranie z funkcji start_pulpit zmiennych (Lista graczy , liczba talii)
    Gra = game.Game(n[0],int(n[1])) #Inicjacja klasy Gra typu Game
    while TRUE: #Pętla sprawdzająca kiedy gracz chce odejść od stołu
        Gra.stack_creation()
        Gra.deal_cards()
        Gra.print_table(False)
        move(Gra)
        if Gra.players_list[0].passed:
            print("Poddałeś się, gra przegrana!")
            break

        if Gra.players_list[0].bet == 0:
            print("Gra przegrana, trzeba wejść do gry z jakąkolwiek stawką.")
            break
        Gra.flop = [Gra.deck.pop(), Gra.deck.pop(), Gra.deck.pop()]
        Gra.print_table(False)
        move(Gra)
        if Gra.players_list[0].passed:
            print("Poddałeś się, gra przegrana!")
            break
        Gra.flop.append(Gra.deck.pop())
        Gra.print_table(False)
        move(Gra)
        if Gra.players_list[0].passed:
            print("Poddałeś się, gra przegrana!")
            break
        Gra.flop.append(Gra.deck.pop())
        Gra.print_table(False)
        move(Gra)
        if Gra.players_list[0].passed:
            print("Poddałeś się, gra przegrana!")
            break

        Gra.print_table(True)
        score = Gra.points()
        print("Otrzymujesz {} punktów!".format(score))
        input()
    pulpit.end_pulpit()
    
main()
