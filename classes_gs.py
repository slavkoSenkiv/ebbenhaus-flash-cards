import datetime
import time
import pyinputplus
import gspread
import pprint


# <editor-fold desc="pre code">
google_client = gspread.oauth()
gs = google_client.open('words collection')

column_headers = ['time', 'eng', 'ua', '#']
time_key = column_headers[0]
eng_key = column_headers[1]
ua_key = column_headers[2]
score_key = column_headers[3]

deck_names = ['bank deck', 'working deck', 'learned deck']
bank_deck_name_key = deck_names[0]
working_deck_name_key = deck_names[1]
learned_deck_name_key = deck_names[2]


def get_str_time_now():
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S.%f')


def convert_str_time_to_date_time(str):
    return datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S.%f')
# </editor-fold>


class BankDeck:
    def __init__(self, deck_name=f'{bank_deck_name_key}'):
        self.deck_name = deck_name
        self.deck_sheet = gs.worksheet(deck_name)
        self.deck = self.deck_sheet.get_all_records()

    def move_deck_into_other(self, destination_deck_class, start_deck_class=None):
        start_deck_class = self if start_deck_class is None else start_deck_class
        for word_dict in start_deck_class.deck:
            destination_deck_class.deck.append(word_dict)
        start_deck_class.deck.clear()# clear_deck()
        start_deck_class.update_sheet_from_dict_deck()
        print(f'{start_deck_class.deck_name} ==> {destination_deck_class.deck_name}')

    def update_dict_deck_from_sheet(self):
        self.deck = self.deck_sheet.get_all_records()
        # print(f'{self.deck_name} sheet is updated')

    def update_sheet_from_dict_deck(self):
        update_list = [column_headers]
        for word_note in self.deck:
            update_list.extend([[word_note[time_key], word_note[eng_key], word_note[ua_key], word_note[score_key]]])
        self.deck_sheet.update('A1', update_list)

    def clear_deck(self):
        self.deck_sheet.clear()
        self.deck_sheet.update('A1', [column_headers])
        print(self.deck_name, 'was cleared')

    def clear_deck_dict(self):
        self.deck.clear()

    def get_deck(self):
        return self.deck

    def get_all_eng_words(self):
        deck_lst = self.get_deck()
        words_lst = []
        for word_dict in deck_lst:
            words_lst.append(word_dict[eng_key])
        return words_lst

    def print_dict_words(self):
        eng_words_lst = self.get_all_eng_words()
        print(self.deck_name, end=': ')
        if len(eng_words_lst) == 0:
            print(f'is empty')
        else:
            for value in eng_words_lst[:-1]:
                print(value, end=' ')
            print(eng_words_lst[-1])

    def print_deck_dicts(self):
        print(self.deck_name)
        print(pprint.pformat(self.deck))

    def add_new_word(self, word_note):
        word_note_list = word_note.split(' ')
        if word_note_list[0] not in self.get_all_eng_words():
            next_free_row = len(self.deck_sheet.get_all_values()) + 1
            self.deck_sheet.update(f'A{next_free_row}:D{next_free_row}', [[get_str_time_now(), word_note_list[0], word_note_list[1], 1]])
            print(word_note_list[0], 'goes into the', self.deck_name)
            self.update_dict_deck_from_sheet()
        else:
            print(f'{word_note_list[0]} already in the {self.deck_name}')

    def rotate_offer_move_word(self, destination_deck_class):
        while len(self.deck) > 0:

            eldest_time = datetime.datetime.now()
            for word_note in self.deck:
                if convert_str_time_to_date_time(word_note[time_key]) < eldest_time:
                    eldest_time = convert_str_time_to_date_time(word_note[time_key])

            for word_note in self.deck:
                if convert_str_time_to_date_time(word_note[time_key]) == eldest_time:
                    know = pyinputplus.inputMenu(['yes', 'no'], f'know {word_note[eng_key]} ?\n', numbered=True)

                    if know == 'yes':
                        word_note[time_key] = get_str_time_now()
                        print(f'{word_note[eng_key]} goes to the end of {self.deck_name}')

                    if know == 'no':
                        word_note[time_key] = get_str_time_now()
                        print(f'{word_note[eng_key]} goes into {destination_deck_class.deck_name}')
                        destination_deck_class.deck.append(word_note)
                        self.deck.remove(word_note)

        print(f'there are no words in {self.deck_name}')


class WorkingDeck(BankDeck):
    def __init__(self):
        super().__init__(f'{working_deck_name_key}')
        self.bank_deck = BankDeck()
        self.learned_deck = LearnedDeck()

    def rotation_inside_working_deck(self):
        while len(self.deck) > 0:
            for word_note in self.deck:
                know = "yes" # pyinputplus.inputMenu(['yes', 'no'], f'know {word_note[eng_key]} ?\n', numbered=True)

                if know == 'yes':
                    self.learned_deck.deck.append(word_note)
                    self.deck.remove(word_note)
                    print(f'you have learned "{word_note[eng_key]}" \n'
                          f'so it goes out of this rotation to {self.learned_deck.deck_name}')

                if know == 'no':
                    word_note[time_key] = get_str_time_now()
                    print(f'{word_note[eng_key]} goes in the end of the {self.deck_name}')

        print(f'you have repeated words from {working_deck_name_key}')
        where_to_put_repeated_words = f'{self.deck_name}' # pyinputplus.inputMenu([f'{self.deck_name}', f'{self.bank_deck.deck_name}'],
                                                            # f'Where to put words from {self.learned_deck.deck_name}?\n', numbered=True)

        # if where_to_put_repeated_words == f'{self.deck_name}':
        self.move_deck_into_other(self, self.learned_deck)

        # if where_to_put_repeated_words == f'{self.bank_deck.deck_name}':
        # self.move_deck_into_other(self.bank_deck, self.learned_deck)


class LearnedDeck(BankDeck):
    def __init__(self):
        super().__init__(f'{learned_deck_name_key}')

