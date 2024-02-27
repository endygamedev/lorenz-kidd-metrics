class Pet:
    def __init__(self, name, weight):
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


class Cat(Pet):

    # Class attribute
    language = "Meow"

    # Method
    def say_name(self):
        return "{}, my name is {} and I am nice!".format(self.language, self.name)


class Dog(Pet):

    # Class attribute
    language = "Woof"

    # Method
    def say_name(self):
        return "{}, my name is {} and I smell funny!".format(self.language, self.name)
