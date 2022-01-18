import classes_gs
import pprint
d1 = classes_gs.BankDeck()
# d2 = classes_gs.WorkingDeck()

print(pprint.pformat(d1.deck))
d1.clear_deck()
print(pprint.pformat(d1.deck))
d1.add_new_word()