from subprocess import call
### to clean the terminal.
from time import sleep
### too show the winner.

### so let's play!
class Game(object):

    def __init__(self):
### maybe the players wanted to know about their score!
    	self.SCOREBOARD = {'X': int(), 'O': int()}
#### and that's how I decide who's turn is it to play.
    	self.COUNTER = int()

### so we want a table to play on it;
### how are you going to draw it?!
    def set_table(self):
        self.TABLE = [['-' for i in range(3)] for j in range(3)]    

### also you should be able to show it to the people.
    def display_table(self):
        call('clear', shell=True)
### now the terimnal is clean af!
        print('X: {}'.format(self.SCOREBOARD['X']), end=' - ')
        print('O: {}'.format(self.SCOREBOARD['O']))
        print('\n')
        for i in self.TABLE:
            for j in i:
                print(j, end='    ')
            print('\n')
        
### let's see if any of players wins.
    def check_the_table(self):
        win = False
### did anybody win?!
### analyzing horizental & vertical lines: {
        if not win:
            for i in self.TABLE:
                if i.count(i[0]) == 3:
                    if i[0] == 'X' or i[0] == 'O':
                        win = True
                        self.SCOREBOARD[i[0]] += 1
                        self.display_table()
                        print('{} won the game!'.format(i[0]))
                        self.set_table()
                        sleep(2)
        if not win:
            for i in range(3):
                tmp = list()
                for j in self.TABLE:
                    tmp.append(j[i])
                    if tmp.count(tmp[0]) == 3:
                        if tmp[0] == 'X' or tmp[0] == 'O':
                            win = True
                            self.SCOREBOARD[tmp[0]] += 1
                            self.display_table()
                            print('{} won the game!'.format(tmp[0]))
                            self.set_table()
                            sleep(2)
### }
### analyzing X lines{
        if not win:
            tmp = [self.TABLE[i][i] for i in range(3)]
            if tmp.count(tmp[0]) == 3:
                if tmp[0] == 'X' or tmp[0] == 'O':
                    win = True
                    self.SCOREBOARD[tmp[0]] += 1
                    self.display_table()
                    print('{} won the game!'.format(tmp[0]))
                    self.set_table()
                    sleep(2)
        if not win:
            tmp = [self.TABLE[0][2], self.TABLE[1][1], self.TABLE[2][0]]
            if tmp.count(tmp[0]) == 3:
                if tmp[0] == 'X' or tmp[0] == 'O':
                    win = True
                    self.SCOREBOARD[tmp[0]] += 1
                    self.display_table()
                    print('{} won the game!'.format(tmp[0]))
                    self.set_table()
                    sleep(2)
### }
