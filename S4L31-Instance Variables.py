import random

class Enemy:
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):  # self - its the object instanciated from the class
        print(self.atkl)

enemy1 = Enemy(40,49)
enemy1.getAtk()

enemy2 = Enemy(75,90)
enemy2.getAtk()





