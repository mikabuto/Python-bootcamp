from collections import Counter
import random
 
 
class Player:
    _instance = None
 
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
 
    def __init__(self):
        self.last_response = -1
        self.name = ""
 
    @staticmethod
    def cooperate():
        return 1
 
    @staticmethod
    def cheat():
        return 0
 
    def strategy(self, other):
        # Abstract
        pass
 
 
class Cheater(Player):
    def __init__(self):
        super(Cheater, self).__init__()
        self.name = "cheater"
 
    def strategy(self, other):
        while True:
            self.last_response = self.cheat()
            yield self.cheat()
 
 
class Cooperator(Player):
    def __init__(self):
        super(Cooperator, self).__init__()
        self.name = "cooperator"
 
    def strategy(self, other):
        while True:
            self.last_response = self.cooperate()
            yield self.cooperate()
 
 
class Copycat(Player):
    def __init__(self):
        super(Copycat, self).__init__()
        self.name = "copycat"
 
    def strategy(self, other: Player):
        while True:
            if other.last_response == -1:
                self.last_response = self.cooperate()
            else:
                self.last_response = other.last_response
            yield self.last_response
 
 
class Grudger(Player):
    def __init__(self):
        super(Grudger, self).__init__()
        self.evil = False
        self.name = "grudger"
 
    def strategy(self, other: Player):
        while True:
            if self.evil:
                self.last_response = self.cheat()
            elif other.last_response == self.cheat():
                self.evil = True
                self.last_response = self.cheat()
            else:
                self.last_response = self.cooperate()
            yield self.last_response
 
 
class Detective(Player):
    def __init__(self):
        super(Detective, self).__init__()
        self.name = "detective"
        self.evil = False
 
    def strategy(self, other: Player):
        for func in [self.cooperate, self.cheat, self.cooperate, self.cheat]:
            if other.last_response == self.cheat():
                self.evil = True
            self.last_response = func()
            yield self.last_response
        while True:
            if self.evil:
                self.last_response = other.last_response
            else:
                self.last_response = self.cheat()
            yield self.last_response
 
 
class Random(Player):
    def __init__(self):
        super(Random, self).__init__()
        self.name = "random"
        self.evil = False
 
    def strategy(self, other: Player):
        while True:
            self.last_response = random.randint(0, 2)
            yield self.last_response
 
 
class Myclass(Player):
    def __init__(self):
        super(Myclass, self).__init__()
        self.name = "myclass"
 
    def strategy(self, other: Player):
        while True:
            if other.last_response == -1:
                self.last_response = self.cheat()
            else:
                self.last_response = other.last_response
            yield self.last_response
 
 
class Game(object):
    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()
 
    def play(self, player1, player2):
        gen1 = player1.strategy(player2)
        gen2 = player2.strategy(player1)
        for _ in range(self.matches):
            resp1 = next(gen1)
            resp2 = next(gen2)
            if resp1 == resp2 == 1:
                self.registry += Counter({player1.name: 2, player2.name: 2})
            elif resp1 == 0:
                self.registry += Counter({player1.name: 3, player2.name: -1})
            elif resp2 == 0:
                self.registry += Counter({player1.name: -1, player2.name: 3})
 
    def top3(self):
        players = [Myclass(), Grudger(), Copycat(), Detective(), Cheater(), Cooperator(), Random()]
        for num1 in range(len(players) - 1):
            for num2 in range(num1 + 1, len(players)):
                self.play(players[num1], players[num2])
        [print(*line) for line in self.registry.most_common(5)]
 
 
game = Game()
game.top3()