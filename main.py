#!/usr/bin/python
import random
import os
import beastiary
import lootdie



def attack(dict1,dict2):
    alive = 1
    dmg = 0
    roll = random.randrange(dict1['acc'], 101)
    print "%s roll: " % (dict1['name']), roll
    if roll >= (101 - dict1['crit']):
        dmg = dict1['max'] + random.randrange(dict1['min'], dict1['max'] + 1) - dict2['def']
        if dmg < 0:
            dmg = 0
        print "%s landed a crit! Dealing %i damage." % (dict1['name'],dmg)
        dict2['hp'] -= dmg
    elif roll > dict2['agi']:
        dmg = random.randrange(dict1['min'], dict1['max'] + 1) - dict2['def']
        if dmg < 0:
            dmg = 0
        print "%s landed a hit! Dealing %i damage." % (dict1['name'],dmg)
        dict2['hp'] -= dmg
    else:
        print "%s missed!" % (dict1['name'])
    if dict2['hp'] <= 0:
        alive = 2
    return alive



player = {'name':'You','hp':15,'max':6,'min':1,'def':2,'agi':20,'acc':30,'crit':20}

id = raw_input('Enter beast code: ')
monster = beastiary.beast(id)
print "You will fight a %s" % (monster['name'])
raw_input("\nPress enter to continue.")

alive = 1
while (alive == 1):
    print "\n%s health: %i" % (monster['name'],monster['hp'])
    print "Your Health: ", player['hp']
    raw_input('\nPress enter to continue: ')
    os.system('clear')

    if player['agi'] >= monster['agi']:
        alive = attack(player, monster)
        if alive == 2:
            break
        alive = attack(monster, player)
    else:
        alive = attack(monster, player)
        if alive == 2:
            break
        alive = attack(player, monster)

    raw_input('Press enter to continue: ')
    os.system('clear')

if monster['hp'] <= 0:
    print "Enemy has died. Congratz your a winner!"
if player['hp'] <= 0:
    print "Oh dear you have died."
print "Your final hp: ", player['hp']
raw_input('\nPress enter to continue: ')

lootdie.loot(monster['name'])

os.system('rm beastiary.pyc')
os.system('rm lootdie.pyc')



raw_input("\n\nPress enter to exit.")
