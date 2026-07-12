from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health  # приватный атрибут
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def attack(self):
        print(f"{self.name} атакует мечом")


class Mage(Hero):
    def attack(self):
        print(f"{self.name} использует магию")


class Assassin(Hero):
    def attack(self):
        print(f"{self.name} атакует из-под тишка")


# Создание объектов
warrior = Warrior("Артур", 10, 100, 20)
mage = Mage("Мерлин", 12, 80, 30)
assassin = Assassin("Эцио", 11, 90, 25)

# Вызов методов
heroes = [warrior, mage, assassin]

for hero in heroes:
    hero.greet()
    hero.attack()
    hero.rest()
    print()