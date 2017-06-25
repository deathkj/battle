#!/usr/bin/python
import random
import os

print "You will fight a Robber"
player = 15
pmax = 6
pmin = 1
pdef = 2
pagi = 20
pacc = 30
pcrit = 20




monster = 15
emax = 5
emin = 1
edef = 2
eagi = 45
eacc = 10
ecrit = 20

raw_input("\nPress enter to continue.")

while (player > 0 and monster > 0):
    print "\nMonster health: ", monster
    print "Your Health: ", player
    raw_input('\nPress enter to continue: ')
    os.system('clear')

    dmg = 0
    roll = random.randrange(pacc,101)
    print "Your roll: ", roll
    if roll >= (101-pcrit):
        dmg = pmax+random.randrange(pmin,pmax+1)-edef
        if dmg < 0:
            dmg =0
        print "You landed a crit! Dealing %i damage." % (dmg)
        monster -= dmg
    elif roll > eagi:
        dmg = random.randrange(pmin,pmax+1) - edef
        if dmg < 0:
            dmg = 0
        print "You landed a hit! Dealing %i damage." % (dmg)
        monster -= dmg
    else:
            print "You missed!"

    if monster <= 0:
        print "Enemy has died. Congratz your a winner!"
        break

    dmg =0
    roll = random.randrange(eacc,101)
    print "Monster roll: ", roll
    if roll >= (101-ecrit):
        dmg = emax+random.randrange(emin,emax+1)-pdef
        if dmg < 0:
            dmg =0
        print "Enemy landed a crit! Dealing %i damage" % (dmg)
        player -= dmg
    elif roll > pagi:
        dmg = random.randrange(emin,emax+1)-pdef
        if dmg < 0:
            dmg =0
        print "Enemy landed a hit! Dealing %i damage" % (dmg)
        player -= dmg
    else:
        print "Enemy missed!"


    if player <=0:
        print "Oh dear you have died."

        break

    raw_input('Press enter to continue: ')
    os.system('clear')


print "Your final hp: ", player

raw_input("\n\nPress enter to exit.")