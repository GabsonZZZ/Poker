#ifndef HAND_H_
#define HAND_H_

#include "Card.h"
#include <string>
#include <vector>

enum HandType {
	HT_NO_HAND,
	HT_HIGH_CARD,
	HT_PAIR,
	HT_TWO_PAIR,
	HT_STRAIGHT,
	HT_THREE_OF_A_KIND,
	HT_FLUSH,
	HT_FULL_HOUSE,
	HT_FOUR_OF_A_KIND,
	HT_STRAIGHT_FLUSH
};
const unsigned int MAX_CARDS_IN_HAND = 7;

typedef struct _HandValue {
	HandType type;
	const Card *primaryCard;
	const Card *secondaryCard;
} HandValue;

class Hand{
public:
  	size_t GetCardCount() const { return m_hand.size(); }
	
	const HandValue& GetBestHandValue() const { return m_best_hand; }
	std::string GetHandTextualDescription() const;
	std::string ToString() const;
private:
};

int hand_compare(const Hand* hand1, const Hand* hand2);
std::ostream& operator<<(std::ostream& os, const Hand& hand);
}
