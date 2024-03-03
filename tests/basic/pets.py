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

    def run(self, distance):
        self.weight -= distance / 2

    def daily_activity(self) -> None:
        self.eat_food(0.3)
        self.run(0.6)


class Cat(Pet):
    def __init__(self) -> None:
        self.__language = "Mew"

    @property
    def language(self) -> str:
        return self.__language

    def say_name(self) -> str:
        self.daily_activity()
        return f"{self.language}, my name is {self.name} and I am nice!"


class Dog(Pet):
    def __init__(self) -> None:
        self.__language = "Woof"

    @property
    def language(self) -> str:
        return self.__language

    def say_name(self) -> str:
        self.daily_activity()
        return f"{self.language}, my name is {self.name} and I smell funny!"
