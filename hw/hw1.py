class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1


# Создаём первого героя
hero1 = Hero(name="Артас", level=5, health=100, strength=20)

# Создаём второго героя
hero2 = Hero(name="Джайна", level=3, health=80, strength=15)

print("---- Герой 1 ----")
hero1.greet()
print(f"Сила до атаки: {hero1.strength}")
hero1.attack()
print(f"Сила после атаки: {hero1.strength}")

print(f"Здоровье до отдыха: {hero1.health}")
hero1.rest()
print(f"Здоровье после отдыха: {hero1.health}")

print("\n---- Герой 2 ----")
hero2.greet()
print(f"Сила до атаки: {hero2.strength}")
hero2.attack()
print(f"Сила после атаки: {hero2.strength}")

print(f"Здоровье до отдыха: {hero2.health}")
hero2.rest()
print(f"Здоровье после отдыха: {hero2.health}")
