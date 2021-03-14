from monster_custom import Wolf,Giant,Magician

class MonsterTeam:
    def __init__(self,level):
        self.level=level
        f = open(f'../levels/level_{level}.txt')
        lines = f.readlines()
        self._monsters=list()
        for line in lines:
            line=line.strip('\n')
            if 'wolf' in line:
                self._monsters.append(Wolf(int(line[-1])))
            elif 'giant' in line:
                self._monsters.append(Giant(int(line[-1])))
            elif 'magician' in line:
                self._monsters.append(Magician(int(line[-1])))


    def __len__(self):
        return len(self._monsters)
 
    # find the highest health points in the team
    @property
    def healthiest_monster(self):
        box=0
        for i in range(len(self._monsters)):
            if self._monsters[i].health>0:
                box=self._monsters[i]
                break

        if box == 0:
            return 'All the monster is dead'
            
        for monster in self._monsters:
            if monster.health>box.health:
                box=monster
            
        return box

    # find the lowerst power points monster in the team
    @property
    def weakest_monster(self):
        box=0
        #check the monster is dead or not
        for i in range(len(self._monsters)):
            if self._monsters[i].health>0:
                box=self._monsters[i]
                break
        
        if box == 0:
            return 'All the monster is dead'

        for monster in self._monsters:
            if monster.health == 0:
                continue
            if monster.power<box.power:
                box=monster

        return box

    # show the health power points for the monster team
    @property
    def health(self):
        totalHpoints=0
        for monster in self._monsters:
            if monster.health>0:
                totalHpoints+=monster.health
        print(totalHpoints)
        return totalHpoints

    # show the total power points for the monster team
    @property
    def power(self):
        totalPpoints=0
        for monster in self._monsters:
            if monster.health>0:
                totalPpoints+=monster.power
        return totalPpoints

    # rerturn the status of monster team
    def __str__(self):
        sortedlist=sorted(self._monsters,reverse=True)
        message=list()
        numberofAlive=0
        for monsterIndex in range(len(sortedlist)):
            if sortedlist[monsterIndex].health>0:
                message.append(f'{sortedlist[monsterIndex]}')
                numberofAlive+=1
            else:
                message.append(f'{sortedlist[monsterIndex]}')

        message.insert(0,f"{numberofAlive}/{len(sortedlist)} monsters:")
        return "\n".join(message)

    # return the alive monster from the health  high to low
    @property
    def alive_monsters(self):
        alive_monster=[monster for monster in self._monsters if monster.health>0]
        return sorted(alive_monster, reverse=True)

    


    #test all the monster is alive if at least one will return true else false
    @property
    def is_alive(self):
        for i in range(len(self._monsters)):
            if self._monsters[i].is_alive:
                return True
        return False




    def next_turn(self):
        #count numbers of wolf
        numberofWolfves=0
        for count in range(len(self._monsters)):
            if type(self._monsters[count]) == Wolf and self._monsters[count].health>0 :
                 numberofWolfves+=1

        #increase wolf ap based on their numbers and magician heal other monster excpet magician
        for i in range(len(self._monsters)):
            if type(self._monsters[i]) == Wolf:
                if numberofWolfves != 1:
                    self._monsters[i].power+=numberofWolfves
            elif type(self._monsters[i]) == Magician and self._monsters[i].is_alive:
                for Healing in range(len(self._monsters)):
                    if type(self._monsters[Healing]) != Magician and self._monsters[Healing].is_alive:
                        self._monsters[Healing].health+=self._monsters[Healing].health*0.1







if __name__=='__main__':
    wolf_1 = Wolf(5)
    wolf_2 = Wolf(5)
    giant = Giant(4)
    magician = Magician(1)
    team = MonsterTeam(1)
    team._monsters = [wolf_1, wolf_2, giant, magician]
    print(team)