import random
import math
# tak moge testować znak karty - jako drugi element listy stringowej
print("6C 7C 8C 9C JC".split()[0][1])


def test():
    "test cases for the function in poker program."
    sf = "6C 7C 8C 9C TC".split()  # straight flush
    fk = "9C 9S 9D 9H 7D".split()  # four of a kind
    fh = "TD TC TH 7C 7S".split()  # full house
    tp = "5S 5D 9H 9C 6S".split()  # two pairs
    s1 = "AS 2S 3S 4S 5C".split()  # A-5 straight
    s2 = "2C 3C 4C 5S 6S".split()  # 2-6 straight
    ah = "AS 2S 3S 4S 6C".split()  # A high
    sh = "2S 3S 4S 6C 7D".split()  # 7 high
    assert poker([s1, s2, ah, sh]) == s2
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9, 5)
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([fk] + 99 * [fh]) == fk
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return "tests pass"


def straight(ranks):
    "return true if the order ranks form a 5-card straight"
    if len(ranks) != 5:
        return False
    else:
        for i in range(1, len(ranks)):
            if ranks[i - 1] - 1 != ranks[i]:
                return False
    return True


def flush(hand):
    "return true if all the cards have the same suit"
    if len(hand) != 5:
        return False
    else:
        suits = [s for r, s in hand]
        for i in range(1, len(suits)):
            if suits[i - 1] != suits[i]:
                return False
    return True


def kind(n, ranks):
    """returns the first rank that the hand has exactly n of.
    reuturn None if there is no n-of-a-kind in the hand
    For A and 4 sevens this function will return 7"""
    for R in set(ranks):
        if ranks.count(R) == n:
            return R
    return None


def two_pair(ranks):
    """ if there is a two pair, this function
                  returns their corresponding ranks as a
                  tuple. For example, a hand with 2 twos
                  and 2 fours would cause this function
                  to return (4, 2)."""
    pairs = []
    for R in set(ranks):
        if ranks.count(R) == 2:
            pairs.append(R)
    if len(pairs) == 2:
        pairs.sort(reverse=True)
        return tuple(pairs)
    return None


def card_ranks2(hand):
    "zwraca listę ranksów w kolejności od najwyszej dla danej hand w postaci int"
    ranks = [r for r, s in hand]
    for r in ranks:
        if r == "T":
            ranks[ranks.index(r)] = int(10)
        elif r == "J":
            ranks[ranks.index(r)] = int(11)
        elif ranks[ranks.index(r)] == "Q":
            ranks[ranks.index(r)] = int(12)
        elif r == "K":
            ranks[ranks.index(r)] = int(13)
        elif r == "A":
            ranks[ranks.index(r)] = int(14)
        else:
            ranks[ranks.index(r)] = int(r)

    ranks.sort(reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        return [5, 4, 3, 2, 1]
    else:
        return ranks


def card_ranks(hand):
    "return a list of the ranks, sorted with higher first"
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks


def hand_rank(hand):
    "return a value indication the ranking of the hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):  # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):  # four of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):  # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):        # flush
        return (5, hand)
    elif straight(ranks):  # straigh
        return (4, max(ranks))
    elif kind(3, ranks):  # three of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):  # two pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):  # one pair
        return (1, kind(2, ranks), ranks)
    else:  # high card - nothing
        return (0, ranks)


def poker(hands):
    "return the best hand: poker([hand1,hand2,...]) => hand"
    # sprawdza jaki hand jest maxem
    # zdejmuje go z listy handów
    # sprawdza maxa na pozostałych
    # porównuje
    # powysze w pętli
    to_return = []

    max_hand = max(hands, key=hand_rank)
    to_return.append(max_hand)
    rest_hands = hands.remove(max_hand)

    # return max(hands, key=hand_rank)

    return to_return[0]


def allmax(iterable, key=None):
    "return the list of all the items quatl to the max of the iterable"
    result = []
    maxval = None
    # ????


def deal(numhands, n=5):
    """return a list of hands for example [2C, 3C, 4C, 5S, 6S]
    count how many decks you need (one deck = 54 cards)
    shuffle the cards in all decks
    return hands
    """
    how_many_decks = math.ceil((numhands * n)/52)
    # clubs = ["2C", "3C", "4C", "5C", "6C", "7C",
    #          "8C", "9C", "TC", "JC", "QC", "KC", "AC"]
    # spades = ["2S", "3S", "4S", "5S", "6S", "7S",
    #           "8S", "9S", "TS", "JS", "QS", "KS", "AS"]
    # diamonds = ["2D", "3D", "4D", "5D", "6D", "7D",
    #             "8D", "9D", "TD", "JD", "QD", "KD", "AD"]
    # hearts = ["2H", "3H", "4H", "5H", "6H", "7H",
    #           "8H", "9H", "TH", "JH", "QH", "KH", "AH"]

    # playing_deck = how_many_decks * (clubs + spades + diamonds + hearts)
    playing_deck2 = how_many_decks * \
        [r+s for r in '23456789TJQKA' for s in 'CSDH']

    # print("nasz deck: ", playing_deck2)
    # print("ma tyle kart: ", len(playing_deck2))

    random.shuffle(playing_deck2)
    # print("deck po tasowaniu: ", playing_deck2)

    # hands = []

    hands = [playing_deck2[n*i: n*(i+1)] for i in range(numhands)]
    # print("handsy")
    # print(hands)
    return hands


def hand_percentages(n=700*1000):
    "sample n random hands and print a table of percentages for each type of hand"
    counts = [0]*9  # licznik wystapien danego rodzaju - jest 9 układów
    for i in range(int(n/10)):  # bedziemy generowac po 10 handsow w jednym tasowaniu
        for hand in deal(10):  # dealujemy 10 ukladow i dla kazdego robimy:
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1

    for i in reversed(range(9)):
        print(i, ": ", 100*counts[i]/n)


def hand_percentages2(n=700*1000):
    counter = [0] * 9
    hand_names = ["Straight flush", "four of a kind", "full house", "flush",
                  "straight", "3 of a kind", "two pair", "one pair", "high card"]
    hand_names.reverse()
    for i in range(int(n/10)):  # bo dealuje po 10 handsów na raz:
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counter[ranking] += 1

    for uklad in reversed(range(len(counter))):
        #print(uklad, ": ", 100*counter[uklad]/n)
        print(hand_names[uklad], " :", 100.*counter[uklad]/n)
# print("winner: ", poker(deal(3)))


print(test())
hand_percentages2()
