import datetime
import time
import pyinputplus


class BankDeck:
    def __init__(self):
        self.bank_deck = {}

    def get_deck(self):
        return self.bank_deck

    def add_new_word(self, word):
        time_stamp = datetime.datetime.now()
        self.bank_deck.setdefault(time_stamp, word)
        time.sleep(0.1)

    def print_words(self):
        print('bank deck: ', end=' ')
        for k, v in self.bank_deck.items():
            print(self.bank_deck[k], end=' ')
        print('\n')


class WorkingDeck(BankDeck):
    def __init__(self, bank_deck):
        self.working_deck = {}
        self.bank_deck = bank_deck

    def pick_word_in_bank_deck(self):
        oldest_word_time = datetime.datetime.now()
        for word_time_stamp in self.bank_deck:
            if oldest_word_time > word_time_stamp:
                oldest_word_time = word_time_stamp

        oldest_dic_item = self.bank_deck[oldest_word_time]
        do_you_remember = pyinputplus.inputMenu(['next', 'get'], f'{oldest_dic_item}: \n', numbered=True)
        if do_you_remember == 'next':
            self.bank_deck[datetime.datetime.now()] = oldest_dic_item; del oldest_dic_item
        else:
            self.working_deck[len(self.working_deck)] = oldest_dic_item
            print(oldest_dic_item, '==> moved to working deck')
            del self.bank_deck[oldest_word_time]

    def move_working_deck_to_bank_deck(self):
        for key, value in self.working_deck.items():
            self.working_deck[datetime.datetime.now()] = self.working_deck[key]
            del self.working_deck[key]
        self.bank_deck.update(self.working_deck)


bank_deck = BankDeck()
working_deck = WorkingDeck(bank_deck.get_deck())  # bank_deck.get_bank_deck())

bank_deck.add_new_word('mother')
bank_deck.add_new_word('father')
bank_deck.add_new_word('sister')
bank_deck.add_new_word('brother')
bank_deck.print_words()

for x in range(4):
    working_deck.pick_word_in_bank_deck()
    working_deck.print_words()
    bank_deck.print_words()

print(working_deck.get_deck())
print('working_deck to bank_deck')
working_deck.move_working_deck_to_bank_deck()
bank_deck.print_words()


