def move_evaluator(unit_attack, defense, accuracy, enemy_unit_attack, approach):
    "Return an unit's movent evaluation."
   
    # unit_attack = ['melee', 'distant']
    if unit_attack == 'melee':
        unit_attack_value = 'a'
    elif unit_attack == 'distance':
        unit_attack_value = 'b'
    else:
        pass        # todo option

    # enemy_unit_attack = ['face to face', 'distant']
    if enemy_unit_attack == 'melee':
        enemy_unit_attack_value = 'a'
    elif enemy_unit_attack == 'distance':
        enemy_unit_attack_value = 'b'
    else:
        pass        # todo option

    # -defense[low, high]
    if defense == 'low':
        defense_value = '1'
    elif defense == 'high':
        defense_value = '2'
    else:
        pass        # todo option

    # -accuracy[low, high]
    if accuracy == 'low':
        accuracy_value = '1'
    elif accuracy == 'high':
        accuracy_value = '2'
    else:
        pass        # todo option

    # -enemy_unit_attack[melee, distant]
    if enemy_unit_attack == 'melee':
        enemy_unit_attack_value = 'a'
    elif enemy_unit_attack == 'distance':
        enemy_unit_attack_value = 'b'
    else:
        pass        # todo option

    # proximity_to_enemy
    if approach < 3:
        prox_value = str(approach)
    elif approach >= 3:
        prox_value = '3'
    else:
        pass        # todo option

    unit_value = unit_attack_value + defense_value + accuracy_value + prox_value + enemy_unit_attack_value

    very_bad = ['b111a', 'b121a', 'b211a', 'b221a']
    bad = ['a111a', 'a121a', 'a212b', 'a112b', 'a122b',
           'a222b', 'b112b', 'b212b']
    middle = ['a112a', 'a122a', 'a211a', 'a221a', 'b112a',
              'b111b', 'b121b', 'b122b', 'b211b', 'b223a',
              'b221b', 'b222b']
    good = ['a113a', 'a123a', 'a212a', 'a213a', 'a222a',
            'a223a', 'b113a', 'a113b', 'a123b', 'a213b',
            'a223b', 'b122a', 'b123b', 'b212a', 'b222a',
            'b213b', 'b223b']
    very_good = ['a111b', 'a211b', 'a121b', 'a221b', 'b113b',
                 'b123a', 'b213a']

    value = 0
    if unit_value in very_bad:
        value = 2
    elif unit_value in bad:
        value = 4
    elif unit_value in middle:
        value = 6
    elif unit_value in good:
        value = 8
    elif unit_value in very_good:
        value = 10
    else:
        value = value

    return value
