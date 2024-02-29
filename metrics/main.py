from pathlib import Path

from .counter import MetricsCounter
from .pretty_printer import (
    print_class_size,
    print_collected_classes,
    print_number_of_operations_overriden,
    print_number_of_added_operations,
    print_specialization_index,
    print_average_operation_size,
    print_average_number_of_parameters,
)


def main() -> None:
    package = Path("./tests")
    metrics_counter = MetricsCounter(package)

    print_collected_classes(metrics_counter)
    print_class_size(metrics_counter)
    print_number_of_operations_overriden(metrics_counter)
    print_number_of_added_operations(metrics_counter)
    print_specialization_index(metrics_counter)
    print_average_operation_size(metrics_counter)
    print_average_number_of_parameters(metrics_counter)
