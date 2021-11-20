from classes import BankDeck
from classes import WorkingDeck

bank_deck = BankDeck()
working_deck = WorkingDeck()
bank_deck.clear_deck()
working_deck.clear_deck()

bank_deck.add_new_word('father')
bank_deck.add_new_word('mother')
bank_deck.add_new_word('father')
bank_deck.add_new_word('sister')
bank_deck.add_new_word('brother')
bank_deck.add_new_word('sister')
print()
working_deck.pick_word_from_bank_deck()
print()
working_deck.pick_word_from_bank_deck()
print()
"""print('bank_deck', bank_deck.get_deck())
print('working_deck', working_deck.get_deck())
bank_deck.print_words()
working_deck.print_words()
print()
working_deck.rotation()
print()
bank_deck.print_words()
working_deck.print_words()
print()"""