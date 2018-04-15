import random

class Enemy:
    atkl = 60  #Attak low
    atkh = 80  #Attak high

    def getAtk(self):  # self - its the object instanciated from the class
        print(self.atkl)

enemy1 = Enemy()
enemy1.getAtk()

enemy2 = Enemy()
enemy2.getAtk()





