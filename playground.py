import openpyxl
wb_name = 'words collection.xlsx'
bank_deck_name = 'bank_deck'
working_deck_name = 'working_deck'
words_collection_wb = openpyxl.open(wb_name)


def clear_deck(self):
    for sheet in words_collection_wb.sheetnames:
        if sheet.startswith(bank_deck_name):
            del words_collection_wb[sheet]
    words_collection_wb.create_sheet(self.deck_name)
    words_collection_wb.save(wb_name)
    self.deck = {}