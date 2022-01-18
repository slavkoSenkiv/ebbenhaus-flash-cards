import datetime
import time
import pyinputplus
import gspread

# <editor-fold desc="access db">
google_client = gspread.oauth()
gs = google_client.open('words collection')
# </editor-fold>


class BankDeck:
    def __init__(self, deck_name='bank deck'):
        self.deck_name = deck_name
        self.deck_sheet = gs.worksheet(deck_name)
        self.deck = self.deck_sheet.get_all_records()

    def update_deck(self):
        self.deck = self.deck_sheet.get_all_records()

    def clear_deck(self):
        self.deck_sheet.clear()
        self.deck_sheet.update('A1:D1', [['time', 'eng word', 'ua word', 'use score']])
        self.update_deck()
        print(self.deck_name, 'was cleared')

    def get_deck(self):
        self.update_deck()
        return self.deck

    def get_all_eng_words(self):
        self.update_deck()
        words_list = []
        for note in self.deck:
            words_list.append(note['eng word'])
        return words_list

    def add_new_word(self, word_note):
        word_note_list = word_note.split(' ')
        if word_note_list[0] not in self.get_all_eng_words():
            time_stamp = datetime.datetime.today().strftime('%d.%m.%y %H:%M:%S')
            next_free_row = len(self.deck_sheet.get_all_values()) + 1
            self.deck_sheet.update(f'A{next_free_row}:D{next_free_row}', [[time_stamp, word_note_list[0], word_note_list[1], 1]])
            print(word_note_list[0], 'goes into the', self.deck_name)
            self.update_deck()
        else:
            print(f'{word_note_list[0]} already in the {self.deck_name}')

    def print_words(self):
        self.update_deck()
        print(self.deck_name, end=': ')
        if len(self.get_all_eng_words()) == 0:
            print(f'is empty')
        else:
            lis = self.get_all_eng_words()
            for value in lis[:-1]:
                print(value, end=' ')
            print(lis[-1])


class WorkingDeck(BankDeck):
    def __init__(self):
        super().__init__(deck_name='working deck')
        self.bank_deck = BankDeck()
        self.learned_deck = {}

    """def move_words_to_bank_deck(self):
        print(self.deck)
        print(self.bank_deck)
        for key in self.deck.keys():
            self.bank_deck.deck[datetime.datetime.now()] = self.deck[key]
        self.deck = {}
        words_collection_wb.save(wb_name) # here we saving the sheet but we have not made any changes to it,
        # meanwhile we should, like move words in wb from 1 sheet to another, and only then save it
        print(f'we moved words from {self.deck_name} to bank_deck')
        print(self.deck)
        print(self.bank_deck)

    def rotation(self):
        while len(self.deck) > 0:
            for key in list(self.deck.keys()):
                remember = 'yes'  # pyinputplus.inputMenu(['yes', 'no'], f'know {self.deck[key]} ?\n', numbered=True)
                if remember == 'yes':
                    self.learned_deck[datetime.datetime.now()] = self.deck[key]
                    print(f'you have learned {self.deck[key]} so it goes out of this rotation')

                    del self.deck[key]
                if remember == 'no':
                    print(f'{self.deck[key]} goes in the end of the {self.deck_name}')
        print(f'you have repeated all words from {self.deck_name}')
        leave_words = pyinputplus.inputMenu(['leave', 'move'], f'leave words in {self.deck_name} or move to bank_deck?\n', numbered=True)
        if leave_words == 'leave':
            pass
            print('as u wish')
        if leave_words == 'move':
            self.move_words_to_bank_deck()

    def pick_word_from_bank_deck(self):
        oldest_word_time = datetime.datetime.now()
        for word_time_stamp_key in self.bank_deck.deck:
            if word_time_stamp_key is not None:
                if oldest_word_time >= word_time_stamp_key:
                    oldest_word_time = word_time_stamp_key
        print('oldest_word_time', oldest_word_time)
        for k, v in self.bank_deck.deck.items():
            print(k, v)

        # know_it = 'don*t know'
        know_it = pyinputplus.inputMenu(['know', 'don*t know'], f'know {self.bank_deck.deck[oldest_word_time]}: \n', numbered=True)
        if know_it == 'know':
            self.bank_deck.print_words()
            self.print_words()
            print(f'ah, u know "{self.bank_deck.deck[oldest_word_time]}"')
            self.bank_deck.deck[datetime.datetime.now()] = self.bank_deck.deck[oldest_word_time]
            del self.bank_deck.deck[oldest_word_time]
            self.bank_deck.print_words()
            self.print_words()

        else:
            # <editor-fold desc="sheet adjustment">
            bank_deck_sheet = words_collection_wb[self.bank_deck.deck_name]
            working_deck_sheet = words_collection_wb[self.deck_name]
            for row in range(2, bank_deck_sheet.max_row):
                if bank_deck_sheet.cell(row=row, column=2).value is not None:
                    if bank_deck_sheet.cell(row=row, column=2).value == self.bank_deck.deck[oldest_word_time]:
                        working_deck_sheet.cell(row=working_deck_sheet.max_row + 1, column=1).value = datetime.datetime.now()
                        working_deck_sheet.cell(row=working_deck_sheet.max_row, column=2).value = self.bank_deck.deck[oldest_word_time]
                        bank_deck_sheet.delete_rows(row, 1)
                        words_collection_wb.save(wb_name)
            # </editor-fold>

            # <editor-fold desc="deck dict adjustment">
            super().__init__(deck_name=self.deck_name)
            print(f'{self.bank_deck.deck[oldest_word_time]} ==> moved from {self.bank_deck.deck_name} ==> {self.deck_name}')
            del self.bank_deck.deck[oldest_word_time]
            super().__init__(deck_name=self.bank_deck.deck_name)

            # </editor-fold>"""
