class Game:
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


        def pair_or_three_of_a_kind(self, cards: [Card], symbols):
                score = 200
                if len(cards) != 5:
                    return False, 0;
                value_dict = dict([(x,0) for x in symbols])
                for die in cards:
                    value_dict[die.symbol] += 1
                set_dict = dict([(x, 0) for x in range(0, 6)])
                for set_size in value_dict.values():
                    set_dict[set_size] += 1
                if set_dict[2] == 1 and set_dict[3] != 1 and set_dict[4] != 1:
                    print("Pair! Otrzymujesz {} punktów.".format(score))
                    return True, score;                     #do zmiany po ustaleniu wartości score
                elif set_dict[3] == 1 and set_dict[4] != 1:
                    score = 400
                    print("Three of a kind! Otrzymujesz {} punktów.".format(score))
                    return True, score;
                elif set_dict[4] == 1:
                    score = 700
                    print("Four of a kind! Otrzymujesz {} punktów.".format(score))
                    return True, score;
                elif set_dict[2] == 1 and set_dict[3] == 1:
                    score = 600
                    print("Full house! Otrzymujesz {} punktów.".format(score))
                    return True, score;
                elif set_dict[2] == 2:
                    score = 300
                    print("Two pair! Otrzymujesz {} punktów.".format(score))
                    return True, score;
                else:
                    return False, 0;
