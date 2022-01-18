import classes_gs
import pprint
d1 = classes_gs.BankDeck()
d2 = classes_gs.WorkingDeck()

d1.print_words()
d1.add_new_word('brother1 brat1')
d1.print_words()
print('\n')

d2.print_words()
d2.add_new_word('brother2 brat2')
d2.print_words()
print('\n')