# import math
# import requests

# r = requests.get("https://google.com")
# print(r.status_code)
# a = 5 + 7
# print(a)
# imie = "wiwo"

# print("siemka ", imie)


# cards = "6C JC AC 9C TC".split()


# def card_ranks(hand):
#     "zwraca listę ranksów w kolejności od najwyszej dla danej hand"
#     ranks = [r for r, s in hand]
#     for r in ranks:
#         if r == "T":
#             ranks[ranks.index(r)] = int(10)
#         elif r == "J":
#             ranks[ranks.index(r)] = int(11)
#         elif ranks[ranks.index(r)] == "Q":
#             ranks[ranks.index(r)] = int(12)
#         elif r == "K":
#             ranks[ranks.index(r)] = int(13)
#         elif r == "A":
#             ranks[ranks.index(r)] = int(14)
#         else:
#             ranks[ranks.index(r)] = int(r)

#     ranks.sort(reverse=True)
#     return ranks


# print(card_ranks(["AC", "3D", "4S", "KH"]))

# print("ehj")


# print("--23456789TJQKA".index("T"))


# def straight(ranks):
#     "return true if the order ranks form a 5-card straight"
#     if len(ranks) != 5:
#         return False
#     else:
#         for i in range(1, len(ranks)):
#             if ranks[i - 1] - 1 != ranks[i]:
#                 return False
#     return True


# print(straight([6, 5, 4, 3, 2]))


# sf = "6C 7C 8C 9C TC".split()
# fk = "9C 9S 9D 9H 7D".split()
# fh = "TD TC TH 7C 7S".split()


# def flush(hand):
#     "return true if all the cards have the same suit"
#     if len(hand) != 5:
#         return False
#     else:
#         suits = [s for r, s in hand]
#         for i in range(1, len(suits)):
#             if suits[i - 1] != suits[i]:
#                 return False
#     return True


# def flush2(hand):
#     "return true if all the cards have the same suit"
#     suits = [s for r, s in hand]
#     return len(set(suits)) == 1


# print(flush2(sf))


# def card_ranks(hand):
#     "zwraca listę ranksów w kolejności od najwyszej dla danej hand w postaci int"
#     ranks = [r for r, s in hand]
#     for r in ranks:
#         if r == "T":
#             ranks[ranks.index(r)] = int(10)
#         elif r == "J":
#             ranks[ranks.index(r)] = int(11)
#         elif ranks[ranks.index(r)] == "Q":
#             ranks[ranks.index(r)] = int(12)
#         elif r == "K":
#             ranks[ranks.index(r)] = int(13)
#         elif r == "A":
#             ranks[ranks.index(r)] = int(14)
#         else:
#             ranks[ranks.index(r)] = int(r)

#     ranks.sort(reverse=True)
#     return ranks


# sf = "6C 7C 8C 9C TC".split()
# fk = "9C 9S 9D 9H 7D".split()
# fh = "TD TC TH 7C 7S".split()
# tp = "5S 5D 9H 9C 6S".split()
# fkranks = card_ranks(fk)
# tpranks = card_ranks(tp)


# def kind(n, ranks):
#     """returns the first rank that the hand has exactly n of.
#     reuturn None if there is no n-of-a-kind in the hand
#     For A and 4 sevens this function will return 7"""
#     for R in set(ranks):
#         if ranks.count(R) == n:
#             return R
#     return None


# assert kind(4, fkranks) == 9
# assert kind(3, fkranks) == None
# assert kind(2, fkranks) == None
# assert kind(1, fkranks) == 7


# sf = "6C 7C 8C 9C TC".split()
# fk = "9C 9S 9D 9H 7D".split()
# fh = "TD TC TH 7C 7S".split()
# tp = "5S 5D 9H 9C 6S".split()
# fkranks = card_ranks(fk)
# tpranks = card_ranks(tp)


# def two_pair(ranks):
#     """ if there is a two pair, this function
#                   returns their corresponding ranks as a
#                   tuple. For example, a hand with 2 twos
#                   and 2 fours would cause this function
#                   to return (4, 2)."""
#     set(ranks)
#     pairs = []
#     for R in set(ranks):
#         if ranks.count(R) == 2:
#             pairs.append(R)
#     if len(pairs) == 2:
#         pairs.sort(reverse=True)
#         return tuple(pairs)
#     return None


# assert two_pair(fkranks) == None
# assert two_pair(tpranks) == (9, 5)


# sf = "6C 7C 8C 9C TC".split()
# fk = "9C 9S 9D 9H 7D".split()
# fh = "TD TC TH 7C 7S".split()


# def card_ranks(hand):
#     "zwraca listę ranksów w kolejności od najwyszej dla danej hand w postaci int"
#     ranks = [r for r, s in hand]
#     for r in ranks:
#         if r == "T":
#             ranks[ranks.index(r)] = int(10)
#         elif r == "J":
#             ranks[ranks.index(r)] = int(11)
#         elif ranks[ranks.index(r)] == "Q":
#             ranks[ranks.index(r)] = int(12)
#         elif r == "K":
#             ranks[ranks.index(r)] = int(13)
#         elif r == "A":
#             ranks[ranks.index(r)] = int(14)
#         else:
#             ranks[ranks.index(r)] = int(r)

#     ranks.sort(reverse=True)
#     return ranks


# print(card_ranks(sf))


def double(x): return x*2


print(double(2))
