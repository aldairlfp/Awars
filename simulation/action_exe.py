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
        receiver.hp(receiver.hp() - self._damage)
        if receiver.hp() <= 0:
            board.cell(self.end_pos).units(None)
        
    
    