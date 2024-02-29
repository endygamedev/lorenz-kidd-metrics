class Animal:
    def __init__(self, animal_type: str) -> None:
        self.__animal_type = animal_type

    @property
    def animal_type(self) -> str:
        return self.__animal_type

    @animal_type.setter
    def animal_type(self, value: str) -> None:
        self.__animal_type = value


class Pet(Animal):
    def __init__(self, animal_type, name, weight):
        super().__init__(animal_type)
        self.name = name
        self.weight = weight

    def eat_food(self, food):
        self.weight += food

    @property
    def weight_lbs(self):
        return self.weight / 0.45359237

    def say_name(self):
        raise NotImplementedError(
            "This method should be implemented by subclasses of Pet"
        )

    def say_name_loudly(self):
        return self.say_name().upper()

    def eat(self):
        self.weight += 0.3

    def run(self):
        self.weight -= 0.3


class Cat(Pet):
    language = "Meow"

    def say_name(self) -> str:
        return f"{self.language}, my name is {self.name} and I am nice!"


class Dog(Pet):
    language = "Woof"

    def say_name(self) -> str:
        return f"{self.language}, my name is {self.name} and I smell funny!"
