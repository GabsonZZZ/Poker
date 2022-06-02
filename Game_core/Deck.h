
#include <vector>
#include <string>

class Deck {

		std::vector<Card> deck_;
		int pos_;
};


std::ostream& operator<<(std::ostream& os, const Deck& deck);

