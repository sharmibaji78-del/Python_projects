class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = max(0, min(100, value))

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self._name} leveled up to {self._level}!")

    def __str__(self):
        return f"Name: {self._name}\nLevel: {self._level}\nHealth: {self._health}\nMana: {self._mana}"
    
hero = GameCharacter("Kratos")
print(hero)

hero.health = 30
hero.mana = 10
print(hero)

hero.level_up()
print(hero)

