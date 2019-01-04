#!/usr/bin/python3
from random import randint, choice
from subprocess import call
from time import sleep
class Game():
    CpTemp = str()
    CpChar = str()
    PlChar = str()
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
                if len(InP) == 2:
                    if int(InP[0]) >= 1 and int(InP[0]) <= 3 and int(InP[1]) >= 1 and int(InP[1]) <= 3:
                        if Game.Row[int(InP[0])-1][int(InP[1])-1] == '-':
                            Game.Row[int(InP[0])-1][int(InP[1])-1] = 'X'
                            Game.Counter += 1
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            except ValueError:
                pass
        else:
            InP = input('O\'s turn \nRowColumn :')
            try:
                if len(InP) == 2:
                    if int(InP[0]) >= 1 and int(InP[0]) <= 3 and int(InP[1]) >= 1 and int(InP[1]) <= 3:
                        if Game.Row[int(InP[0])-1][int(InP[1])-1] == '-':
                            Game.Row[int(InP[0])-1][int(InP[1])-1] = 'O'
                            Game.Counter += 1
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            except ValueError:
                pass
    def Player():
        done = False
        while done == False:
            Game.ST()
            InP = input('%s\'s turn \nRowColumn :'%Game.PlChar)
            try:
                if len(InP) == 2 and int(InP[0]) >= 1 and int(InP[0]) <= 3 and int(InP[1]) >= 1 and int(InP[1]) <= 3:
                    if Game.Row[int(InP[0])-1][int(InP[1])-1] == '-':
                        Game.Row[int(InP[0])-1][int(InP[1])-1] = Game.PlChar
                        Game.Counter += 1
                        done = True
                    else:
                        pass
                else:
                    pass
            except ValueError:
                pass
    def CPU():
        Temper = Game.CpTemp
        if Game.Counter <= 1:
            Temp = randint(0,1)
            if Temp == 0:
                if Game.Row[1][1] == '-':
                    Game.CpTemp = '11'
                if Game.Row[1][1] != '-':
                    pass
            elif Temp == 1 or Game.Row[1][1] != '-':
                Game.CpTemp = choice (['00','02','20','22'])
                while Game.Row[int(Game.CpTemp[0])][int(Game.CpTemp[1])] != '-':
                    Game.CpTemp = choice (['00','02','20','22'])
        elif Game.Counter >= 2:
            if Temper == Game.CpTemp:
                for i in Game.Row:
                    if i[0] == i[1] and i[0] != '-':
                        if i[2] == '-':
                            Game.CpTemp = str(Game.Row.index(i))+'2'
                            break
                    elif i[0] == i[2] and i[0] != '-':
                        if i[1] == '-':
                            Game.CpTemp = str(Game.Row.index(i))+'1'
                            break
                    elif i[1] == i[2] and i[1] != '-':
                        if i[0] == '-':
                            Game.CpTemp = str(Game.Row.index(i))+'0'
                            break
            if Temper == Game.CpTemp:
                for i in range(3):
                    if Game.Row[0][i] == Game.Row[1][i] and Game.Row[0][i] != '-':
                        if Game.Row[2][i] == '-':
                            Game.CpTemp = '2'+str(i)
                            break
                    elif Game.Row[0][i] == Game.Row[2][i] and Game.Row[0][i] != '-':
                        if Game.Row[1][i] == '-':
                            Game.CpTemp = '1'+str(i)
                            break
                    elif Game.Row[1][i] == Game.Row[2][i] and Game.Row[1][i] != '-':
                        if Game.Row[0][i] == '-':
                            Game.CpTemp = '0'+str(i)
                            break
            if Temper == Game.CpTemp:
                if Game.Row[0][0] == Game.Row[1][1] and Game.Row[0][0] != '-':
                    if Game.Row[2][2] == '-':
                        Game.CpTemp = '22'
            if Temper == Game.CpTemp:
                if Game.Row[0][0] == Game.Row[2][2] and Game.Row[0][0] != '-':
                    if Game.Row[1][1] == '-':
                        Game.CpTemp = '11'
            if Temper == Game.CpTemp:
                if Game.Row[1][1] == Game.Row[2][2] and Game.Row[1][1] != '-':
                    if Game.Row[0][0] == '-':
                        Game.CpTemp = '00'
            if Temper == Game.CpTemp:
                if Game.Row[0][2] == Game.Row[1][1] and Game.Row[0][2] != '-':
                    if Game.Row[2][0] == '-':
                        Game.CpTemp = '20'
            if Temper == Game.CpTemp:
                if Game.Row[0][2] == Game.Row[2][0] and Game.Row[0][2] != '-':
                    if Game.Row[1][1] == '-':
                        Game.CpTemp = '11'
            if Temper == Game.CpTemp:
                if Game.Row[1][1] == Game.Row[2][0] and Game.Row[1][1] != '-':
                    if Game.Row[0][2] == '-':
                        Game.CpTemp = '02'
            if Temper == Game.CpTemp:
                while Game.Row[int(Game.CpTemp[0])][int(Game.CpTemp[1])] != '-':
                    for i in range(3):
                        for j in range(3):
                            if Game.Row[i][j] == '-':
                                Game.CpTemp = str(i)+str(j)
                                break
                            break
        Game.Row[int(Game.CpTemp[0])][int(Game.CpTemp[1])] = Game.CpChar
        Game.Counter += 1
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
tmp = call('clear',shell=True)
while True:
    newGame = int(input('1.Multi mode \n2.Single mode\nYour Choice :'))
    if newGame == 1:
        while True:
            Game.FT()
            while Game.Counter < 9:
                if Game.Counter <= 8:
                    Game.play()
                    Game.Chck()
    elif newGame == 2:
        while True:
            Temper = int(input('1.X \n2.O \nChoose your Char :'))
            if Temper == 1:
                Game.PlChar = 'X'
                Game.CpChar = 'O'
                break
            elif Temper == 2:
                Game.PlChar = 'O'
                Game.CpChar = 'X'
                break
            else:
                print('WRONG OPTION!')
        while True:
            Game.FT()
            while Game.Counter < 9:
                if Game.Counter <= 8:
                    Game.CPU()
                    Game.Chck()
                    Game.Player()
                    Game.Chck()

    else:
        print('WRONG OPTION!')
