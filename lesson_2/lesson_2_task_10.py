
def bank(X,Y):
    
    profit = X*1.1**Y

    return profit

X = float(input("Введите сумму вклада: "))

Y = float(input("Введите срок вклада(лет): "))

result = bank(X,Y)

print("Cумма вклада: ",X , "Количество лет: ",Y , "Сумма с процентами: ", result)




    