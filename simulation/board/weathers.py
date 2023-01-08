class Weather():
    def __init__(self):
        self._name = None
        self._temperature = None
        self._precipitation = None
        self._modifiers = None
    
    def get_name(self):
        return self._name
    
    def get_temperature(self):
        return self._temperature
    
    def get_precipitation(self):
        return self._precipitation
        
    def get_modifiers(self):
        return self._modifiers
    
    def __str__(self):
        return f"{self._name}"
        
    def __getitem__(self, key):
        try:
            return self._modifiers[key]
        except KeyError:
            print(f"The weather don't have {key} modifier")
            return 1
        
class Sunny(Weather):
    def __init__(self):
        self._name = "sunny"
        self._temperature = 24
        self._precipitation = 0
        self._modifiers = {"attack": 1, "defense": 1, "speed": 1, "accuracy": 1}

class Foggy(Weather):
    def __init__(self):
        self._name = "foggy"
        self._temperature = 20
        self._precipitation = 10
        self._modifiers = {"attack": 0.9, "defense": 1, "speed": 0.9, "accuracy": 0.8}

class Raining(Weather):
    def __init__(self):
        self._name = 'raining'
        self._temperature = 18
        self._precipitation = 80
        self._modifiers = {"attack": 0.8, "defense": 1, "speed": 0.6, "accuracy": 0.7}
        
class Snowing(Weather):
    def __init__(self):
        self._name = 'snowing'
        self._temperature = -10
        self._precipitation = 100
        self._modifiers = {"attack": 1, "defense": 0.7, "speed": 0.5, "accuracy": 0.8}