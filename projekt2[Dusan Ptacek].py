# author: Dusan Ptacek
# project 2

import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chosen_num = []
user = ""
guesses = 0
num_bulls = 0

print('|| BULLS & COWS ||\n')
print('Vygeneroval som 4-ciferne cislo.')
print('Skus ho uhadnut.')
print('Ak stratis trpezlivost, napis "q". \n')


def generate_number(numbers_needed, choose_number):
    for i in range(4):
        cipher = random.choice(numbers_needed)
        while i == 0 and cipher == '0':
            cipher = random.choice(numbers_needed)
        choose_number += cipher
        numbers_needed.remove(cipher)
    return choose_number


def test_of_agreement(usr, four_digits):
    bulls = 0
    cows = 0
    for i in range(4):
        if usr[i] == four_digits[i]:
            cows -= 1
            bulls += 1
    cows += len(set(usr).intersection(set(four_digits)))
    return bulls, cows


def evaluation(guessing):
    if guessing < 7:
        return 'vynimocny'
    elif 7 < guessing <= 11:
        return 'velmi dobry'
    elif 11 < guessing <= 15:
        return 'dobry'
    elif 15 < guessing <= 19:
        return 'slaby'
    else:
        return 'mizerny'


four_digit_number = generate_number(numbers, chosen_num)

while num_bulls != 4:
    user = input()
    if user != 'q':
        while not user.isdigit() or len(user) != 4:
            user = input('Nezadal si 4-ciferne cislo alebo tvoja volba obsahuje neciselny znak. Zadaj cislo znova: ')
            if user == 'q':
                break
    if user == 'q':
        break
    guesses += 1
    num_bulls, num_cows = test_of_agreement(user, four_digit_number)
    print(num_bulls, ' bulls', num_cows, " cows")

if num_bulls == 4:
    print(f'Vyborne!! Pocet pokusov: {guesses}.')
    print(f'Je to {evaluation(guesses)} vysledok')
else:
    print('Skoda, ze to vzdavas.')
