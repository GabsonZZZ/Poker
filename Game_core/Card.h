#ifndef CARD_H_
#define CARD_H_

#include <string>

enum SUIT {
    CLUBS = 0,
    DIAMONDS = 1,
    HEARTS = 2,
    SPADES = 3
};



enum FACE_CARDS {
    JACK = 11,
    QUEEN = 12,
    KING = 13,
    ACE = 14
};

const int NUM_SUITS = 4;
const int LOWEST_SUIT_VALUE = CLUBS; 
const int HIGHEST_SUIT_VALUE = SPADES;

const int LOWEST_CARD_VALUE = 2;
const int HIGHEST_CARD_VALUE = ACE;

class Card {
	
	public:
  
		Card(const int value, const int suit);
		const int GetSuit() const { return suit_; }
		const int GetValue() const { return value_; }
		const bool IsSuit(const int suit) const { return (suit == suit_); }
		const bool IsValue(const int value) const { return (value == value_); }

		std::string ToString(bool compressed = false) const;
		std::string ToShortString() const;
		std::string ToLongString() const;

  private:

    int value_;
		int suit_;
};

std::ostream& operator<<(std::ostream& os, const Card& card);
bool operator==(const Card& c1, const Card& c2);

std::string CardValueToString(const int value, bool expandFaceName = false);
std::string CardSuitToString(const int suit);

}

#endif