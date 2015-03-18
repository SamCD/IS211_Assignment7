import random
import sys

random.seed(0)
class Player(object):


    def __init__(self,name):

        self.name = name
        self.score = 0
        self.Turn = False
        self.rolls = []
        self.status = 0
        

class Die(object):

    
    def __init__(self):
        self.showing = 0


    def roll(self):

        self.showing = random.randint(1,6)
        return self.showing


class Game(object):


    def __init__(self,player1,player2):

        self.Player1 = Player(player1)
        self.Player2 = Player(player2)
        self.die = Die()
        self.winner = ''
        self.turn(self.Player1)


    def switch(self):

        if self.Player1.Turn == True:
            self.Player1.Turn = False
            self.turn(self.Player2)

        if self.Player2.Turn == True:
            self.Player2.Turn = False
            self.turn(self.Player1)


    def turn(self,player):
        player.Turn = True
        while player.Turn == True and player.score < 100:
            choice = raw_input('{}, Hold or Roll? (h/r): '.format(
                                                            player.name))
            if choice[0].lower() == 'r':
                player.status = self.die.roll()
                if player.status == 1:
                    player.rolls = []
                    self.switch()
                else:
                    player.rolls.append(player.status)
                print 'Roll: {}, Turn total: {}, ' \
                    'Game total: {}'.format(
                            player.status,sum(player.rolls),
                            player.score + sum(player.rolls))

            if choice[0].lower() == 'h':
                player.score += sum(player.rolls)
                if player.score >= 100:
                    self.winner = player.name
                    self.game_over()
                player.rolls = []
                print '{} current score: {}'.format(player.name,player.score)
                self.switch()

                
    def game_over(self):

        print '{} is the winner'.format(self.winner)
        sys.exit()
