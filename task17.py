greet = input()
google_office = [
    '1 google_kazakstan'
    '2 google_paris'
    '3 google_uar'
    '4 google_kyrgystan'
    '5 google_san_francisco'
    '6 google_germany'
    '7 google_moscow'
    '8 google_sweden'
    ]

if greet == 'Hello':
    

    for x in google_office:
        print(x)

    choice_of_office = int(input('Enter a number: '))
    complain = input('Write your complain: ')

    if choice_of_office == 1:
        with open ('google_kazakstan.txt', 'w') as f:
            f.write(complain)

    if choice_of_office == 2:
        with open('google_paris.txt', 'w',) as f:
            f.write(complain)

    if choice_of_office == 3:
        with open('google_uar.txt', 'w',) as f:
            f.write(complain)

    if choice_of_office == 4:
        with open('google_kyrgyzstan.txt', 'w',) as f:
            f.write(complain)

    if choice_of_office == 5:
        with open('google_san_francisco.txt', 'w',) as f:
            f.write(complain)

    if choice_of_office == 6:
        with open('google_germany.txt', 'w',) as f:
            f.write(complain)

    if choice_of_office == 7:
        with open('google_moscow.txt', 'w',) as f:
            f.write(complain)

    if choice_of_office == 8:
        with open('google_sweden.txt', 'w',) as f:
            f.write(complain)

else:
    print('wrong')