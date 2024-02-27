from pathlib import Path
from glob import glob
from typing import Any
from ast import parse, ClassDef, Name, FunctionDef, Assign, Attribute

from .class_data import ClassData


class MetricsCounter:
    def __init__(self, package: Path):
        self.module_ast = self.parse_package(package)
        self.classes: list[ClassData] = []
        self.get_classes()

    @staticmethod
    def parse_package(package: Path) -> list:
        module_ast = []
        for module in glob("./**/*.py", root_dir=package, recursive=True):
            source = Path(package, module).read_text(encoding="utf-8")
            module_ast += parse(source=source, filename=package).body
        return module_ast

    def get_classes(self):
        classes: list[tuple[ClassData, list[str]]] = []

        for defenition in self.module_ast:
            if isinstance(defenition, ClassDef):
                base_classes = [
                    base_class.id
                    for base_class in defenition.bases
                    if isinstance(base_class, Name)
                ]

                functions: list[FunctionDef] = []
                fields: list[Any] = []
                for statement in defenition.body:
                    if isinstance(statement, FunctionDef):
                        functions.append(statement)
                        if statement.name == "__init__":
                            fields = self.get_class_fields(statement.body)
                methods, properties = self.divide_methods_and_properties(functions)

                class_data = ClassData(
                    defenition=defenition,
                    methods=methods,
                    properties=properties,
                    fields=fields,
                )
                classes.append((class_data, base_classes))

        for current_class_data, base_classes in classes:
            for base_class in base_classes:
                for other_class_data, _ in classes:
                    if other_class_data.name == base_class:
                        current_class_data.add_base_class(other_class_data)

        self.classes = [class_data for (class_data, _) in classes]

    @staticmethod
    def get_class_fields(statements: list[Any]):
        fields = []
        for statement in statements:
            if isinstance(statement, Assign):
                for target in statement.targets:
                    if (
                        isinstance(target, Attribute)
                        and isinstance(target.value, Name)
                        and target.value.id == "self"
                    ):
                        fields.append(target.attr)
        return fields

    @staticmethod
    def divide_methods_and_properties(
        functions: list[FunctionDef],
    ) -> tuple[list[FunctionDef], list[FunctionDef]]:
        methods: list[FunctionDef] = []
        properties: list[FunctionDef] = []

        for function in functions:
            has_property_decorator: bool = False

            # Iterator over function (method) decorator
            for decorator in function.decorator_list:
                if isinstance(decorator, Name) and decorator.id == "property":
                    has_property_decorator = True
                    break

            if has_property_decorator:
                properties.append(function)
            else:
                methods.append(function)

        return methods, properties
