class battery:
    def __init__(self):
        self.energy = 10
#///////////////////////////

    def setEnergy(self):
        while True:
        
            self.energy = int(input("Hay sac pin(Nhap phan tram cho pin):   "))
            if self.energy < 0 and self.energy >100:
                print("Sac pin khong dung, vui long sac lai!")
            else:
                break

#////////////////////////////

    def getEnergy(self):
        print("Phan tram pin hien tai: {0}".format(self.energy))

#////////////////////////////

    def decreaseEnergy(self):
        self.energy -= 2
    
#*****************************************************************
battery_1 = battery()
battery_1.setEnergy()
battery_1.getEnergy()
battery_1.decreaseEnergy()
battery_1.getEnergy()
