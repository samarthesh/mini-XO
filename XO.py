from subprocess import call
class Game():
    Row = list()
    Wn = [0,0]
    def FT():
        Game.Counter = 0
        Game.Row = list()
        for i in range(0,3):
            Game.Row.append(list())
        for i in Game.Row:
            for a in range(0,3):
                i.append('-')
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
            if int(InP[0]) >= 1 and int(InP[0]) <= 3 and int(InP[1]) >= 1 and int(InP[1]) <= 3:
                if Game.Row[int(InP[0])-1][int(InP[1])-1] == '-':
                    Game.Row[int(InP[0])-1][int(InP[1])-1] = 'X'
                    Game.Counter += 1
                else:
                    pass
            else:
                pass
        else:
            InP = input('O\'s turn \nRowColumn :')
            if int(InP[0]) >= 1 and int(InP[0]) <= 3 and int(InP[1]) >= 1 and int(InP[1]) <= 3:
                if Game.Row[int(InP[0])-1][int(InP[1])-1] == '-':
                    Game.Row[int(InP[0])-1][int(InP[1])-1] = 'O'
                    Game.Counter += 1
                else:
                    pass
            else:
                pass
    def Chck():
        if Game.Row[0][0] == Game.Row[0][1] and Game.Row[0][1] == Game.Row[0][2]:
            if Game.Row[0][2] != '-':
                print('%s won the game !' %Game.Row[0][2])
                if Game.Row[0][2] == 'O':
                    Game.Wn[0] += 1
                else:
                    Game.Wn[1] += 1
                Game.ST()
                Game.FT()
                Game.Counter = 0
        if Game.Row[0][0] == Game.Row[1][0] and Game.Row[1][0] == Game.Row[2][0]:
            if Game.Row[2][0] != '-':
                print('%s won the game !' %Game.Row[2][0])
                if Game.Row[2][0] == 'O':
                    Game.Wn[0] += 1
                else:
                    Game.Wn[1] += 1
                Game.ST()
                Game.FT()
                Game.Counter = 0
        if Game.Row[1][0] == Game.Row[1][1] and Game.Row[1][1] == Game.Row[1][2]:
            if Game.Row[1][2] != '-':
                print('%s won the game !' %Game.Row[1][2])
                if Game.Row[1][2] == 'O':
                    Game.Wn[0] += 1
                else:
                    Game.Wn[1] += 1
                Game.ST()
                Game.FT()
                Game.Counter = 0
        if Game.Row[2][0] == Game.Row[2][1] and Game.Row[2][1] == Game.Row[2][2]:
            if Game.Row[2][2] != '-':
                print('%s won the game !' %Game.Row[2][2])
                if Game.Row[2][2] == 'O':
                    Game.Wn[0] += 1
                else:
                    Game.Wn[1] += 1
                Game.ST()
                Game.FT()
                Game.Counter = 0
        if Game.Row[0][1] == Game.Row[1][1] and Game.Row[1][1] == Game.Row[2][1]:
            if Game.Row[2][1] != '-':
                print('%s won the game !' %Game.Row[2][1])
                if Game.Row[2][1] == 'O':
                    Game.Wn[0] += 1
                else:
                    Game.Wn[1] += 1
                Game.ST()
                Game.FT()
                Game.Counter = 0
        if Game.Row[0][2] == Game.Row[1][2] and Game.Row[1][2] == Game.Row[2][2]:
            if Game.Row[2][2] != '-':
                print('%s won the game !' %Game.Row[2][2])
                if Game.Row[2][2] == 'O':
                    Game.Wn[0] += 1
                else:
                    Game.Wn[1] += 1
                Game.ST()
                Game.FT()
                Game.Counter = 0
        if Game.Row[0][0] == Game.Row[1][1] and Game.Row[1][1] == Game.Row[2][2]:
            if Game.Row[2][2] != '-':
                print('%s won the game !' %Game.Row[2][2])
                if Game.Row[2][2] == 'O':
                    Game.Wn[0] += 1
                else:
                    Game.Wn[1] += 1
                Game.ST()
                Game.FT()
                Game.Counter = 0
        if Game.Row[0][2] == Game.Row[1][1] and Game.Row[1][1] == Game.Row[2][0]:
            if Game.Row[2][0] != '-':
                print('%s won the game !' %Game.Row[2][0])
                if Game.Row[2][0] == 'O':
                    Game.Wn[0] += 1
                else:
                    Game.Wn[1] += 1
                Game.ST()
                Game.FT()
                Game.Counter = 0
# Enough coding , let's play ! :)
while True:
    Game.FT()
    while Game.Counter < 9:
        if Game.Counter <= 8:
            Game.play()
            Game.Chck()
