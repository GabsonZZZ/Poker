###TO MA BYĆ METODA KLASY GAME   
class Game:  
  def choose_cards(self) -> [Card]:
        cards = []
        for card in self.players_list[0].cards:
            ans = input("Chcesz użyć karty {}? (W tym celu wpisz tak/nie)".format(card.symbol + card.suit))
            if ans == "tak":
                cards.append(card)
        for card in self.flop:
            ans = input("Chcesz użyć karty {}? (W tym celu wpisz tak/nie)".format(card.symbol + card.suit))
            if ans == "tak":
                if len(cards) < 5:
                    cards.append(card)
                else:
                    print("Wybrano już 5 kart!")
                    break
        return cards
