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
###     def decrease_balance(self, change):     
###          self.balance -= change


last_bet = 0                                            #do wyrzucenia stąd, na razie jest, zeby bylo cokolwiek o tej nazwie             

def call(player: Player, balance: int) -> None:         #sprawdzenie (nie wiem co tu mam wpisac, bo to co  bedzie w tej funkcji zalezy od tego co potem)
    if last_bet == 0:
        raise ValueError
    balance -= last_bet
