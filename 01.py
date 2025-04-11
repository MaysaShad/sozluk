Program = {"hello" : "salam",
       "apple" : "alma",
       "lemon" : "limon",
       "cat" : "pişik",
       "dog" : "it",
       "flag" : "baýdak",
       "student" : "okuwçy",
       "family" : "maşgala",
       "pen" : "ruçka",
       "water" : "suw",
       "bread" : "çörek" }

while True:
    print(''' *****My Dictionary program*****
    1.Show
    2.Add
    3.Edit
    4.Delete
    5.Exit
    ''')

    a = int(input('Birini sayla: '))
    if 1 == a:
        for i,j in Program.items():
            print(i, '-', j)
    elif 2 == a:
        eng = input("English word: ")
        tkm = input('Turkmen word: ')
        Program[eng] = tkm
        print('Added')

    elif 3 == a:
        word = input('Enter the word in english: ')
        word1 = input('Enter the word in turkmen: ')
        Program[word] = word1
        print('Edited')

    elif 4 == a:
        soz = input('Enter the word in english: ')
        del Program[soz]
        print('Deleted')

    elif 5 == a:
        print('Thank you for using Program!')
        break

    else:
        print('Wrong command...')