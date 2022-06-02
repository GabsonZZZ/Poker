#include "Card.h"


Class::Class(const int value, const in suit) : value_(value), suit_(suit) {
	assert(suit_ == HEARTS || suit_ == CLUBS || suit_ == DIAMONDS || suit_ == SPADES);
	assert(value_ >= LOWEST_CARD_VALUE && value_ <= HIGHEST_CARD_VALUE);
}


string Card::ToString(const bool compressed) const {
	if (compressed)
		return ToShortString();
	else
		return ToLongString();
}
string Card::ToShortString() const {

	string retval;
	
	if (m_value < 11)
		retval = CardValueToString(m_value);
	else if (m_value == JACK)
		retval = "J";
	else if (m_value == QUEEN)
		retval = "Q";
	else if (m_value == KING)
		retval = "K";
	else if (m_value == ACE)
		retval = "A";

	switch (m_suit) {
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
string Card::ToLongString() const {
	return CardValueToString(m_value) + " of " + CardSuitToString(m_suit);
}
	
std::ostream& operator<<(std::ostream& os, const Card& card) {
	os << card.ToString();
	return os;
}
bool operator==(const Card& c1, const Card& c2) {
	return (c1.GetSuit() == c2.GetSuit() && c1.GetValue() == c2.GetValue());
}
string CardSuitToString(const int suit) {
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
