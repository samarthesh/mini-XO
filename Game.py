from subprocess import call
### to clean the terminal.
from time import sleep
### too show the winner.

### so let's play!
class Game(object):

    def __init__(self, X='X', O='O'):
### I let you use your favorite char. :)
        self.OCHAR = O
        self.XCHAR = X
### maybe the players wanted to know about their score!
        self.SCOREBOARD = {self.XCHAR: int(), self.OCHAR: int()}

### so we want a table to play on it;
### how are you going to draw it?!
    def set_table(self):
        self.TABLE = [['-' for i in range(3)] for j in range(3)] 
        self.COUNTER = 0   

### also you should be able to show it to the people.
    def display_table(self):
        call('clear', shell=True)
### now the terimnal is clean af!
        print('{}: {}'.format(self.XCHAR, self.SCOREBOARD[self.XCHAR]), end=' - ')
        print('{}: {}'.format(self.OCHAR, self.SCOREBOARD[self.OCHAR]))
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
                    if i[0] != '-':
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
                        if tmp[0] != '-':
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
                if tmp[0] != '-':
                    win = True
                    self.SCOREBOARD[tmp[0]] += 1
                    self.display_table()
                    print('{} won the game!'.format(tmp[0]))
                    self.set_table()
                    sleep(2)
        if not win:
            tmp = [self.TABLE[0][2], self.TABLE[1][1], self.TABLE[2][0]]
            if tmp.count(tmp[0]) == 3:
                if tmp[0] != '-':
                    win = True
                    self.SCOREBOARD[tmp[0]] += 1
                    self.display_table()
                    print('{} won the game!'.format(tmp[0]))
                    self.set_table()
                    sleep(2)
### }
### what if nobody couldn't win!?
        if not win:
            if self.COUNTER >= 9:
                win = True
                self.display_table()
                print('no one won the game!')
                self.set_table
                sleep(2)
