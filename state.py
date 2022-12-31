from simulation.unit import *

class State:
    """State of the battle, the position of all units and more"""
    def __init__(self, rows:int=10, cols:int=10, units:list=[Unit('1', 1, 1, None)]) -> None:
        self._rows = rows
        self._cols = cols
        self._units = units
        self._map = [[None for _ in range(cols)] for _ in range(rows)]
        self._turn = units[0]#TODO: end this

    def add_unit(self, unit:Unit) -> None:
        """Add a unit to the state"""
        self._units.append(unit)
        self._map[unit.get_posx()][unit.get_posy()] = unit

    def move_unit(self, unit:Unit, row:int, col:int) -> None:
        """Move a unit to a new position"""
        self._map[unit.get_posx()][unit.get_posy()] = None
        self._map[row][col] = unit
        unit.set_posx(row)
        unit.set_posy(col)

    def remove_unit(self, unit:Unit) -> None:
        """Remove a unit from the state"""
        self._units.remove(unit)
        self._map[unit.get_posx][unit.get_posy] = None

    def get_unit(self, row:int, col:int) -> Unit:
        """Get the unit at a position"""
        return self._map[row][col]

    def get_units(self) -> list[Unit]:
        """Get all units"""
        return self._units