from monster_team import MonsterTeam
from monster_custom import Wolf, Giant, Magician
from monster import Monster

class Hero:
    def __init__(self,name,health=100,power=50):
        self.name=name
        self.health=float(health)
        self.power=power
        self.healtimes=0
        self.gold=0

    # check the hero is alive if helth point greater than 0
    @property
    def is_alive(self):
        return self.health>0

    # return the information of hero health and power add color for the word 'HP' and 'AP'
    def get_description(self):
        if self.health>20:
            return f"{self.name} ({self.health}\033[1;32;40mHP\033[0;37;40m, {self.power}\033[1;31;40mAP\033[0;37;40m)"
        elif self.health>0 and self.health <= 20:
            return f"{self.name} (\033[1;31;40m{self.health}\033[0;37;40m\033[1;32;40mHP\033[0;37;40m, {self.power}\033[1;31;40mAP\033[0;37;40m)"
        else:
            return f"{self.name} (DEAD)"
    # deduct the heath point of hero and deduct the health point of monster and reset the heal times
    def attack(self,Monster):
        x=0
        #test the monster tyoe is correct
        if type(Monster) == MonsterTeam:
            #automatically search the first alive monster in the list
            while Monster._monsters[x].is_alive == False:
                x+=1
            self.health-=Monster._monsters[x].power
            Monster._monsters[x].health-=self.power
            self.healtimes=0
        else:
            raise TypeError('invalid type')

    # deduct the heath point of hero and deduct the health point of monster and reset the heal times
    def block(self,Monster):
        x=0
        # test the monster tyoe is correct
        if type(Monster) == MonsterTeam:
            #automatically search the first alive monster in the list
            while Monster._monsters[x].is_alive == False:
                x+=1
            self.health-=Monster._monsters[0].power*0.3
            Monster._monsters[0].health-=self.power*0.5
            self.healtimes=0
        else:
            raise TypeError('invalid type')

    # add money
    def goldplus(self):
        self.gold+=1

    #My own fun version 
    @property
    def new_version(self):
        return f"{self.name}"
        
    #My own fun version 
    @property
    def new_version2(self):
        if self.health>20:
            return f"({self.health}\033[1;32;40mHP\033[0;37;40m, {self.power}\033[1;31;40mAP\033[0;37;40m)"
        elif self.health>0 and self.health <= 20:
            return f"(\033[1;31;40m{self.health}\033[0;37;40m\033[1;32;40mHP\033[0;37;40m, {self.power}\033[1;31;40mAP\033[0;37;40m)"
        else:
            return f"(DEAD)"




if __name__=="__main__":
    me=Hero('benny')
    print(me.new_version)
    print(me.new_version2)