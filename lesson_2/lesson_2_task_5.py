month = input("Введите номер месяца: ")

mon = int(month)

def month_to_season():
    
    if (mon == 1 or mon == 2 or mon == 12):
        
        print("Зима")

    elif (mon == 3 or mon == 4 or mon == 5):
    
        print("Весна")
    
    elif (mon == 6 or mon == 7 or mon == 8):

        print("Лето")

    elif (mon == 9 or mon == 10 or mon == 11):

        print("Осень")

month_to_season()