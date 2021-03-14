
class Monster:
    def __init__(self,level):
        self.level=level
        self.set_health(level)
        self.set_power(level)

    # give moster health point based on their level if level is string will raise an error
    def set_health(self,value):
        if type(value) is str:
            raise AttributeError('have to be a number')
        self.health=float(10+value*10)

    # give moster power point based on their level if level is string will raise an error
    def set_power(self,value):
        if type(value) is str:
            raise AttributeError('have to be a number')
        self.power=float(value*5)
    # check the moster is alive or not
    @property
    def is_alive(self):
        return self.health>0
    
    # ri==to set a rule for the comparison 
    def __lt__(self,other):
        if isinstance(self,Monster) and isinstance(other,Monster):
            return (self.health, self.power) < (other.health, other.power)
        else:
            raise TypeError("wrong value")



    # return the information of monster health and power add color for the word 'HP' and 'AP'
    def get_description(self):
        return f"Monster ({self.health}\033[1;32;40mHP\033[0;37;40m, {self.power}\033[1;31;40mAP\033[0;37;40m)"


if __name__=="__main__":
    kk=Monster(1)
