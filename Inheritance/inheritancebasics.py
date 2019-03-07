class Human:
    

    def __init__(self, name, ff, iq):
        self.name = name
        self.ff = ff # = facebook friends
        self.iq = iq

    def befriend(self, other):
        self.ff += 1
        other.ff += 1

    def learn(self):
        self.iq += 1



class Wizard(Human):

    def __init__(self, name, ff, iq, mana):
        super().__init__(name, ff, iq)
        self.mana = mana

    def magic_friends(self, num):
        self.ff += num if self.mana>0 else 0
        self.mana -= 100


vernon = Human("Vernon", 0, 80)
tom = Wizard("Tom", 666, 130, 100)
dumbledore = Wizard("Albus", 999, 189, 100)

dumbledore.befriend(tom)
dumbledore.befriend(vernon)
dumbledore.magic_friends(100)

print("Friends Vernon: " + str(vernon.ff))
print("Friends Tom: " + str(tom.ff))
print("Friends Dumbledore: " + str(dumbledore.ff))

dumbledore.learn()
print("IQ Dumbledore: " + str(dumbledore.iq))