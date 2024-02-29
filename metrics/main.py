from pathlib import Path

from .counter import MetricsCounter
from .pretty_printer import (
    print_class_size,
    print_collected_classes,
    print_number_of_operation_overriden,
)


def main() -> None:
    package = Path("./tests")
    metrics_counter = MetricsCounter(package)

    print_collected_classes(metrics_counter)
    print_class_size(metrics_counter)
    print_number_of_operation_overriden(metrics_counter)
