#Tidak  memakai template karena baru tahu ada template saat sudah mau kelar
#import rng
import random
#setup variable dan random hp, atk, jumlah musuh
input_atk = input("Masukkan ATK Depram : ")
input_def = input("Masukkan DEF Depram : ")
HP_boss = random.randint(20,100)
ATK_boss = random.randint(10,30)
jumlah_musuh = random.randint(1,2)
#setup loop
stop = False
stop_1 = False

#setup class
class entity :
    #nama, hp, atk semua entity di game
    def __init__(self, nama, HP, ATK) :
        self.nama = nama
        self.HP = HP
        self.ATK = ATK
        
    #cek nyawa
    def is_alive (self) :
        if int(self.HP) > 0 :
            return self.HP
        else :
            return self.HP
    #return atk entity
    def attack (self) :
        return self.ATK
    #return take damage entity
    def take_damage (self) :
        return self.HP

class player(entity) :
    def __init__(self, nama, HP, ATK, Defense):
        super().__init__(nama, HP, ATK)
        #defense player
        self.Defense = Defense

class boss(entity) :
    def __init__(self, nama, HP, ATK):
        super().__init__(nama, HP, ATK)

Final_boss = boss("Final Boss", f"{HP_boss}", f"{ATK_boss}")
Depram = player("Depram", "100", f"{input_atk}", f"{input_def}")
print ("---------------")
print (f"Terdapat {jumlah_musuh} yang menghadang Depram!")
print ("---------------")

#setup loop
for i in range (0, jumlah_musuh - 1) :
    print (f"Enemy {i} muncul!")
    HP_enemy = random.randint(20,100)
    ATK_enemy = random.randint(10,30)
    Enemy = entity(f"{i}", f"{HP_enemy}", f"{ATK_enemy}")

    print ("----Status----")
    print (f"Enemy {Enemy.nama:<14}", f"HP :{Enemy.HP:<8}")
    print (f"{Depram.nama:<20}", f"HP :{Depram.HP:<8}")
    print ("--------------")

    while stop == False :
        #saling terus menyerang sampai ada yang mati
        print (f"{Depram.nama} menyerang Enemy {Enemy.nama} dengan {Depram.attack()}")
        Hp = int(Enemy.take_damage()) - int(Depram.attack())
        Enemy = entity(f"{i}", f"{Hp}", f"{ATK_enemy}")
        print (f"{Enemy.nama} menyerang {Depram.nama} dengan {int(Enemy.attack()) - int(Depram.Defense)}")
        Hp = int(Depram.take_damage()) - (int(Enemy.attack()) - int(Depram.Defense))
        Depram = player("Depram", f"{Hp}", f"{input_atk}", f"{input_def}")
        #apabila ada yang mati, stop loop
        if int(Depram.is_alive()) < 0 :
            print ("Tidak! Depram telah dikalahkan oleh musuhnya :(")
            stop = True
            stop_1 = True
        elif int(Enemy.is_alive()) < 0 :
            print (f"Enemy {Enemy.nama} telah dikalahkan")
            stop = True

if int(Depram.is_alive()) < 0 :
    stop_1 = True
else :
    print (f"{Final_boss.nama} muncul!")  
    print ("----Status----")
    print (f"Enemy {Final_boss.nama:<14}", f"HP :{Final_boss.HP:<8}")
    print (f"{Depram.nama:<20}", f"HP :{Depram.HP:<8}")
    print ("--------------")

#loop lawan boss
while stop_1 == False :
    print (f"{Depram.nama} menyerang {Final_boss.nama} dengan {Depram.attack()}")
    Hp = int(Final_boss.take_damage()) - int(Depram.attack())
    Final_boss = entity(f"{Final_boss.nama}", f"{Hp}", f"{Final_boss.attack()}")
    print (f"{Final_boss.nama} menyerang {Depram.nama} dengan {int(Final_boss.attack())}")
    Hp = int(Depram.take_damage()) - int(Final_boss.attack())
    Depram = player("Depram", f"{Hp}", f"{input_atk}", f"{input_def}")
    #apabila ada yang mati, stop loop
    if int(Depram.is_alive()) < 0 :
        print ("Tidak! Depram telah dikalahkan oleh musuhnya :(")
        stop_1 = True
    elif int(Final_boss.is_alive()) < 0 :
        print (f"{Final_boss.nama} telah dikalahkan")
        stop_1 = True

if int(Final_boss.take_damage()) < 0 :
    print ("Selamat! Semua musuh Depram telah kalah!")

        







    


