import simulation.simulation as simulation
from simulation.Units.unit_generator import normal_unit
from simulation.Units.units_allocator import random_allocator
from algoritms.strategies.strategies import Random_strategy
from simulation.modes import Normal_mode


if __name__ == "__main__":
    sim = simulation.Simulator(Normal_mode(), 10)
    strategies = {"random": Random_strategy()}
    units = []
    
    sim.units(normal_unit, 5, 'red', 'random')
    sim.units(normal_unit, 5, 'blue', 'random')
    
    sim.board(60, 60)
    
    sim.allocate_units(random_allocator, sim.unit())
    
    for unit in sim.unit():
        unit.strategy('random', Random_strategy())
    
    sim.execute()