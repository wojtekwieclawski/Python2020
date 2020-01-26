import random


def create_deck():
    return [r+s for r in '23456789TJQKA' for s in 'CSDH']


def shuffle_teacher(deck):
    "not efficient way of swapping"
    n = len(deck)
    counter = 0
    swapped = [False] * n
    while not all(swapped):
        i = random.randrange(n)
        j = random.randrange(n)
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp
        swapped[i] = swapped[j] = True
        counter += 1
    print("I did that many rounds: ", counter)
    return deck


def shuffle_better(deck):
    "more efficient way of swapping"
    n = len(deck)
    counter = 0
    for i in range(n-1):
        temp = deck[i]
        j = random.randrange(i, n)
        deck[i] = deck[j]
        deck[j] = temp
        counter += 1
    print("I did that many rounds in better swapping alg: ", counter)
    return deck


deck = create_deck()
print("new deck:")
print(deck)
print("swapped bad way:")
deck = shuffle_teacher(deck)
print(deck)
print("swapped better way:")
deck = create_deck()
print("new deck:")
print(deck)
deck = shuffle_better(deck)
print(deck)
