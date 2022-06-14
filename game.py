def stack_creation(self):
   values = {"A": 14, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
   suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
   suits_values = {"Spades": "\u2660", "Hearts": "\u2665", "Clubs": "\u2663", "Diamonds": "\u2666"}
   self.deck = []
   for suit in suits:  # Pętla dla każdego koloru
      for card in self.symbols:  # Pętla dla każdej karty w danym kolorze
         self.deck.append(
            Card(suits_values[suit], card, values[card]))  # Dodanie karty o danych wartościach do stosu
   random.shuffle(self.deck)  # Przetasowanie stosu kart
   return self.deck
