import openpyxl
import pprint

wb = openpyxl.open('10k_words.xlsx')
sheet = wb.active
dic = {}
for row in sheet.iter_rows(values_only=True):
    frequency = row[0]
    word = row[1]
    dic[frequency] = word

print(pprint.pformat(dic))
