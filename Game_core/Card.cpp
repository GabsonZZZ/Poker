#include "Card.h"


Card::Card(const int value, const int suit) : value_(value), suit_(suit) {
	assert(suit_ == HEARTS || suit_ == CLUBS || suit_ == DIAMONDS || suit_ == SPADES);
	assert(value_ >= LOWEST_CARD_VALUE && value_ <= HIGHEST_CARD_VALUE);
}


std::string Card::ToString(const bool compressed) const {
	if (compressed)
		return ToShortString();
	else
		return ToLongString();
}
std::string Card::ToShortString() const {

	std::string retval;
	
	if (value_ < 11)
		retval = CardValueToString(value_);
	else if (value_ == JACK)
		retval = "J";
	else if (value_ == QUEEN)
		retval = "Q";
	else if (value_ == KING)
		retval = "K";
	else if (value_ == ACE)
		retval = "A";

	switch (suit_) {
		case (HEARTS):
			retval += "H";
			break;
		case (CLUBS):
			retval += "C";
			break;
		case (DIAMONDS):
			retval += "D";
			break;
		case (SPADES):
			retval += "S";
			break;
	}

	return retval;
}
std::string Card::ToLongString() const {
	return CardValueToString(value_) + " of " + CardSuitToString(suit_);
}
	
std::ostream& operator<<(std::ostream& os, const Card& card) {
	os << card.ToString();
	return os;
}

bool operator==(const Card& c1, const Card& c2) {
	return (c1.GetSuit() == c2.GetSuit() && c1.GetValue() == c2.GetValue());
}

std::string CardValueToString(const int value, bool expandFaceName) {

	if (expandFaceName) {
		
		switch (value) {
			case (JACK):
				return "Jack";
			case (QUEEN):
				return "Queen";
			case (KING):
				return "King";
			case (ACE):
				return "Ace";
			default:
				return PokerUtils::AutoToString(value);
		}
	} else
		return PokerUtils::AutoToString(value);
  }

std::string CardSuitToString(const int suit){
	switch (suit) {
		case (CLUBS):
			return "Clubs";
		case (SPADES):
			return "Spades";
		case (DIAMONDS):
			return "Diamonds";
		default:
			return "Hearts";
	}
  }
