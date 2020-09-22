'''
author = Dusan Ptacek.
project 1
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

ramik = ' ' * 3 + ' = ' * 17
oddelovac = ' ' * 3 + ' . ' * 17
medzery = ' ' * 4

print(ramik)
print('|| Vitaj, mily pouzivatel! A teraz sa prihlas, prosim: ||')
print(ramik)

print()

uzivatel = input(medzery + 'Tvoje prihlasovacie meno bude: ')
heslo = input(medzery + 'Zadaj svoje heslo: ')

users_database = {'bob':  123, 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

print()

if uzivatel in users_database.keys():
    if str(users_database.get(uzivatel)) == heslo:
        print(medzery + 'Prihlasenie prebehlo uspesne.')
    else:
        print(medzery + 'Zadali ste nespravne heslo!')
else:
    print(medzery + 'Neexistujuci pouzivatel!')

print()
print(oddelovac)
print()

print(f'{medzery}Mozeme analyzovat 1 z 3 textov.')
vyber_textu = int(input(f'{medzery}Vyber si jeden z nich (zadaj cislo 1-3): '))
print()
while 1 > vyber_textu or vyber_textu > 3:
    vyber_textu = int(input(f'{medzery}Znova. Vyber si text (zadaj cislo 1-3): '))
    print(oddelovac)
print(oddelovac)

pocet_slov = {}
prve_velke = 0
prve_male = 0
vsetky_velke = 0
vsetky_male = 0
cisel = 0
freq_dlzok_slov = {}
tokenized_text = TEXTS[vyber_textu - 1].strip('.,!?;''').split()
sucet = 0

for slovo in tokenized_text:
    pocet_slov[slovo.lower()] = pocet_slov.get(slovo.lower(), 0) + 1

    if slovo[0].isupper() == True:
        prve_velke += 1
    elif slovo[0].islower() == True:
        prve_male += 1
    else:
        cisel += 1

    if slovo.isupper() == True:
        vsetky_velke += 1
    elif slovo.islower() == True:
        vsetky_male += 1

    if slovo.isdigit() == True:
        sucet += int(slovo)

    freq_dlzok_slov[len(slovo)] = freq_dlzok_slov.get(len(slovo), 0) + 1

print(f'{medzery}Pocet vsetkych slov v texte {vyber_textu} je: {len(tokenized_text)}')
print(f'{medzery}Pocet slov v texte {vyber_textu}, ktore zacinaju velkym pismenom: {prve_velke}')
print(f'{medzery}Pocet slov v texte {vyber_textu}, ktore zacinaju malym pismenom: {prve_male}')
print(f'{medzery}Pocet slov v texte {vyber_textu}, ktore su napisane iba velkymi pismenami: {vsetky_velke}')
print(f'{medzery}Pocet slov v texte {vyber_textu}, ktore su napisane iba malymi pismenami: {vsetky_male}')
print(f'{medzery}Pocet cisel v texte {vyber_textu} je: {cisel}')
print(oddelovac)

for dlzka_slova in range(min(freq_dlzok_slov), max(freq_dlzok_slov) + 1):
    kolko = freq_dlzok_slov.get(dlzka_slova, 0)
    if kolko > 0:
        print((medzery) * 2, dlzka_slova, '*' * kolko, kolko)

print(oddelovac)

print(f'{medzery}Ked zratame vsetky cisla v texte {vyber_textu}, dostaneme cislo {sucet}')
print(oddelovac)