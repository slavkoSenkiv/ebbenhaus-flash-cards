lst = [{'time': '2022-01-23 22:24:49.989745', 'eng': 'sister', 'ua': 'sestra', '#': 2},
       {'time': '2022-01-23 22:24:50.989745', 'eng': 'brother', 'ua': 'brat', '#': 2}]

lst2 = []
for i in lst:
    lst2.append(i['eng'])

print(lst2)


