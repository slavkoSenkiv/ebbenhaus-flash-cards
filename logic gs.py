import classes_gs
import pprint
import datetime
import time


def print_words():
    d1.print_dict_words()
    d2.print_dict_words()
    d3.print_dict_words()


def get_and_print_words():
    print(d1.get_all_eng_words())
    print(d2.get_all_eng_words())
    print(d3.get_all_eng_words())


def print_decks():
    print(d1.deck)
    print(d2.deck)
    print(d3.deck)


def update_decks():
    d1.update_dict_deck_from_sheet()
    d2.update_dict_deck_from_sheet()
    d3.update_dict_deck_from_sheet()


d1 = classes_gs.BankDeck()
d2 = classes_gs.WorkingDeck()
d3 = classes_gs.LearnedDeck()

print_words()
d2.rotation_inside_working_deck()
update_decks()
print_words()
