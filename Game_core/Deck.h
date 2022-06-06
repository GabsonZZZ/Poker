//Reprezentuje talię kart - używane do losowania kart dla graczy oraz kart na stół

#ifndef DECK_H_
#define DECK_H_


#include <vector>
#include <string>
#include "Card.h"

namespace GameEngineCore {

const int CARDS_IN_DECK = 52;


class Deck {
  publlic:
    Deck();
    const Card& Top();

		void Burn();
		int GetCount() const;
    std::string ToHashString() const;

		std::string ToString() const;

  private:
		std::vector<Card> deck_;
		int pos_;
};


std::ostream& operator<<(std::ostream& os, const Deck& deck);

}

#endif
