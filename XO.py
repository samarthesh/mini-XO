#!/usr/bin/python3
from subprocess import call
from time import sleep
class Game():
    Row = list()
    Wn = [0,0]
    def FT():
        Game.Counter = 0
        Game.Row = [['-' for i in range(3)] for j in range(3)]
    def ST():
        tmp = call('clear',shell=True)
        print('O : %i | X : %i' %(Game.Wn[0],Game.Wn[1]))
        print ('* * * * * * *')
        for i in Game.Row:
            for j in i:
                print(j,end='    ')
            print('\n')
        print ('* * * * * * *')
    def play():
        Game.ST()
        if Game.Counter%2 == 0:
            InP = input('X\'s turn \nRowColumn :')
            try:
                if int(InP[0]) >= 1 and int(InP[0]) <= 3 and int(InP[1]) >= 1 and int(InP[1]) <= 3:
                    if Game.Row[int(InP[0])-1][int(InP[1])-1] == '-':
                        Game.Row[int(InP[0])-1][int(InP[1])-1] = 'X'
                        Game.Counter += 1
                    else:
                        pass
                else:
                    pass
            except ValueError:
                pass
        else:
            InP = input('O\'s turn \nRowColumn :')
            try:
                if int(InP[0]) >= 1 and int(InP[0]) <= 3 and int(InP[1]) >= 1 and int(InP[1]) <= 3:
                    if Game.Row[int(InP[0])-1][int(InP[1])-1] == '-':
                        Game.Row[int(InP[0])-1][int(InP[1])-1] = 'O'
                        Game.Counter += 1
                    else:
                        pass
                else:
                    pass
            except ValueError:
                pass
    def Chck():
        Win = False
        for i in Game.Row:
            if i[0] == i[1] and i[1] == i[2] and i[2] != '-':
                if i[2] == 'O':
                    Game.Wn[0] += 1
                else:
                    Game.Wn[1] += 1
                Game.ST()
                print('%s won the game !' %i[2])
                sleep(2)
                Game.FT()
                Game.Counter = 0
                Win = True
            else:
                pass
        for i in range(3):
            if Game.Row[0][i] == Game.Row[1][i] and Game.Row[1][i] == Game.Row[2][i] and Game.Row[2][i] != '-':
                if Game.Row[2][i] == 'O':
                    Game.Wn[0] += 1
                else:
                    Game.Wn[1] += 1
                Game.ST()
                print('%s won the game !' %Game.Row[2][i])
                sleep(2)
                Game.FT()
                Game.Counter = 0
                Win = True
            else:
                pass
        if Game.Row[0][0] == Game.Row[1][1] and Game.Row[1][1] == Game.Row[2][2] and Game.Row[2][2] != '-':
            if Game.Row[2][2] == 'O':
                Game.Wn[0] += 1
            else:
                Game.Wn[1] += 1
            Game.ST()
            print('%s won the game !' %Game.Row[2][2])
            sleep(2)
            Game.FT()
            Game.Counter = 0
            Win = True
        else:
            pass
        if Game.Row[0][2] == Game.Row[1][1] and Game.Row[1][1] == Game.Row[2][0] and Game.Row[2][0] != '-':
            if Game.Row[2][0] == 'O':
                Game.Wn[0] += 1
            else:
                Game.Wn[1] += 1
            Game.ST()
            print('%s won the game !' %Game.Row[2][0])
            sleep(2)
            Game.FT()
            Game.Counter = 0
            Win = True
        else:
            pass
        if Game.Counter == 9:
            if Win == False:
                Game.ST()
                print('No one won the game !')
                sleep(2)
                Game.FT()
                Game.Counter = 0
# let's play ! 
while True:
    Game.FT()
    while Game.Counter < 9:
        if Game.Counter <= 8:
            Game.play()
            Game.Chck()
