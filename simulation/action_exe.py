class Action_executer():
    def __init__(self, producer, receiver, ini_pos, end_pos, action_type, simulator) -> None:
        self.producer = producer
        self.receiver = receiver
        self.ini_pos = ini_pos
        self.end_pos = end_pos
        self.action_type = action_type
        self.simulator = simulator
    
    def make_action(self, board):
        if self.action_type == "movement":
            self.move(board)
        elif self.action_type == "attack":
            self.attack(board)
            
    def move(self, board):
        board.get_cell(self.ini_pos).set_unit(None)
        board.get_cell(self.end_pos).set_unit(self.producer)
        self.producer.set_pos(self.end_pos)
        
    def attack(self, board):
        receiver = board.get_cell(self.end_pos).get_unit()
        receiver.set_hp(receiver.get_hp() - self.calculate_damage(self.producer.get_attack()))
        if receiver.get_hp() <= 0:
            board.get_cell(self.end_pos).set_unit(None)
            board.get_units().remove(receiver)
    
    def calculate_damage(self, basic):
        return self.simulator.calculate_damage(basic, self.ini_pos, self.end_pos)
        
    
    