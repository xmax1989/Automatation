# class User:
#    age = 0;
        
#    def __init__(self, name):    
#        print("я создался")
#        self.username = name

#    def sayName(self):
#        print("меня зовут ", self.username)

#    def sayAge(self):
#        print("мой возраст ", self.age)

#    def setAge(self, newAge):
#        self.age = newAge

#    def addCard(self, card):
#        self.card = card

#    def getCard(self):
#        return self.card


class User:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
        
    def sayFirst(self):   
        print("мое имя ", self.first_name)
        
    def sayLast(self):    
        print("моя фамилия ", self.last_name)
        
    def sayFirstLast(self):    
        print("меня зовут ", self.first_name, self.last_name)
        
        
        
        

