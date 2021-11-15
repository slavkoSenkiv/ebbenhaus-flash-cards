class BankDeck:
    def __init__(self):
        self.deck = []

    def add_word(self, word):
        self.deck.append(word)

    def print_deck(self):
        print(self.deck)


deck_eg = BankDeck()
deck_eg.add_word('lol')

