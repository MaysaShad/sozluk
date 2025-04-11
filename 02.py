dukan = {
    'alma': 8,
    'uzum': 12,
    'hurma': 18,
    'banan': 25,
    'nar': 15}

for i, j in dukan.items():
    print(i, '-', j,'Manat')
kassa = 0
while True:
    miwe = input('Name almak isleyaniz? ')
    if miwe == 'quit':
        break
    elif miwe in dukan:
        kg = int(input('Nace kg almak isleyarsiniz? '))
        pul = kg * dukan[miwe]
        kassa += pul
    elif miwe not in dukan:
        print(f'{miwe} Dukanda yok')
print(f'Siz {kassa} manat tolemeli')