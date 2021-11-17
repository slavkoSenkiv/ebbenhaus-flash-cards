import datetime
import time
import pyinputplus


class BankDeck:
    def __init__(self):
        self.bank_deck = {}

    def get_bank_deck(self):
        return self.bank_deck

    def add_new_word(self, word):
        time_stamp = datetime.datetime.now()
        self.bank_deck.setdefault(time_stamp, word)
        time.sleep(0.1)

    def print_bank_deck_words(self):
        print('bank deck: ', end=' ')
        for k, v in self.bank_deck.items():
            print(self.bank_deck[k], end=' ')
        print('\n')


class WorkingDeck:
    def __init__(self, bank_deck):
        self.working_deck = {}
        self.bank_deck = bank_deck

    def get_working_deck(self):
        return self.working_deck

    def add_new_word(self, word):
        time_stamp = datetime.datetime.now()
        self.working_deck.setdefault(time_stamp, word)

    def print_working_deck_words(self):
        print('working deck: ', end=' ')
        for key, value in self.working_deck.items():
            print(self.working_deck[key], end=' ')
        print('\n')

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




