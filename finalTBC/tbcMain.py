# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:21:03 2024

@author: gnoel
"""

import tbc

def main():
    hero = tbc.Character()
    hero.name = "Malfurion the Druid"
    hero.HP = 35
    hero.accuracy = 70
    hero.maxDamage = 10
    hero.armor = 0

    monster = tbc.Character("LichKing", 50, 30, 5, 5)

    hero.printStats()
    monster.printStats()

    tbc.punchyPunchy(hero, monster)
    


if __name__ == "__main__":
    main()