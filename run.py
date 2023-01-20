import simulation.simulation as simulation
from simulation.Units.unit_generator import *
from simulation.Units.units_allocator import random_allocator
from algoritms.strategies.strategies import *
from simulation.modes.modes import Normal_mode, Hard_mode


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

# if __name__ == '__main__':
#     from simulation.board.chess_board import Chess_board
#     from simulation.board.maps_gen.chess_generator import chess_generator
#     from simulation.modes.chess_mode import Chess_mode
#     from algoritms.strategies.chess_strategies import Minimax_strategy
#     from simulation.units.units_allocator import chess_allocator

#     sim = simulation.Simulator(Chess_mode(), 100000000)

#     sim.board(8, 8)

#     sim.units(chess_unit, 1, 0, 'minimax')
#     sim.units(chess_unit, 1, 1, 'minimax')

#     for unit in sim.unit():
#         unit.strategy('minimax', Minimax_strategy(unit))

#     sim.allocate_units(chess_allocator, sim.unit())

#     sim.execute()
