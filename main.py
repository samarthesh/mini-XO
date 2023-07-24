import Game, Play

def main():
    game = Game.Game(X='X', O='O')
    game.set_table()
    Xplayer = Play.Player('X', game)
    Oplayer = Play.Player('O', game)
    while True:
        Xplayer.play()
        game.check_the_table()
        Oplayer.play()
        game.check_the_table()

if __name__ == '__main__':
    main()
    
