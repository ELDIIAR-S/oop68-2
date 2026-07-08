import random


# Родительский класс
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет! Я {self.name}.")

    def attack(self):
        print(f"{self.name} атакует!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает. Здоровье: {self.health}")


# Дочерний класс Warrior
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name}: Воин атакует мечом!")


# Дочерний класс Mage
class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name}: Маг кастует заклинание!")


# Дочерний класс Assassin
class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name}: Ассасин атакует из-под тишка!")


# Создание объектов
warrior = Warrior("Warrior", 5, 100, 20, 80)
mage = Mage("Mage", 5, 80, 25, 100)
assassin = Assassin("Assassin", 5, 90, 22, 95)

heroes = {
    "warrior": warrior,
    "mage": mage,
    "assassin": assassin
}

hero_list = list(heroes.values())


# Выбор пользователя
choice = input("Выберите героя (Warrior / Mage / Assassin): ").lower()

if choice not in heroes:
    print("Неверный выбор героя!")
else:
    player = heroes[choice]

    # Случайный противник (не такой же герой)
    opponents = [hero for hero in hero_list if hero != player]
    enemy = random.choice(opponents)

    print(f"\nВы выбрали: {player.name}")
    print(f"Противник: {enemy.name}\n")

    player.attack()
    enemy.attack()

    # Правила игры
    wins = {
        "Warrior": "Assassin",
        "Assassin": "Mage",
        "Mage": "Warrior"
    }

    if wins[player.name] == enemy.name:
        print(f"\n{player.name} победил!")
    else:
        print(f"\n{enemy.name} победил!")