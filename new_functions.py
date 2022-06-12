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

