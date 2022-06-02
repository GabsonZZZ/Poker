#include <assert.h>
#include <algorithm>
#include "Deck.h"
#include "CommonFunctions.h"

using namespace std;

namespace GameEngineCore {

Deck::Deck() :
	m_deck(),
	m_pos(CARDS_IN_DECK)
{
	m_deck.reserve(CARDS_IN_DECK);

	for (int value = LOWEST_CARD_VALUE; value <= HIGHEST_CARD_VALUE; value++) {
		m_deck.push_back(Card(value, HEARTS));
		m_deck.push_back(Card(value, CLUBS));
		m_deck.push_back(Card(value, DIAMONDS));
		m_deck.push_back(Card(value, SPADES));
	}
		
	random_shuffle(m_deck.begin(), m_deck.end());
}

	
string Deck::ToHashString() const {
	string card_list;
	card_list.reserve((CARDS_IN_DECK * 2) + 1);
	
	for (const Card& card : m_deck)
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
