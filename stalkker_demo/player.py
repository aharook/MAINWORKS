

class player():
    def __init__(self, health,armor_status,radiation_status,hungry_status):
        self.health = health
        self.armor_status = armor_status
        self.radiation_status = radiation_status
        self.hungry_status = hungry_status
        
    def heal(self,amount, med_kit):
        if med_kit <= 0:
            print("не лишилось аптечок!")
            return
        else:
            med_kit -= 1
            self.health += amount
            print(f"здоров'я поповнено на {amount}, залишилось аптечок: {med_kit}")
            if self.health > 100:
                self.health = 100
        return self.health
    
    def radiation_heal(self,radiation_status, anti_rad):
        if anti_rad <= 0:
            print("не лишилось антирадіаційних препаратів!")
            return
        else:
            anti_rad -= 1
            self.radiation_status -= radiation_status
            print(f"радіація зменшена на {radiation_status}, залишилось антирадіаційних препаратів: {anti_rad}")
            if self.radiation_status < 0:
                self.radiation_status = 0
        return self.radiation_status
    
    def hungry_heal(self,hungry_status, food):
        if food <= 0:
            print("No food left!")
            return
        else:
            food -= 1
            self.hungry_status -= hungry_status
            if self.hungry_status < 0:
                self.hungry_status = 0
        return self.hungry_status