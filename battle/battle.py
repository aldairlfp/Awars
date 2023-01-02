from unit import *
from state import *
from field import *


class Battle:
    """A battle is similar to a problem, but it has a terminal test instead of 
    a goal test, and a utility for each terminal state. To create a battle, 
    subclass this class and implement `actions`, `result`, `is_terminal`, 
    and `utility`. You will also need to set the .initial attribute to the 
    initial state; this can be done in the constructor."""

    def __init__(self, field: Field):
        """Specify the initial state."""
        self._field = field
        self._units = {}
        self._units_count = 0

    def add_unit(self, unit: Unit):
        self._units_count += 1
        self._units[unit.get_posx(), unit.get_posy()] = unit

    def move_unit(self, unit: Unit, x: int, y: int):
        if (x, y) in self._field:
            return False
        else:
            del self._units[unit.get_posx(), unit.get_posy()]
            self._units[x, y] = unit
            return True

    def remove_unit(self, unit: Unit):
        self._units_count -= 1
        self._units[unit.get_posx(), unit.get_posy()] = None

    def get_unit(self, x: int, y: int):
        return self._units[x, y]

    def get_units(self):
        return self._units

    def get_units_count(self):
        return self._units_count

    def get_field(self):
        return self._field

    def get_field_size(self):
        return self._field.get_size()

    def get_field_cell(self, x: int, y: int):
        return self._field.get_cell(x, y)

    def get_field_cells(self):
        return self._field.get_cells()

    def step_foward(self):
        all_steps = []
        for pos in self._units:
            if self._units[pos].get_alive():
                x, y = self._units[pos].step_foward()
                all_steps.append((pos, (x, y)))
        return all_steps

    def one_frame(self):
        all_steps = self.step_foward()
        for step in all_steps:
            self.move_unit(self.get_unit(step[0][0], step[0][1]), step[1][0], step[1][1])

    def __str__(self):
        """Return a string representation of the battle."""
        s = ""
        for i in range(self._field.get_width()):
            for j in range(self._field.get_height()):
                if (i, j) in self._units:
                    if self._units[i, j].get_alive():
                        if self._units[i, j] is Soldier:
                            s += "S    "
                        else:
                            s += "U    "
                    else:
                        s += "X    "
                else:
                    s += ".    "
            s += "\n"
        return s
