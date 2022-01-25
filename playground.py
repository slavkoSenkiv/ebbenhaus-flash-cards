class CardsDeck:
    def __init__(self):
        self.deck = [{'#': 2, 'eng': 'sister', 'time': '2022-01-23 22:24:49.989745', 'ua': 'sestra'},
                     {'#': 2, 'eng': 'brother', 'time': '2022-01-23 22:24:50.989745', 'ua': 'brat'}]

    def get_all_eng_words(self):
        deck_lst = self.deck
        words_lst = []
        for word_dict in deck_lst:
            words_lst.append(word_dict[eng_key])
        return words_lst


column_headers = ['time', 'eng', 'ua', '#']
time_key = column_headers[0]
eng_key = column_headers[1]
ua_key = column_headers[2]
score_key = column_headers[3]

print(CardsDeck().get_all_eng_words())