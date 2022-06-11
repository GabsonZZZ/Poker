from inspect import stack
import random
import os
from colorama import Fore


class Game:
    def __init__(self, players_list, number_of_decks=1):
        self.deck = []  # Stos kart
        self.dealer = Player([],'dealer',0)         #Dealer jako gracz
        self.number_of_players = len(players_list)  # Liczba graczy
        self.players_list = players_list  # Lista graczy
        self.number_of_decks = number_of_decks  # Liczba użytych talii
        self.stack_creation()
        self.flop = []

    def stack_creation(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        suits_values = {"Spades": "\u2660", "Hearts": "\u2665", "Clubs": "\u2663", "Diamonds": "\u2666"}
        symbols = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        values = {"A": 14, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12,
                  "K": 13}

        self.deck = []
        for _ in range(self.number_of_decks):
            for suit in suits:  # Pętla dla każdego koloru
                for card in symbols:  # Pętla dla każdej karty w danym kolorze

                    self.deck.append(
                        Card(suits_values[suit], card, values[card]))  # Dodanie karty o danych wartościach do stosu
        random.shuffle(self.deck)  # Przetasowanie stosu kart
        return self.deck

    def deal_cards(self):
        self.dealer.cards = []                        #Czyszczenie kart dealera przed każdym rozdaniem
        for i in range(len(self.players_list)):       #Pętla czyszcząca karty dla każdego gracza
            self.players_list[i].cards = []
            self.players_list[i].bet = 0
            self.players_list[i].passed = False
        for _ in range(2):                            #Rozdanie 2 kart dealerowi i dla każdego gracza
            for player in range(len(self.players_list)):
                player_card = self.deck.pop()
                self.players_list[i].add_card(player_card)
            dealer_card = self.deck.pop()
            self.dealer.add_card(dealer_card)   
        print(self.players_list[0])

    def play_again(self):
        pass

    def clear(self):
        os.system('cls')

    def print_table(self,show_dealer_card : bool) -> None:
        #interfejs da radę pokazać 7 kart dla krupiera i góra 10 kart gracza(po modyfikacji możliwe jest 14 i 20 odpowiednio), chyba wystarczy
        player_size = 20
        dealer_size = 14

        player_cards = self.players_list[0].cards  # jedyny gracz istniejący w trybie jednoosobowym, najprawdopoboniej do zmiany
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

        print(Fore.GREEN + "  Wins: {:2d}".format(5) + Fore.RED + "   Losses: {:2d}".format(3) + Fore.WHITE)
        print(init_space * " " + (dealer_size - 1) * "_")
        print("   " + dealer_hand_chars)
        print("   ╱               ╲    Bet: {" + str(2*self.players_list[0].bet) + "}\n  ╱" + flop_chars + "\n ╱                   ╲   ".format(14, self.players_list[0].total()))
        print(player_hand_chars)
        print((player_size + 3) * chr(8254))


  #  def blackjack(self):
  #      if total(player_hand) == 21: #Sprawdza czy wartość na ręce jest równa
  #          print_results(dealer_hand, player_hand)
  #          print("You win !\n")
  #          play_again()
  #      elif total(dealer_hand) == 21:
  #          print_results(dealer_hand, player_hand)
  #          print("You lose\n")
  #         play_again()

    def evaluate(self):
    self.player_hand_chars 

class Card:
    def __init__(self, suit, symbol, value):    
        self.suit = suit #Kolor 
        self.symbol = symbol #Symbol karty
        self.value = value #Wartość karty


class Player:
    def __init__(self,cards,nick,nr_wins):
        self.nick = nick 
        self.cards = cards #Aktualne posiadane przez gracza karty
        self.nr_wins = nr_wins
        self.bet = 0

    def add_card(self,card):
        self.cards.append(card)

    def total(self):
        total = 0
        for card in self.cards:
            total+=card.value
            if card.symbol == "A" and total>21: 
                total-=10
        return total
