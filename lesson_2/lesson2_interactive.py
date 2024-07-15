# приветствие
name = input("Как вас зовут? ")
if name == "Neo":
    print("Следуй за белым кроликом " + name +"...") # пасхалка=)
    exit()
else:
    print("Здравствуйте " + name)



# оценка от пользователя
rate_as_str = input(name + " оцените работу оператора (от 1 до 5) ") #str
rate = int(rate_as_str) # int

# проверить что оценка от 1 до 5

if(rate < 1):
    rate = 1
if(rate > 5):
    rate = 5

# обратная связь с зывисимостью от оценки

feedback = ''

if rate == 1:
    feedback = input("расскажите что вам не понравилось : ")
elif rate == 2:
    feedback = input("расскажите что вас смутило : ")
elif rate == 3:
    feedback = input("расскажите что нам улучшить : ")
elif rate == 4:
    feedback = input("расскажите как нам стать лучше : ")
else:
    feedback = input("расскажите что вам понравилось : ")
    
print("Коментарий от " + name + " : " + feedback)
print("Спасибо за помощь! "+ name)
