
#include <vector>
#include <string>

class Deck {
  publlic:
    Deck();
  private:
		std::vector<Card> deck_;
		int pos_;
};


std::ostream& operator<<(std::ostream& os, const Deck& deck);

