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

	
std::ostream& operator<<(std::ostream& os, const Card& card) {
	os << card.ToString();
	return os;
}
