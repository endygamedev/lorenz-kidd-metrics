from typing import Self
from ast import ClassDef, FunctionDef


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
    def class_size(self) -> int:
        value = len(self.properties) + len(self.methods)
        method_names = self.method_names()
        for base_class in self.base_classes:
            for method in base_class.methods:
                if method.name not in method_names:
                    value += 1
            value += len(base_class.properties)
        return value

    def add_base_class(self, base_class: Self) -> None:
        self.base_classes.append(base_class)

    def method_names(self) -> list[str]:
        return [method.name for method in self.methods]
