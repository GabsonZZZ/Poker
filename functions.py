from typing import List

def fold(player: Player, current_deck: List[Card]) -> None:            #gracz passuje
    current_deck.append(player.cards[-1])                              #karta wraca do decku a potem jest zabierana graczowi (irl jest na odwrot)
    del player.cards[-1]
    current_deck.append(player.cards[-2])
    del player.cards[-2]
    deck.deck_update(current_deck.cards)


