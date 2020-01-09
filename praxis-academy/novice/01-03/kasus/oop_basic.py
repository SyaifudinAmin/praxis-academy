class Hero:

    def __init__(self, name,healt,armor,attack):
        self.name = name
        self.healt = healt
        self.armor = armor
        self.attack = attack

    def srg(self,lawan,lwn):
        print (self.name + " menyerng " + lawan.name)
        lawan.dsrg(self, self.attack,lwn,lwn.attack)


    def dsrg(self,musuh, attackmusuh,rekan,attackrekan):
        print(self.name + " diserang " +musuh.name)
        attackditerima = attackmusuh/self.armor
        print("serangan : " + str(attackmusuh))
        print("armor: " + str(self.armor)) 
        print("serangan di dapatkan : " + str(attackditerima))
        print("Healt = " + str(self.healt))
        self.healt -= attackditerima
        print("sisa Healt =" + str(self.healt))
        print(rekan.name +" ikut menyerang "+ musuh.name)
        attacktambahan = attackrekan/self.armor
        print("attck tambahan: " + str(attackrekan))
        print("armor: " + str(self.armor))
        print("self adalah: "+ str(self.name))
        self.healt-= attacktambahan
        print(str(self.healt))
        # org3.srg1(self)
        # org3.srg1(self)

    def srg1(self,musuh):
        print(self.name +"juga menyerang"+ musuh.name)
        # print(str(musuh.healt))

hero1 = Hero('Axe',1000,7,50)
hero2 = Hero('Sv',1100,5,30)
hero3 = Hero('Mir',800,4,70)
 
hero1.srg(hero2,hero3)
print("")
hero3.srg(hero1,hero2)