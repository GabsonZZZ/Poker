
#include <vector>
#include <string>

class Deck {
  publlic:
    Deck();
    const Card& Top();

		void Burn();
		int GetCount() const;
  private:
		std::vector<Card> deck_;
		int pos_;
};


std::ostream& operator<<(std::ostream& os, const Deck& deck);

