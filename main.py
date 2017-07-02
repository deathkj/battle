#!/usr/bin/python
import random
import os
import beastiary
import lootdie
import data



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

ans = raw_input('New player? ')
if ans == 'yes' or ans == 'Yes' or ans == 'y' or ans =='1':
    filename = raw_input('Name your Character: ')
    data.new_file(filename)
    player = data.load_file(filename)
else:
    filename = raw_input('What is your Character Name? ')
    player = data.load_file(filename)

ans = raw_input('Wanna use health potion? ')
if ans == 'yes' or ans == 'Yes' or ans == 'y' or ans =='1':
    player['hp'] += 5
    if player['hp'] > player['life']:
        player['hp'] = player['life']


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
    player['exp'] += monster['exp']
    xpto = player['lvl']*83
    if player['exp'] > xpto:
        player['lvl'] += 1
        print "Woo!!! You leveled Up!\nCurrent Level: ", player['lvl']
        player['exp'] -= xpto


if player['hp'] <= 0:
    print "Oh dear you have died."
print "Your final hp: ", player['hp']
raw_input('\nPress enter to continue: ')

lootdie.loot(monster['name'])

ans = raw_input('Save? ')
if ans == 'yes' or ans == 'Yes' or ans == 'y' or ans =='1':
    data.save_file(filename,player)


os.system('rm beastiary.pyc')
os.system('rm lootdie.pyc')
os.system('rm data.pyc')


raw_input("\n\nPress enter to exit.")
