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
