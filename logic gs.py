import classes_gs
import pprint
import datetime
import time


d1 = classes_gs.BankDeck()
d2 = classes_gs.WorkingDeck()
d3 = classes_gs.LearnedDeck()

# d1.rotate_and_offer_word(d2)
# d2.rotate_and_offer_word(d3)
# d3.rotate_and_offer_word(d3)
d2.print_dict_words()
d3.print_dict_words()

d3.move_deck_into_other(d2)

d2.print_dict_words()
d3.print_dict_words()
