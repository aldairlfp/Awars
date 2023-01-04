import simulation.simulation as simulation
from simulation.Units.unit_generator import normal_unit
from simulation.Units.units_allocator import random_allocator
from algoritms.strategies.strategies import *
from simulation.modes import Normal_mode


if __name__ == "__main__":
    sim = simulation.Simulator(Normal_mode(), 1000)
    strategies = {"random": Random_strategy()}
    units = []
    
    sim.board(10, 10)
    
    sim.units(normal_unit, 5, 'red', 'advanced')
    
    for unit in sim.unit()[:5]:
        unit.strategy('advanced', Advanced_strategy(unit, sim.board_s()))
        
    sim.units(normal_unit, 5, 'blue', 'advanced')
    
    for unit in sim.unit()[5:]:
        unit.strategy('advanced', Advanced_strategy(unit, sim.board_s()))
    
    sim.allocate_units(random_allocator, sim.unit())
    
    sim.execute()