from pathlib import Path
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
            f"{cclass.name}: {cclass.class_size()} <= {recommended_value} — {cclass.class_size() <= recommended_value}"
        )


def main() -> None:
    package = Path("./tests")
    metrics_counter = MetricsCounter(package)
    print_collected_classes(metrics_counter)
    print_class_size(metrics_counter)
