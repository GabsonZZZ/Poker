#### punktacja
### tutaj funkcja, w ktorej gracz wybiera karty do swojej kombinacji ###

def choose_cards(player: Player, current_flop: List[Card]) -> List[Card]: #zwraca liste kart potrzebna do funckji, które będą sprawdzały czy jest jakaś ta odpowiednia kombinacja
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


def flush(cards: List[Card], player: Player) -> None:   #połączenie royal i straight flusha w 1 funckję
    score_royal_flush = 10                              #do zmiany moze byc ta ilosc punktow
    score_straight_flush = 9
    card1 = cards[0]
    if len(cards) != 5:
        return None
    for card in cards:
        if card.suit != card1.suit:
            return None
    for card in cards:
        if not (card.value == 10 or card.value == 11 or card.value == 12 or card.value == 13 or card.value == 14) and (card != card1):
            print("Straight flush! Zyskujesz {} punktow".format(score_straight_flush))
            player.new_score(score_straight_flush)
            return None
    print("Royal flush! Zyskujesz {} punktow".format(score_royal_flush))
    player.new_score(score_royal_flush)

    
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

        
 def flush(cards: List[Card], player: Player) -> None:
    score = 6
    card1 = cards[0]
    if len(cards) != 5:                         #jak gracz wybrał za mało kart to naura już dalej nie sprawdzane
        return None
    for card in cards:
        if card.suit != card1.suit:             #karty mają miec ten sam suit, wiec jak jakas ma inny niz ta pierwsza to tez naura
            return None
    values = []
    for card in cards:                          #utworzenie listy, ktora przechowuje tylko wartosci kart
        values.append(card.value)
    values.sort()                               #posortowanie jej (od min do max)
    i = 0
    count = 0
    while i < len(values) - 2:                  #dopoki nie wyjdzie poza zakres listy
        if values[i + 1] - values[1] == 1:      #jesli roznica jest 1 to liczy ile jest takich roznic
            count += 1
        i += 1
    if count == 4:                              #wtedy chyba jest sekwencja, czyli zle
        return None
    print("Flush! Zyskujesz {} punktow".format(score))
    player.new_score(score)
       

 
###funkcja robiaca liste liczby wartosci
#napisana osobno, bo uzyta zostala chyba 2 razy w tych punktacjach, najwyzej tamte funkcje do edycji, zeby ja jakos wykorzystac
def values_only(cards: List[Card]) -> List[int]:
    values = []
    for card in cards:
        values.append(card.value)
    return values


###UWAGA ##################################
### MOGĄ BYĆ TUTAJ BŁĘDY, POLECAM SPRAWDZIĆ (NIE BYŁY TESTOWANE), BO MOŻLIWE, ŻE JAKIEŚ WARUNKI ZOSTAŁY POMINIĘTE, ALBO DZIAŁAJĄ NIE TAK JAK POWINNY, BO ŹLE ZROZUMIAŁAM ZASADY

