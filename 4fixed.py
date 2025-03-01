from typing import Optional

class Animal:
    """
    Base class representing an animal.
    """

    def init(self, species: str, name: str, age: int):
        if not isinstance(species, str):
            raise ValueError("Species must be a string")
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer")

        self._species = species
        self._name = name
        self._age = age
        self._hungry = True  # Private attribute to control hunger state

    @property
    def species(self):
        return self._species

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def str(self) -> str:
        return f"{self._species} {self._name}, age: {self._age}"

    def repr(self) -> str:
        return f"Animal(species='{self._species}', name='{self._name}', age={self._age})"

    def make_sound(self) -> str:
        return "Unknown sound"

    def eat(self) -> None:
        self._hungry = False

    def is_hungry(self) -> bool:
        return self._hungry


class Dog(Animal):
    """
    Class representing a dog.
    """

    def init(self, name: str, breed: str, age: int, commands: Optional[list[str]] = None):
        super().init(species="Dog", name=name, age=age)

        if not isinstance(breed, str):
            raise ValueError("Breed must be a string")

        self._breed = breed
        self._commands = commands if commands is not None else []
        self._favorite_toy = "Ball"

    @property
    def breed(self):
        return self._breed

    @property
    def favorite_toy(self):
        return self._favorite_toy

    @favorite_toy.setter
    def favorite_toy(self, toy: str):
        if not isinstance(toy, str):
            raise ValueError("Favorite toy must be a string")
        self._favorite_toy = toy

    def str(self) -> str:
        return f"{self._breed} {self.name}, age: {self.age}, knows commands: {', '.join(self._commands) or 'none'}"

    def repr(self) -> str:
        return f"Dog(name='{self.name}', breed='{self._breed}', age={self.age}, commands={self._commands})"

    def make_sound(self) -> str:
        return "Woof!"

    def learn_command(self, command: str) -> None:
        if not isinstance(command, str):
            raise ValueError("Command must be a string")
        self._commands.append(command)

    def bring_toy(self) -> str:
        return f"{self.name} brought {self._favorite_toy}!"


if name == "main":
    animal = Animal(species="Unknown", name="Nameless", age=1)
    print(animal)
    print(repr(animal))
    print(animal.make_sound())

    dog = Dog(name="Bobby", breed="Mixed", age=3)
    print(dog)
    print(repr(dog))
    print(dog.make_sound())

    dog.learn_command("Sit")
    print(dog)
    print(dog.bring_toy())

    dog.favorite_toy = "Bone"
    print(dog.bring_toy())

    print(f"Is Bobby hungry? {dog.is_hungry()}")
    dog.eat()
    print(f"Is Bobby hungry? {dog.is_hungry()}")