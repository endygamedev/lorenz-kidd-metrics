from pprint import pprint

from .counter import MetricsCounter


def print_collected_classes(metrics_counter: MetricsCounter) -> None:
    print("Collected classes:")
    pprint(metrics_counter.classes)


def print_class_size(metrics_counter: MetricsCounter) -> None:
    recommended_value: int = 20
    print("\nClass Size (CS) Metric:")
    for cclass in metrics_counter.classes:
        print(
            f"{cclass.name}: {cclass.class_size()} <= {recommended_value} "
            f"— {cclass.class_size() <= recommended_value}"
        )


def print_number_of_operations_overriden(metrics_counter: MetricsCounter) -> None:
    recommended_value: int = 3
    print("\nNumber of Operations Overriden by a Subclass (NOO) Metric:")
    for cclass in metrics_counter.classes:
        print(
            f"{cclass.name}: {cclass.number_of_operaions_overriden()} <= {recommended_value} "
            f"— {cclass.number_of_operaions_overriden() <= recommended_value}"
        )


def print_number_of_added_operations(metrics_counter: MetricsCounter) -> None:
    recommended_value: int = 4
    print("\nNumber of Operations Added by a Subclass (NOA) Metric:")
    for cclass in metrics_counter.classes:
        print(
            f"{cclass.name}: {cclass.number_of_added_operations()} <= {recommended_value} "
            f"— {cclass.number_of_added_operations() <= recommended_value}"
        )


def print_specialization_index(metrics_counter: MetricsCounter) -> None:
    recommended_value: float = 0.75
    print("\nSpecialization Index (SI) Metric:")
    for cclass in metrics_counter.classes:
        print(
            f"{cclass.name}: {cclass.specialization_index()} <= {recommended_value} "
            f"— {cclass.specialization_index() <= recommended_value}"
        )
