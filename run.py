import simulation.simulation as simulation
from simulation.Units.unit_generator import *
from simulation.Units.units_allocator import random_allocator
from algoritms.strategies.strategies import *
from simulation.modes import Normal_mode, Hard_mode


if __name__ == "__main__":
    sim = simulation.Simulator(Hard_mode(), 1000)
    units = []
    
    sim.board(10, 10)
    
    sim.units(archer_b_unit, 5, 'red', 'hard')
    sim.units(archer_c_unit, 5, 'red', 'hard')
    sim.units(swordman_unit, 5, 'red', 'hard')
    sim.units(spearman_unit, 5, 'red', 'hard')
    
    
    for unit in sim.unit()[:20]:
        unit.strategy('hard', Hard_fuzzy_strategy(unit))
        
    sim.units(archer_b_unit, 5, 'blue', 'hard')
    sim.units(archer_c_unit, 5, 'blue', 'hard')
    sim.units(swordman_unit, 5, 'blue', 'hard')
    sim.units(spearman_unit, 5, 'blue', 'hard')
    
    for unit in sim.unit()[20:]:
        unit.strategy('hard', Hard_fuzzy_strategy(unit))
    
    sim.allocate_units(random_allocator, sim.unit())
    
    sim.execute()