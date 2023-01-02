class Action_executer():
    def __init__(self, producer, receiver, ini_pos, end_pos, action_type) -> None:
        self.producer = producer
        self.receiver = receiver
        self.ini_pos = ini_pos
        self.end_pos = end_pos
        self.action_type = action_type
    
    def make_action(self, board):
        if self.action_type == "movement":
            self.move(board)
        elif self.action_type == "attack":
            self.attack(board)
            
    def move(self, board):
        board.cell(self.ini_pos).unit(None)
        board.cell(self.end_pos).unit(self.producer)
        self.producer.pos(self.end_pos)
        
    def attack(self, board):
        receiver = board.cell(self.end_pos).unit()
        receiver.hp(receiver.hp() - self.calculate_damage(self.producer.attack()))
        if receiver.hp() <= 0:
            board.cell(self.end_pos).unit(None)
            board.units().remove(receiver)
    
    def calculate_damage(self, basic, damage_calculator):
        return damage_calculator(basic, self.ini_pos, self.end_pos)
        
    
    