import field
import unit
import battle

field1 = field.Field()
battle = battle.Battle(field1)
battle.add_unit(unit.Soldier(1, 1))
battle.add_unit(unit.Soldier(1, 2))
battle.add_unit(unit.Soldier(1, 3))

for i in range(10):
    battle.one_frame()
    print(battle)

# field1.move_soldier(field1.soldiers[1, 2], 2, 1)
# print(field1)
