#!/usr/bin/python
import random

def loot(id):
    print 'Rolling for Loot...'
    roll = random.randrange(1,101)

    if roll <= 55:
        print 'Common Drop'
    if roll > 55 and roll <= 80:
        print 'Uncommon Drop'
    if roll > 80 and roll <= 95:
        print 'Rare Drop!'
    if roll > 95:
        print "Ultra Rare Drop!!!"

    raw_input(".")
    raw_input(".")
    raw_input(".")

    roll = random.randrange(1,11)
    print 'Item Roll %i\nCheck Drop Table' % (roll)