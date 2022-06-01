#include <assert.h>
#include <algorithm>
#include "Deck.h"
#include "CommonFunctions.h"

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
