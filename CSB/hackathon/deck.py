import random


class Card:
    def __init__(self):
        self.value = ""
        self.suit = ""

    def __str__(self):
        v = self.value
        s = self.suit
        return f"{v} of {s}"


class Deck:
    def __init__(self):
        self.cards = []

        suits = ["hearts", "diamonds", "clubs", "spades"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for s in suits:
            for v in values:
                self.cards.append(f"{v} of {s}")

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_a_card(self):
        return self.cards.pop(0) if self.cards else None

    def sort(self):
        suits = {"hearts": 0, "diamonds": 1, "clubs": 2, "spades": 3}
        values = {
            "2": 0,
            "3": 1,
            "4": 2,
            "5": 3,
            "6": 4,
            "7": 5,
            "8": 6,
            "9": 7,
            "10": 8,
            "J": 9,
            "Q": 10,
            "K": 11,
            "A": 12,
        }

        def card_key(card):
            v, _, s = card.partition(" of ")
            return (suits[s], values[v])

        self.cards.sort(key=card_key)

    def __str__(self):
        cards = ", ".join(self.cards)
        return f"Deck of {len(self.cards)} cards: {cards}"
