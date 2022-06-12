#### punktacja
### tutaj funkcja, w ktorej gracz wybiera karty do swojej kombinacji ###

def choose_cards(player: Player, current_flop: List[Card]) -> List[Card]: #zwraca liste kart potrzebna do kolejnej funkcji
    cards = []
    i = 1
    for card in player.cards:                   #wybieranie ze swoich kart
        print("Chcesz użyć karty {}?(wpisz {})".format(i, i))
        if card == i:
            cards.append(card)
        i += 1
    j = 1
    for card in current_flop:                   #wybieranie z flopa
        print("Chcesz użyć karty {}?(wpisz {})".format(j, j))
        if len(cards) <= 5:
            if card == j:
                cards.append(card)
            j += 1
        print("Wybrał*ś już 5 kart!")
    return cards


def royal_flush(cards: List[Card], player: Player) -> None:
    score = 10                              #do zmiany moze byc ta ilosc punktow
    card1 = cards[0]
    if len(cards) != 5:
        return None
    for card in cards:
        if card.suit != card1.suit:
            return None
    for card in cards:
        if not (card.value == 10 or card.value == 11 or card.value == 12 or card.value == 13 or card.value == 14) and (card != card1):
            return None
    print("Royal flush! Zyskujesz {} punktow".format(score))
    player.new_score(score)
        #funckja w klasie ktora dodaje punkty
        ### w klasie Player przydałoby sie pole score - ile gracz ma aktualnie punktów


#funkcja działająca podobnie/analogicznie do royal_flush        
def straight_flush(cards: List[Card], player: Player) -> None:
    score = 9
    card1 = cards[0]
    if len(cards) != 5:
        return None
    for card in cards:
        if card.suit != card1.suit:
            return None
    print("Straight flush! Zyskujesz {} punktow".format(score))
    player.new_score(score)

    
def four_of_a_kind(cards: List[Card], player: Player) -> None:      
    score = 8
    card1 = cards[0]
    if len(cards) != 4:
        return None
    for card in cards:
        if card.value != card1.value:                           #jesli jakas wartosc jest inna to konczy
            return None
    print("Four of a kind! Zyskujesz {} punktow".format(score))
    player.new_score(score)    

    
card_values = [] #lista ze wszystkimi wartosciami, nie pamietam czy istnieje, mozliwe, ze tak jest


def full_house(cards: List[Card], player: Player) -> None:
    score = 7
    if len(cards) != 5:
        return None
    values = []
    values_freq = []
    for card in cards:                                          #tworzenie listy samych wartosci z kart
        values.append(card.value)
    for value in card_values:                                   #zlicz ile razy dana wartosc jest w liscie values i dodaj ten licznik do values_freq (powtorki nie wplywaja na to i tak)
        values_freq.append(values.count(value))
    if (3 in values_freq) and (2 in values_freq):               #tj. jesli jakas wartosc jest 3 razy i jakas inna jest 2 razy
        print("Full house! Zyskujesz {} punktow".format(score))
        player.new_score(score)
