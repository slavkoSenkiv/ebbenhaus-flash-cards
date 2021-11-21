from classes import BankDeck
from classes import WorkingDeck

bank_deck = BankDeck()
working_deck = WorkingDeck()
bank_deck.clear_deck()
working_deck.clear_deck()
bank_deck.print_words()
working_deck.print_words()

bank_deck.add_new_word('father')
bank_deck.add_new_word('mother')
bank_deck.add_new_word('sister')
bank_deck.add_new_word('brother')
print()
bank_deck.print_words()
working_deck.print_words()
print()
working_deck.add_new_word('uncle')
working_deck.add_new_word('aunt')
print()
bank_deck.print_words()
working_deck.print_words()
print()
working_deck.pick_word_from_bank_deck()
print()
bank_deck.print_words()
working_deck.print_words()
