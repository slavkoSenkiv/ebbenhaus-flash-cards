from classes import BankDeck
from classes import WorkingDeck

bank_deck = BankDeck()
working_deck = WorkingDeck(bank_deck.get_deck())

bank_deck.add_new_word('mother')
bank_deck.add_new_word('father')
bank_deck.add_new_word('sister')
bank_deck.add_new_word('brother')
bank_deck.print_words()
print()

for x in range(4):
    working_deck.pick_word_in_bank_deck()
    working_deck.print_words()
    bank_deck.print_words()
    print()

print(working_deck.get_deck())
print('working_deck to bank_deck')
working_deck.move_working_deck_to_bank_deck()
bank_deck.print_words()
working_deck.print_words()



