#!/usr/bin/python

def beast(id):
    if id == 'Goblin Smuggler' or id == '1' or id == 'goblin':
        monster = {'name': 'Goblin Smuggler', 'hp': 5, 'max': 2, 'min': 1, 'def': 0, 'agi': 20, 'acc': 5, 'crit': 1, 'exp': 25}
    if id == 'Giant Rat' or id == '2' or id == 'rat':
        monster = {'name': 'Giant Rat', 'hp': 7, 'max': 2, 'min': 1, 'def': 0, 'agi': 25, 'acc': 1, 'crit': 5, 'exp': 35}
    if id == 'Rock Crab' or id == 'crab' or id == '3':
        monster = {'name': 'Rock Crab', 'hp': 5, 'max': 1, 'min': 1, 'def': 2, 'agi': 10, 'acc': 1, 'crit': 1, 'exp': 25}
    if id == 'Armored Bear' or id == '4' or id == 'bear':
        monster = {'name': 'Armored Bear', 'hp': 10, 'max': 1, 'min': 1, 'def': 1, 'agi': 10, 'acc': 1, 'crit': 1, 'exp': 35}
    if id == 'Beserk Farmer' or id == '5' or id =='farmer':
        monster = {'name': 'Beserk Farmer', 'hp': 5, 'max': 2, 'min': 2, 'def': 0, 'agi': 15, 'acc': 1, 'crit': 1, 'exp': 35}
    if id == 'Wizard Novice' or id == '6' or id == 'wizard':
        monster = {'name': 'Wizard Novice', 'hp': 5, 'max': 4, 'min': 0, 'def': -1, 'agi': 15, 'acc': 1, 'crit': -1, 'exp': 25}

    if id == 'Stone Golem' or id == 'golem' or id == '7':
        monster = {'name': 'Stone Golem', 'hp': 20, 'max': 4, 'min': 2, 'def': 4, 'agi': 0, 'acc': -10, 'crit': 1, 'exp': 500}
    if id == 'Enraged Minotaur' or id == 'bull' or id == '8':
        monster = {'name': 'Enraged Minotaur', 'hp': 20, 'max': 6, 'min': 4, 'def': 2, 'agi': 10, 'acc': 0, 'crit': 1, 'exp': 500}
    if id == 'Highway Man' or id == 'robber' or id == '9':
        monster = {'name': 'Highway Man', 'hp': 15, 'max': 5, 'min': 1, 'def': 0, 'agi': 45, 'acc': 10, 'crit': 20, 'exp': 500}
    if id == 'Agile Marksman' or id == 'archer' or id == '10':
        monster = {'name': 'Agile Marksman', 'hp': 15, 'max': 5, 'min': 1, 'def': 1, 'agi': 30, 'acc': 20, 'crit': 10, 'exp': 500}
    if id == 'Elemental Apparition' or id == 'spirit' or id == '11':
        monster = {'name': 'Elemental Apparition', 'hp': 12, 'max': 10, 'min': 0, 'def': 0, 'agi': 15, 'acc': 1, 'crit': -1, 'exp': 500}

    return monster
