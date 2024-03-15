# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:33:52 2024

@author: gnoel
"""

class Character(object):
	def __init__(self):
		self.name

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		self.__name = value

	@property
	def hitPoints(self):
		return self.__hitPoints

	@hitPoints.setter
	def hitPoints(self, value):
		value = self.testInt(value, 0, 10, 0)
		self.__hitPoints = value

	def printStats(self):
		print(f"""
{self.name}
		HP: {self.hitPoints}
		Accuracy: {self.hitChance}
		Max Damage: {self.maxDamage}
		Armor: {self.armor}
		""")
        
    def hit(self, enemy):
        if random.randint(1,100) < self.hitPerc:
            print(f"{self.name} hits {enemy.name}...")
            damage = random.randint(1, self.maxDamage)
            print(f"for {damage} points of damage...")
            damage -= enemy.armor
            if damage < 0:
                damage = 0
            if enemy.armor > 0:
                print(f" but {enemy.name} has {enemy.armor} of armor ")
                

	def testInt(self, value, min = 0, max = 100, default = 0):
		#takes in value, checks to see if int between min and max
		out = default
		if type(value) == int:
			if value >= min:
				if value <= max:
					out = value
				else:
					print("Too large")
			else:
				print("Too small")
		else:
			print("Must be an int")
		return out

	def main():
		c = Character()
		c.name = "Malfurion the Druid"
		c.printStats()  #can add c.whatever stat and set whatever name or stats you want for this particular character

if __name__ == "__main__":
    main()