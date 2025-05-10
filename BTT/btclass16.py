class battery:
    def __init__(self):
        self.energy = 10

    def setEnergy(self):
        while True:
        
            self.energy = int(input("Hay sac pin(Nhap phan tram cho pin):   "))
            if self.energy < 0 and self.energy >100:
                print("Sac pin khong dung, vui long sac lai!")
            else:
                break
        return self.energy
    
    def getEnergy(self):
        print("Phan tram pin hien tai: {0}".format(self.energy))

    def decreaseEnergy(self):
        if  self.energy >= 2:
            self.energy -= 2
    
#*****************************************************************

class FlashLamp:
    def __init__(self):
        self.status = True
        self.battery = None
    def setbattery(self,b):
        self.battery = b
    
    def turnOn(self):
        if self.battery > 0:
            self.status = True
            print("Den bat")
        else:
            print("Het Pin")

    def turnOff(self):
        self.status = False
        print("Den tat *************")

def main():
    pin = battery()
    nhayden = FlashLamp()
    pin.setEnergy()
    nhayden.setbattery(pin.energy)
    print("Da lap pin")
    print("Phan tram pin hien tai la: {0}".format(nhayden.battery))

    for i in range(20):
        if nhayden.status == True:
            nhayden.turnOff()
        else:
            nhayden.turnOn()
            pin.decreaseEnergy()
            nhayden.setbattery(pin.energy)

    print("Phan tram pin hien tai la: {0}".format(nhayden.battery))

if __name__ == "__main__":
    main()
