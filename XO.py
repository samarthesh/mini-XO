from random import randint, choice
from subprocess import call
from time import sleep

class Game(object):
    ScoreBoard = {'X': int(), 'O': int()}
    def FeelTable(self):
        self.Counter = 0
        self.Table = [['-' for i in range(3)] for j in range(3)]
    def ShowTable(self):
        call('clear', shell = True)
        print('O: %s | X: %s' %(self.ScoreBoard['O'], self.ScoreBoard['X']))
        print('* ! * ! * !')
        for i in self.Table:
            for j in i:
                print(j, end = '    ')
            print('\n')
        print('* ! * ! * !')
    def Play(self):
        self.ShowTable()
        if self.Counter%2 == 0:
            ChoiceTemp = 'O' if self.Counter%2 == 0 else 'X'
            choice = input('%s\'s trun: ' %ChoiceTemp)
            try:
                if len(choice) == 2 and int(choice[0]) >= 1 and int(choice[0]) <= 3 and int(choice[1]) >= 1 and int(choice[1]) <= 3:
                    if self.Table[int(choice[0]) - 1][int(choice[1]) - 1] == '-':
                        self.Table[int(choice[0])][int(choice[1])] = ChoiceTemp
                        self.Counter += 1
            except:
                print('ERROR!')

class Player(object):
    def __init__(self,char):
        self.Char = char
    def Play(self,table):
        while True:
            choice = str(input('your turn :'))
            if table[int(choice[0]) - 1][int(choice[1]) - 1] == '-':
                return choice
            else:
                print('ERROR!')

class CPU(object):
    def __init__(self,char,playerchar,game):
        self.PlayerChar = playerchar
        self.Char = char
        self.Game = game
    def Play(self):
        is_done = False
        if self.Game.Counter <= 1:
            if randint(0,1):
                if self.Game.Table[1][1] == '-':
                    is_done = True
                    return '11'
                else:
                    while not is_done:
                        tmp = choice(['00', '22', '02', '20'])
                        if self.Game.Table[int(tmp[0])][int(tmp[1])] == '-':
                            is_done = True
                            return tmp
            else:
                while not is_done:
                    tmp = choice(['00', '22', '02', '20'])
                    if self.Game.Table[int(tmp[0])][int(tmp[1])] == '-':
                      is_done = True
                      return tmp
        elif self.Game.Counter >= 2 and self.Game.Counter <= 3:
            while not is_done:
                tmp = choice(['00', '22', '02', '20'])
                if self.Game.Table[int(tmp[0])][int(tmp[1])] == '-':
                    is_done = True
                    return tmp
        elif self.Game.Counter >= 4:
            for i in self.Game.Table:
                if i.count(self.PlayerChar) == 2 and i.count('-') == 1:
                    is_done = True
                    return str(self.Game.Table.index(i)+(i.index('-')))
                elif i.count(self.Char) == 2 and i.count('-') == 1:
                    is_done = True
                    return str(self.Game.Table.index(i)+(i.index('-')))
            if not is_done:
                for i in range(3):
                    tmp = [j[i] for j in self.Game.Table]
                    if tmp.count(self.PlayerChar) == 2 and tmp.count('-') == 1:
                        is_done = True
                        return str(tmp.index('-'))+str(int(str(tmp[tmp.index('-')])[1])-1)
                    elif tmp.count(self.Char) == 2 and tmp.count('-') == 1:
                        is_done = True
                        return str(tmp.index('-'))+str(int(str(tmp[tmp.index('-')])[1])-1)
                        ### to be to be continued...
