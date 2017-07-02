def save_file(filename,player):

    filename += '.sav'
    dat = str(player['hp'])
    dat += '\n'
    dat += str(player['exp'])
    dat += '\n'
    dat += str(player['lvl'])
    dat += '\n'
    dat += str(player['class'])

    file = open(filename, "w")
    file.write(dat)
    file.close()
    return

def new_file(filename):

    filename += '.sav'
    player = {'name':'You', 'life':10, 'hp':10, 'max':2, 'min':1, 'def':0, 'agi':15, 'acc':1, 'crit':1, 'exp':0, 'lvl':1, 'class': 'Novice'}
    dat = str(player['hp'])
    dat += '\n'
    dat += str(player['exp'])
    dat += '\n'
    dat += str(player['lvl'])
    dat += '\n'
    dat += player['class']

    file = open(filename, "wb")
    file.write(dat)
    file.close()
    return

def load_file(filename):

    filename += '.sav'

    dat = [line.rstrip('\n') for line in open(filename)]

    hp = int(int(dat[0]))
    exp = int(dat[1])
    lvl = int(dat[2])
    role = dat[3]
    life = 10 + int(lvl/2)
    maxh = 2+int(lvl/5)
    minh = 1+int(lvl/10)
    player = {'name': 'You', 'life': life, 'hp':hp, 'max':maxh, 'min':minh, 'def':0, 'agi': 15, 'acc': 1, 'crit': 1, 'exp': exp, 'lvl': lvl, 'class':role}
    return(player)

