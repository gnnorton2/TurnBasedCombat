# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:02:22 2024

@author: gnoel
"""
import random

keepGoing = True
while keepGoing: 
    
    if userInput == input():
        if random.randint(1, 70) <= druidAccuracy:
            getDruidDamage = random.randint(1, 5)
            druidDamage = ({getDruidDamage} - {lichKingArmor})
            if druidDamage < 0:
                druidDamage == 0
            else:
                ({lichKingHP} - {druidDamage}) == newLichKingDamage
                print("The Lich King takes {druidDamage} from Malfurion!")
                if lichKingHP < 0:
                    print("Congratulations, Malfurion the Druid. You have successfully defeated the Lich King. You have grown wise from the ways of battle.")
	
        if random.randint(1, 30) <= lichKingAccuracy:
            getLichKingDamage = random.randint(1, 7)
            lichKingDamage = ({getLichKingDamage} - {druidArmor}) 
            if lichKingDamage < 0:
                        lichKingDamage == 0
            else:
                ({druidHP} - {lichKingDamage}) == newDruidDamage
                print("Malfurion takes {LichKingDamage} from the Lich King!")
                if druidHP < 0:
                    print("The forest cries for its protector. You have lost and the forest has died.")
		
	
		


