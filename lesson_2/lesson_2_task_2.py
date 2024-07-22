year = input("Введите год: ")

is_year_leap = int(year)

if (is_year_leap % 4 == 0):
        print("Год ",year,":", True)
else:
        print("Год ",year,":",False)