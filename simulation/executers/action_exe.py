from random import random

class Action_executer():
    def __init__(self, producer, receiver, ini_pos, end_pos, action_type, damage) -> None:
        self.producer = producer
        self.receiver = receiver
        self.ini_pos = ini_pos
        self.end_pos = end_pos
        self.action_type = action_type
        self._damage = damage
    
    def make_action(self, board):
        if self.action_type == "movement":
            self.move(board)
        elif self.action_type == "attack":
            self.attack(board)
      
    def move(self, board):
        board.cell(self.ini_pos).units(None)
        board.cell(self.end_pos).units(self.producer)
        self.producer.pos(self.end_pos)
        
    def attack(self, board):
        receiver = board.cell(self.end_pos).unit()
        receiver.hp(receiver.hp_s() - self._damage)
        if receiver.hp_s() <= 0:
            board.cell(self.end_pos).units(None)
                
class Advanced_executer(Action_executer):
    def __init__(self, producer, receiver, ini_pos, end_pos, action_type, damage, accuracy, defense) -> None:
        super().__init__(producer, receiver, ini_pos, end_pos, action_type, damage)
        self._accuracy = accuracy
        self._defense = defense
        
    def make_action(self, board):
        if self.action_type == "movement":
            self.move(board)
        elif self.action_type == "attack":
            self.attack(board)
        elif self.action_type == "reload":
            self.reload(board)
    
    def reload(self):
        self.producer.weapon().reload()
        
    def attack(self, board):
        receiver = board.cell(self.end_pos).unit()
        rand = random()
        if rand < self._accuracy:
            if self._damage - self._defense > 0:
                receiver.hp(receiver.hp_s() - self._damage + self._defense)
            else:
                receiver.hp(receiver.hp_s() - 1)
            if receiver.hp_s() <= 0:
                board.cell(self.end_pos).units(None)
        