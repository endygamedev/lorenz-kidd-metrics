from typing import Self
from collections import defaultdict
from ast import ClassDef, FunctionDef, walk, Call, Attribute, Name


class ClassData:
    def __init__(
        self,
        defenition: ClassDef,
        methods: list[FunctionDef],
        properties: list[FunctionDef],
        fields: list[str],
    ) -> None:
        self.name: str = defenition.name
        self.defenition: ClassDef = defenition
        self.methods: list[FunctionDef] = methods
        self.properties: list[FunctionDef] = properties
        self.fields: list[str] = fields
        self.base_classes: list[ClassData] = []

    def __str__(self) -> str:
        method_names: list[str] = [method.name for method in self.methods]
        property_names: list[str] = [pproperty.name for pproperty in self.properties]
        return (
            f"<Class {self.name}: "
            f"base_classes: {[base_class.name for base_class in self.base_classes]}; "
            f"fields: {self.fields}; "
            f"methods: {method_names}; "
            f"properties: {property_names}>"
        )

    def __repr__(self) -> str:
        return str(self)

    # `CS` — Class size metrics
    #
    # Calculation rule:
    #   ClassSize = TotalPropertiesCount + TotalMethodsCount
    #
    # Recommended value:
    #   ≤ 20
    def class_size(self) -> int:
        value: int = len(self.properties) + len(self.methods)
        method_names: list[str] = self.method_names()
        for base_class in self.base_classes:
            for method in base_class.methods:
                if method.name not in method_names:
                    value += 1
            value += len(base_class.properties)
        return value

    # `NOO` — Number of Operaions (Methods) Overriden by a Subclass
    #
    # Recommended value:
    #   ≤ 3
    def number_of_operaions_overriden(self) -> int:
        value: int = 0
        for method in self.methods:
            for base_class in self.base_classes:
                if base_class.is_method_overriden(method.name):
                    value += 1
        return value

    # `NOA` —  Number of Operations (Methods) Added by a Subclass
    #
    # Recommended value:
    #   ≤ 0.75
    def number_of_added_operations(self) -> int:
        return len(self.methods) - self.number_of_operaions_overriden()

    # `SI` — Specialization Index
    #
    # Calculation rule:
    #   SpecializationIndex = (NOO * Level) / M
    #
    #   where:  NOO     — Number of Operations (Methods) Overriden by a Subclass
    #           Level   — hierarchy level
    #           M       — total number of methods
    #
    # Recommended value:
    #   ≤ 0.75
    def specialization_index(self) -> int:
        if (m := len(self.methods)) == 0:
            return 0

        number_of_operations_overriden: int = self.number_of_operaions_overriden()
        level: int = self.max_iheritance_depth()

        return (number_of_operations_overriden * level) / m

    # `OSavg` — Average Operation Size
    #
    # Calculation rule:
    #   AverageOperationSize = TotalOperationSizesOverAllMethods / M
    #
    #   where:  M — total number of methods
    #
    # Recommended value:
    #   ≤ 9
    def average_operation_size(self) -> float:
        if (m := len(self.methods)) == 0:
            return 0

        operation_sizes: dict[str, int] = self.operation_sizes()
        total_operation_sizes: int = sum(operation_sizes.values())
        return total_operation_sizes / m

    def operation_sizes(self) -> dict[str, int]:
        sizes: dict[str, int] = defaultdict(int)
        for method in self.methods:
            for node in walk(method):
                if (
                    isinstance(node, Call)
                    and isinstance(node.func, Attribute)
                    and isinstance(node.func.value, Name)
                    and node.func.value.id == "self"
                ):
                    sizes[node.func.attr] += 1
        return sizes

    # `NPavg` — Average Number of Parameters per operation
    #
    # Calculation rule:
    #   AverageNumberOfParameters = TotalOperationSizesOverAllMethods / M
    #
    #   where:  M — total number of methods
    #
    # Recommended value:
    #   ≤ 0.7
    def average_number_of_parameters(self) -> float:
        if (m := len(self.methods)) == 0:
            return 0

        number_of_parameters: dict[str, int] = self.number_of_parameters()
        total_number_of_parameters: int = sum(number_of_parameters.values())
        return total_number_of_parameters / m

    def number_of_parameters(self) -> dict[str, int]:
        parameters: dict[str, int] = defaultdict(int)
        for method in self.methods:
            parameters[method.name] = sum(
                1 for arg in method.args.args if arg.arg != "self"
            )
        return parameters

    def add_base_class(self, base_class: Self) -> None:
        self.base_classes.append(base_class)

    def method_names(self) -> list[str]:
        return [method.name for method in self.methods]

    def is_method_overriden(self, target_method: str) -> bool:
        for method in self.methods:
            if method.name == target_method:
                return True

        for base_class in self.base_classes:
            if base_class.is_method_overriden(target_method):
                return True

        return False

    def max_iheritance_depth(self) -> int:
        max_depth: int = 0

        for base_class in self.base_classes:
            current_depth = base_class.max_iheritance_depth() + 1
            max_depth = max(max_depth, current_depth)

        return max_depth
