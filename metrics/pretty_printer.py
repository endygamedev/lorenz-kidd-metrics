from pprint import pprint

from .counter import MetricsCounter


def print_collected_classes(metrics_counter: MetricsCounter) -> None:
    print("Collected classes:")
    pprint(metrics_counter.classes)


def print_class_size(metrics_counter: MetricsCounter) -> None:
    recommended_value = 20
    print("\nClass Size (CS) Metric:")
    for cclass in metrics_counter.classes:
        print(
            f"{cclass.name}: {cclass.class_size()} <= {recommended_value} "
            f"— {cclass.class_size() <= recommended_value}"
        )


def print_number_of_operation_overriden(metrics_counter: MetricsCounter) -> None:
    recommended_value = 3
    print("\nNumber of Operations Overriden by a Subclass (NOO) Metric:")
    for cclass in metrics_counter.classes:
        print(
            f"{cclass.name}: {cclass.number_of_operaion_overriden()} <= {recommended_value} "
            f"— {cclass.number_of_operaion_overriden() <= recommended_value}"
        )
