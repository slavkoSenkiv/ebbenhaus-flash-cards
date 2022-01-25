import classes_gs
import pprint
import datetime
import time


d1 = classes_gs.BankDeck()
d2 = classes_gs.WorkingDeck()
d3 = classes_gs.LearnedDeck()

d1.print_dict_words()
d2.print_dict_words()
d2.rotation_inside_working_deck()
d1.print_dict_words()
d2.print_dict_words()
