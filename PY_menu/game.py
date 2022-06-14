import random
import os




class Player:
    def __init__(self,cards,nick):
        self.nick = nick
        self.cards = cards      #Aktualne posiadane przez gracza karty
        self.bet = 0
                
    def add_card(self, card):
        self.cards.append(card)

class Card:
    def __init__(self, suit, symbol, value):
        self.suit = suit #Kolor
        self.symbol = symbol #Symbol karty
        self.value = value #Wartość karty
        
class Game:
    def __init__(self, players_list, number_of_decks=1):
        self.deck = []  # Stos kart
        self.dealer = Player([],'dealer')         #krupier jako gracz
        self.number_of_players = len(players_list)  # Liczba graczy
        self.players_list = players_list  # Lista graczy
        self.number_of_decks = number_of_decks  # Liczba użytych talii
        self.flop = []
        self.symbols = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

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
    



    def play_again(self):
            pass
        
        
    def print_table(self,show_dealer_card : bool) -> None:
        player_size = 20
        dealer_size = 14

        player_cards = self.players_list[0].cards
        dealer_cards = self.dealer.cards

        player_n_chars = len(player_cards)
        dealer_n_chars = len(dealer_cards)

        init_space = int((player_size - dealer_size) / 2) + 2

        self.clear()

        player_hand_chars = ""
        player_hand_chars += "╱" + int((player_size - 2 * player_n_chars) / 2) * " "
        flop_chars = ""
        flop_chars += " "
        for card in player_cards:
            player_hand_chars = player_hand_chars + card.symbol + card.suit +  " "
        player_hand_chars += (player_size - len(player_hand_chars) + 2) * " " + "╲"
        for card in self.flop:
           flop_chars = flop_chars + card.symbol + card.suit + " "
        flop_chars += (16 - (len(self.flop) + 2*len(self.flop))) * " " + "╲"

        dealer_hand_chars = " "
        dealer_hand_chars += "╱" + int((dealer_size - 2 * dealer_n_chars) / 2) * " "
        if show_dealer_card == True:
            for card in dealer_cards:
                dealer_hand_chars = dealer_hand_chars + card.symbol + card.suit + " "
        else:
            dealer_hand_chars = dealer_hand_chars + "[?] [?]"
        dealer_hand_chars += (dealer_size - len(dealer_hand_chars) + 1) * " " + "╲"

        print(init_space * " " + (dealer_size - 1) * "_")
        print("   " + dealer_hand_chars)
        print("   ╱               ╲    Bet: {" + str(2*self.players_list[0].bet) + "}\n  ╱" + flop_chars + "\n ╱                   ╲   ")
        print(player_hand_chars)
        print((player_size + 3) * chr(8254))
        
    def royal_flush(self, cards: [Card]):
                score = 1000
                cards.sort(key=lambda x: x.value)
                card1 = cards[0]
                if len(cards) != 5:
                    return False, 0;
                if card1.value != 10:
                    return False, 0;
                for card in cards:
                    if not (card.value == 10 or card.value == 11 or card.value == 12 or card.value == 13 or card.value == 14):
                        return False, 0;
                print("Royal Flush! Otrzymujesz {} punktów.".format(score))
                return True, score;
        
        
    def high_card(self, cards: [Card]):
                score = 1
                card1 = cards[0]
                if len(cards) != 5:
                    return False, 0;
                score = max([card.value for card in cards])
                print("High Card! Otrzymujesz {} punktów.".format(score))     #do zmiany po ustaleniu wartości score
                return True, score;
     

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
                   #do zmiany po ustaleniu wartości score
                
                
                
     def straight(self, cards: [Card]):
        score = 500
        if len(cards) != 5:
            return False, 0;
        cards.sort(key=lambda x: x.value)
        i = cards[0].value
        found = cards[0].value == i and cards[1].value == i+1 and cards[2].value == i+2 and cards[3].value == i+3 and cards[4].value == i+4
        if found == False:
            if cards[4].value == 14:
                i = 1
                found = cards[0].value == i+1 and cards[1].value == i+2 and cards[2].value == i+3 and cards[3].value == i+4
        if found:
            print("Straight! Otrzymujesz {} punktów.".format(score))
            return True, score;
        else:
            return False, 0;
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
  
 def points(self):
        cards = self.choose_cards()
        straight_found, straight_points = self.straight(cards)
        flush_found, flush_points = self.flush(cards)
        if straight_found and flush_found:
            royal_found, royal_points = self.royal_flush(cards)
            if royal_found:
                return royal_points
            else:
                return 900
        elif straight_found:
            return straight_points
        elif flush_found:
            return flush_points
        pairs_found, pairs_points = self.pair_or_three_of_a_kind(cards, self.symbols)
        if pairs_found:
            return pairs_points
        high_found, high_points = self.high_card(cards)
        return high_points
