from typing import List


def fold(player: Player, current_deck: List[Card]) -> None:            #gracz passuje
    current_deck.append(player.cards[-1])                              #karta wraca do decku a potem jest zabierana graczowi (irl jest na odwrot)
    del player.cards[-1]
    current_deck.append(player.cards[-2])
    del player.cards[-2]
    deck.deck_update(current_deck.cards)

    
b_blind = 50                                                                   #to jest do zmiany, np. zeby pytac sie na poczatku gracza, jakie stawki chce


def play(player: Player, current_bet: int, balance: int) -> int:               #gracz gra (przebicie, tak?)
    player.bet = int(input("Wybierz kwotę, którą chcesz zagrać: "))            #jaką kwotą
    if bet > balance or bet < 2 * b_blind or bet <= current_bet:               #jesli da za malo albo za duzo to jest zle
        raise ValueError
    balance -= player.bet                                                      #ta kwota jest mu zabierana z konta tak jakby
    return player.bet                                                          #zwraca bet (zapamietuje), zeby moc go potem podpisac pod last_bet, zeby call mial z czego korzystac, tj. last_bet = play(...)

### do klasy Player przydałoby się self.balance i funkcje increase/decrease tego typu:
###     def decrease_balance(self, change) -> None:     
###          self.balance -= change


last_bet = 0                                            #do wyrzucenia stąd, na razie jest, zeby bylo cokolwiek o tej nazwie             


def call(player: Player, balance: int) -> None:         #sprawdzenie
    if last_bet == 0:
        raise ValueError
    balance -= last_bet                                 #znowu przydałby player.balance; gracz stawia tyle, ile ostatni zaklad
    
    
 def flop(current_deck: List[Card]) -> List[Card]:
    card1 = random.choice(current_deck)                         #wybór 3 kart i usuniecie ich z decku
    current_deck.cards.remove(card1)                            #idk czy one powinny byc losowe czy z poczatku
    card2 = random.choice(current_deck)
    current_deck.cards.remove(card2)
    card3 = random.choice(current_deck)
    current_deck.cards.remove(card3)
    deck.deck_update(current_deck)
    print("Karta 1: {} {}".format(card1.suit, card1.value))     #wypisywanie, jakie to są karty
    print("Karta 2: {} {}".format(card2.suit, card2.value))
    print("Karta 3: {} {}".format(card3.suit, card3.value))
    return [card1, card2, card3]                                #zwraca karty, bo wtedy korzystajac z tej listy mozna sobie wybrac tę, z którą się robi cos

### polecam jakas funckje w klasie Game typu set_flop, bo lista flop jest polem w tej klasie, a ta funckja powzsza flop wlasnie te liste zwraca
### def set_flop(self, new_flop) -> None:
###     flop = deepcopy(new_flop)
### ^(wtedy oczywiscie from copy import deepcopy);
