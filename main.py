from pytania import pytania
from random import choice
from time import sleep









def startGry():
    print("Quiz związany z grami: League of legends, CS:go oraz overwatch")
    pytanie = input("Wpisz 'zaczynam', aby zaczac \n")
    if pytanie.lower() == "zaczynam":
        gra()
    else:
        print("Zła opcja")
        sleep(2)
        startGry()    
def gra():
    pytaniaZuzyte = []        
    twoje_punkty = 0
    max_punkty = 25
    
    for x in range(max_punkty):
        print(x)
        random_question = choice(pytania)
        
        while random_question in pytaniaZuzyte:
            random_question = choice(pytania)
        
        
        question_text = random_question["pytanie"]
        print(question_text)

        for index, answer in enumerate(random_question["odpowiedzi"]):
            print(f'{index}. {answer["text"]}')
        
        odpowiedz = input("Twoja odpowiedź to: \n")
        is_correct = False
        for answer in random_question["odpowiedzi"]:
            if odpowiedz.lower() == answer['text'].lower():
                is_correct = answer['poprawne']
                break

        if is_correct:
            print("Poprawna odpowiedź")
            twoje_punkty += 1
        else:
            print("Niepoprawna odpowiedź")
        pytaniaZuzyte.append(random_question)
    print(f"Twoja ilosc puntkow: {twoje_punkty} / {max_punkty}")
    if twoje_punkty == max_punkty:
        print("Wygrałeś, zdobyłeś maksymalną ilość punktów")

        
        
        


startGry()
