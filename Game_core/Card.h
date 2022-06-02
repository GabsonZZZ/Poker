#ifndef CARD_H_
#define CARD_H_

enum SUIT {
    CLUBS = 0,
    DIAMONDS = 1,
    HEARTS = 2,
    SPADES = 3
};

#include <string>

enum FACE_CARDS {
    JACK = 0,
    QUEEN = 1,
    KING = 2,
    ACE = 3
};

const int NUM_SUITS = 4;
const int LOWEST_SUIT_VALUE = CLUBS; 
const int HIGHEST_SUIT_VALUE = SPADES;

const int LOWEST_CARD_VALUE = 2;
const int HIGHEST_CARD_VALUE = ACE;


#endif