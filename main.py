import random

print "You will fight a Goblin"
player = 10
pmax = 2
pmin = 1
pdef = 0
pagi = 20
pacc = 1
pcrit = 1




monster = 5
emax = 2
emin = 1
edef = 0
eagi = 15
eacc = 5
ecrit = 1

raw_input("\nPress enter to continue.")

while (player > 0 and monster > 0):
    if random.randrange(pacc,100+1) > eagi:
        print "You landed a hit!"
        monster -= random.randrange(pmin,pmax+1)
    else:
        print "You missed!"
    raw_input("\nPress enter to continue.")
    if monster <= 0:
        print "Enemy has died."
        break
    if random.randrange(eacc,100+1) > pagi:
        print "Enemy landed a hit!"
        player -= random.randrange(emin,emax+1)
    else:
        print "Enemy missed!"
    raw_input("\nPress enter to continue.")
    if player <=0:
        print "Oh dear you have died."
        break

    print "Monster health: ", monster
    print "\nYour Health: ", player


print "Congratz your a winner!"

raw_input("\n\nPress enter to exit.")