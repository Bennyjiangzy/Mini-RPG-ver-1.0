from monster import Monster

class Magician(Monster):
    def __init__(self, level):
        super().__init__(level)
        self.health = float(20)
        self.power = float(0)
        
    # show the monster name and health and power
    def __str__(self):
        if self.health>0:
            return f"Magician ({self.health:.2f} health, {self.power:.2f} power)"
        else:
            return f"Magician (DEAD)" 

    #my own version stuff
    def new_version(self):
        return f"Magician"
    #my own version stuff
    @property
    def new_version2(self):
        if self.health>0:
            return f"({self.health:.2f} \033[1;32;40mhealth\033[0;37;40m, {self.power:.2f} \033[1;31;40mpower\033[0;37;40m)"
        else:
            return f"(DEAD)"

class Wolf(Monster):
    # show the monster name and health and power
    def __str__(self):
        if self.health>0:
            return f"Wolf ({self.health:.2f} health, {self.power:.2f} power)"
        else:
            return f"Wolf (DEAD)"

    #my own version stuff
    def new_version(self):
        return f"Wolf"
    #my own version stuff
    @property
    def new_version2(self):
        if self.health>0:
            return f"({self.health:.2f} \033[1;32;40mhealth\033[0;37;40m, {self.power:.2f} \033[1;31;40mpower\033[0;37;40m)"
        else:
            return f"(DEAD)"

class Giant(Monster):
    def __init__(self, level):
        super().__init__(level)
        self.power = self.power * 2
        self.health = self.health / 2

    # show the monster name and health and power
    def __str__(self):
        if self.health>0:
            return f"Giant ({self.health:.2f} health, {self.power:.2f} power)"
        else:
            return f"Giant (DEAD)" 

    #my own version stuff
    def new_version(self):
        return f"Giant"

    #my own version stuff
    @property
    def new_version2(self):
        if self.health>0:
            return f"({self.health:.2f} \033[1;32;40mhealth\033[0;37;40m, {self.power:.2f} \033[1;31;40mpower\033[0;37;40m)"
        else:
            return f"(DEAD)"

if  __name__=="__main__":
    pass