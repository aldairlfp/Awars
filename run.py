import simulation.simulation as simulation
from simulation.Units.unit_generator import normal_unit
from simulation.Units.units_allocator import random_allocator
from algoritms.strategies.strategies import Random_strategy, Greedy_strategy, Runner_strategy
from simulation.modes import Normal_mode


if __name__ == "__main__":
    sim = simulation.Simulator(Normal_mode(), 1000)
    strategies = {"random": Random_strategy()}
    units = []
    
    sim.board(10, 10)
    
    sim.units(normal_unit, 5, 'red', 'random')
    
    sim.unit()[0].strategy('random', Random_strategy())
    sim.unit()[1].strategy('random', Runner_strategy())
    
    for unit in sim.unit()[2:5]:
        unit.strategy('random', Greedy_strategy())
        
    sim.units(normal_unit, 5, 'blue', 'random')
    
    for unit in sim.unit()[5:7]:
        unit.strategy('random', Greedy_strategy())
    
    for unit in sim.unit()[7:10]:
        unit.strategy('random', Random_strategy())
    
    sim.allocate_units(random_allocator, sim.unit())
    
    sim.execute()