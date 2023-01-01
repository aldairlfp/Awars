import simulation.simulation as simulation
import simulation.board as board
from simulation.unit import Normal_generator, Random_allocator
from simulation.map_types import Basic_map
from algoritms.strategies.strategies import Random_strategy
from simulation.modes import Normal_mode


if __name__ == "__main__":
    sim = simulation.Simulator(Normal_mode(), 10)
    strategies = {"random": Random_strategy(None)}
    units = []
    
    for i in range(5):
        gen = Normal_generator(i, "random", "blue")
        unit = gen.generate_unit()
        unit.set_strategies(strategies)
        units.append(unit)
        
    for i in range(5):
        gen = Normal_generator(i, "random", "red")
        unit = gen.generate_unit()
        unit.set_strategies(strategies)
        units.append(unit)
        
    sim.se
        
    terrain = board.Board(50, 50, Basic_map(50, 50), Random_allocator(strategies, None))
    terrain.create_map()
    terrain.allocate_units()
    sim.execute()