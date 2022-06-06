#include <assert.h>
#include <algorithm>
#include "Deck.h"
#include "CommonFunctions.h"

using namespace std;

namespace GameEngineCor {

Deck::Deck() :
	deck_(),
	pos_(CARDS_IN_DECK)
{
	deck_.reserve(CARDS_IN_DECK);

	for (int value = LOWEST_CARD_VALUE; value <= HIGHEST_CARD_VALUE; value++) {
		deck_.push_back(Card(value, HEARTS));
		deck_.push_back(Card(value, CLUBS));
		deck_.push_back(Card(value, DIAMONDS));
		deck_.push_back(Card(value, SPADES));
	}
		
	random_shuffle(deck_.begin(), deck_.end());
}

const Card& Deck::Top() {
	assert(pos_ > 0);

	pos_--;
	return deck_[pos_];
}

void Deck::Burn() {
	assert(pos_ > 0);
	pos_--;
}

int Deck::GetCount() const {
	return pos_;
}	
	
string Deck::ToHashString() const {
	string card_list;
	card_list.reserve((CARDS_IN_DECK * 2) + 1);
	
	for (const Card& card : deck_)
		card_list += card.ToShortString();
	
	return card_list;
}
	
string Deck::ToString() const {
	string cardcount = PokerUtils::AutoToString(GetCount());
	string retval = "Deck of " + cardcount + " Cards";
	return retval;
}
	
ostream& operator<<(ostream& os, const Deck& dk) {
	os << dk.ToString();
	return os;
}
	
}
