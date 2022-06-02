#ifndef CARD_H_
#define CARD_H_

enum SUIT {
    CLUBS = 0,
    DIAMONDS = 1,
    HEARTS = 2,
    SPADES = 3
};

#include <string>

enum FACE_CARDS {
    JACK = 0,
    QUEEN = 1,
    KING = 2,
    ACE = 3
};

const int NUM_SUITS = 4;
const int LOWEST_SUIT_VALUE = CLUBS; 
const int HIGHEST_SUIT_VALUE = SPADES;

const int LOWEST_CARD_VALUE = 2;
const int HIGHEST_CARD_VALUE = ACE;

class Card {
	
	public:
  
		Card(const int value, const int suit);
		const int GetSuit() const { return m_suit; }
		const int GetValue() const { return m_value; }
		const bool IsSuit(const int suit) const { return (suit == m_suit); }
		const bool IsValue(const int value) const { return (value == m_value); }

		std::string ToString(bool compressed = false) const;
		std::string ToShortString() const;
		std::string ToLongString() const;

  private:

    int value_;
		int suit_;


#endif