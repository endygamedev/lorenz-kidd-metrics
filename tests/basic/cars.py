class Car:
    def start_engine(self) -> None:
        print("Engine starts")

    def stop_engine(self) -> None:
        print("Engine stops")

    def gas(self) -> None:
        print("Gas-gas-gas")

    def stop(self) -> None:
        print("Stooop")

    def change_transmission(self) -> None:
        raise NotImplementedError("This method should be implemented by subclasses")


class Manual(Car):
    def change_transmission(self) -> None:
        print("Changing transmission on manual car")


class Automatic(Car):
    def change_transmission(self) -> None:
        print("Changing transmission on automatic car")
