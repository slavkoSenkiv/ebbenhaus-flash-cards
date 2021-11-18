import datetime
import time
import pyinputplus


class BankDeck:
    def __init__(self):
        self.deck_name = 'bank deck'
        self.bank_deck = {}

    def get_deck(self):
        return self.bank_deck

    def add_new_word(self, word):
        time_stamp = datetime.datetime.now()
        self.bank_deck.setdefault(time_stamp, word)
        time.sleep(0.1)
        print(word, 'goes into', self.deck_name)

    def print_words(self):
        print(self.deck_name, end=' ')
        for k, v in self.bank_deck.items():
            print(self.bank_deck[k], end=' ')
        print()


class WorkingDeck(BankDeck):
    def __init__(self, bank_deck):
        self.working_deck = {}
        self.bank_deck = bank_deck
        self.deck_name = 'working deck'

    def pick_word_in_bank_deck(self):
        oldest_word_time = datetime.datetime.now()
        for word_time_stamp in self.bank_deck:
            if oldest_word_time > word_time_stamp:
                oldest_word_time = word_time_stamp

        oldest_dic_item = self.bank_deck[oldest_word_time]
        do_you_remember = 'get'  # pyinputplus.inputMenu(['next', 'get'], f'{oldest_dic_item}: \n', numbered=True)
        if do_you_remember == 'next':
            self.bank_deck[datetime.datetime.now()] = oldest_dic_item; del oldest_dic_item
        else:
            self.working_deck[len(self.working_deck)] = oldest_dic_item
            print(oldest_dic_item, '==> moved to working deck')
            del self.bank_deck[oldest_word_time]

    def move_working_deck_to_bank_deck(self):
        for key, value in self.working_deck.items():
            self.bank_deck[datetime.datetime.now()] = self.working_deck[key]
            # del self.working_deck[key]
        self.working_deck = {}


