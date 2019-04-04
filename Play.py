from time import sleep
### to show the errors!

### we can't play without players, you know?!
class Player(object):

### every player has their own cahr(X, O), and their own game.(which table am I playing on!)
    def __init__(self, char, game):
        self.CHAR = char[0]
        self._game = game

    @property
    def GAME(self):
        return self._game
### now you have access to the orriginal table whenever it changes.

### so we have our game, table and our players; let's play!
    def play(self):
        is_done = False
        while not is_done:
            self.GAME.display_table()
            tmp = input('{}s turn: '.format(self.CHAR))
            try:
                if self.GAME.TABLE[int(tmp[0])-1][int(tmp[1]) - 1] == '-' and len(tmp) == 2:
                    self.GAME.TABLE[int(tmp[0])-1][int(tmp[1]) -1] = self.CHAR
                    self.GAME.COUNTER += 1
                    is_done = True
                else:
                    print('--!ERROR!--')
                    sleep(2)
            except:
                print('--!ERROR!--')
                sleep(2)