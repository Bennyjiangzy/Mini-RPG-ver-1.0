from hero import Hero
from shop import Shop
from shop_item import BigHealingPotion, SmallHealingPotion, WeaponUpgrade
from monster_team import MonsterTeam
# A01158605 Benny Jiang

#I add some color to the data
#Also, I change the Hero only can attack the first monster. The Hero cannot attack the second monster until the previous monster dead
#Add additional option for tutorial.
def main():
    # ask the name of user want
    name=input('Type your name hero \n')
    # create the hero by the name user given
    player=Hero(name)
    # first monster level is 1
    levelOfmonster=1
    #create shop
    shop=Shop('../tests/test_shop.txt')

    while True:
        #generate a new monster
        new_moster_team=MonsterTeam(levelOfmonster)
        print('****A new monster team jump from the jungle****')
        print('')
        print('-'*40)
        #provide information to the player
        print(Monster_Hero_name(new_moster_team,player))
        print(Monster_Hero_data(new_moster_team,player))
        print('-'*40)
        print('')
        #Total gold in a round 
        Totalgold=-1
        # player will take action in the battle until player dead or monster dead
        while new_moster_team.is_alive:
            
            # collect user action
            user_action=input('\033[1;31;40m[A]\033[0;37;40mttack, \033[1;34;40m[B]\033[0;37;40mlock, \033[1;32;40m[S]\033[0;37;40mhop [T]utorial\n')
            print('')
            # call the attack if user type A or a and reset healtimes
            if user_action.lower()=='a':
                print("\033[1;31;40mYou attack the monster\033[0;37;40m")
                player.attack(new_moster_team)
                new_moster_team.next_turn()

                # return information after user take action
                print('-'*40)
                print(Monster_Hero_name(new_moster_team,player))
                print(Monster_Hero_data(new_moster_team,player))
                print('-'*40)

            # call the block if user type B or b and reset healtimes
            elif user_action.lower()=='b':
                print("\033[1;34;40mYou block the monster\033[0;37;40m")
                player.block(new_moster_team)
                new_moster_team.next_turn()

                # return information after user take action
                print('-'*40)
                print(Monster_Hero_name(new_moster_team,player))
                print(Monster_Hero_data(new_moster_team,player))
                print('-'*40)

            # call the tutorials interface
            elif user_action.lower()=='t':
                while True:
                    # if user type A show the attack tutorials
                    user_action_Tu=input('\033[1;31;40m[A]\033[0;37;40mttack Tutorial, \033[1;32;40m[S]\033[0;37;40mhop Tutorial')
                    if user_action_Tu.lower() =='a':
                        print(Tutorials_Attack())
                        break
                    # if user type S show the Shop tutorials
                    elif user_action_Tu.lower()=='s':
                        print(Tutorials_Shop())
                        break
                    # show the error message if no macthed message
                    else:
                        print('\033[1;31;40mPlease type valid action\033[0;37;40m')
                        print(' ')
                        print(' ')

            # call the shop if user type S or s
            elif user_action.lower()=='s':

                while True:
                    #print the list of the products in the shop
                    print(shop)
                    # print(shop.available_items)
                    print('')
                    print(f'You have {player.gold}g')
                    #juddge player have enough gold to pay the products
                    user_shop_action=input('Type index of the products(0 is start) or type \033[1;32;40m[E]\033[0;37;40m to quit\n')
                    print('')

                    #break the shop loop if user type e to exit the shop
                    if user_shop_action.lower() == 'e':
                        print('-'*40)
                        print(Monster_Hero_name(new_moster_team,player))
                        print(Monster_Hero_data(new_moster_team,player))
                        print('-'*40)
                        break

                    #test if the input is a digit or not
                    elif user_shop_action.isdigit():
                        Int_input=int(user_shop_action)
                        #test the hero have enough gold or not if not show the error message
                        if shop.items[Int_input]==SmallHealingPotion.name and SmallHealingPotion.price <= player.gold:
                            shop.buy(Int_input).change(player)
                            print(player.get_description())
                            player.gold-=SmallHealingPotion.price

                        elif shop.items[Int_input]==BigHealingPotion.name and BigHealingPotion.price <= player.gold:
                            shop.buy(Int_input).change(player)
                            print(player.get_description())
                            player.gold-=BigHealingPotion.price
                        
                        elif shop.items[Int_input]==WeaponUpgrade.name and WeaponUpgrade.price <= player.gold:
                            shop.buy(Int_input).change(player)
                            print(player.get_description())
                            player.gold-=WeaponUpgrade.price

                        #error message if no enough gold
                        else:
                            print('\033[1;31;40mYou don`t have enough gold!!!\033[0;37;40m')
                            print(' ')
                            print(' ')

                    #error message if no matched input
                    else:
                        print('\033[1;31;40mPlease type valid action\033[0;37;40m')
                        print(' ')
                        print(' ')
                             


            # add the gold if the monster is dead each monster will only add once 
            for monster in range(len(new_moster_team._monsters)):
                if monster >Totalgold:
                    if new_moster_team._monsters[monster].is_alive == False:
                        player.goldplus()
                        print(f'You have {player.gold}g')
                        Totalgold+=1




            # break the inside loop if player die
            if not player.is_alive:
                break

        # break the outside loop if player die
        if not player.is_alive:
                break
        # return a message after moster is dead
        print('\033[1;33;40m****You win!****\033[0;37;40m')
        print('')
        print('')


        # increase the level for next new monster if player win
        levelOfmonster+=1
    # return dead messgae and the level reached if the loop break means hero health point is 0
    print(f'\033[1;37;41m****You are died at level {levelOfmonster} **** \033[0;37;40m')
        

# print the information of how the attack and block wokrs
def Tutorials_Attack():
    Tutorial = "\n".join([
        "\033[1;31;40mType [A] will [A]ttack the first monster",
        "The first monster's health will be deducted by Hero AP",
        "Hero will also take a damange by monster's AP\033[0;37;40m",
        '\n',
        "\033[1;34;40mType [B] will [B]lock the first monster",
        "The first monster's health will be deducted by Hero AP times 0.5",
        "Hero will also take a damange by monster's AP times 0.3\033[0;37;40m"
        '\n',
        "\033[1;33;40mHero' action will only effect to the first monster in the team\033[0;37;40m",
    ])
    return Tutorial

# print the information of how the shop works
def Tutorials_Shop():
    Tutorial = "\n".join([
        "Shop has three type of items",
        "small potion: Heal 10 health points",
        "big postion: Heal 50 health points",
        "weapon upgrade: Add hero power by 1.05",
        "Each monster Hero defeated will get 1 gold",
    ])
    return Tutorial

# prine the name for hero and monster in one line
def Monster_Hero_name(monsterlist,Hero):
    Name="{:^20}       ".format(Hero.new_version)
    for i in range(len(monsterlist)):
        if monsterlist._monsters[i].health<=0:
            Name+=''
        else:
            Name+='{:^20}'.format(monsterlist._monsters[i].new_version())
    return Name

# prine the health and power for hero and monster in one line
def Monster_Hero_data(monsterlist,Hero):
    Data="{:^20}       ".format(Hero.new_version2)
    for i in range(len(monsterlist)):
        if monsterlist._monsters[i].health<=0:
            Data+=''
        else:
            Data+='{:^33}'.format(monsterlist._monsters[i].new_version2)
    return Data








main()