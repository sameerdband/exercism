"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

ACE_CARD_VALUE = 1
FACE_CARD_VALUE = 10

def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """

    if '1' < card <= '9' or card == '10':
        return int(card)
    if card in ['J', 'Q', 'K']:
        return FACE_CARD_VALUE
    if card == 'A':
        return ACE_CARD_VALUE
    raise ValueError("Invalid card. Card should be Ace, 2 - 10, or a face card")


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value > card_two_value:
        return card_one
    if card_two_value > card_one_value:
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value == 1:
        card_one_value = 11
    if card_two_value == 1 and card_one_value != 1 and card_one_value != 11:
        card_two_value = 11

    return 11 if card_one_value + card_two_value <= 10 else 1 


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """

    face_cards = ['J', 'Q', 'K', '10']
    has_ace = card_one == 'A' or card_two == 'A'
    has_face = card_one in face_cards or card_two in face_cards
    return has_ace and has_face


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    face_cards = ['J', 'Q', 'K', '10']
    return True if card_one == card_two else card_one in face_cards and card_two in face_cards


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    total = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= total <= 11
