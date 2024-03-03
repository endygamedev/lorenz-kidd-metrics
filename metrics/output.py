from pprint import pprint
from pathlib import Path
from typing import Any, Callable

from yaml import safe_load, dump

from .counter import MetricsCounter
from .class_data import ClassData


def read_config(path: Path) -> dict[str, Any]:
    content: str = path.read_text(encoding="utf-8")
    return safe_load(content)


def print_metrics(
    metrics_counter: MetricsCounter,
    *,
    config_path: Path,
) -> None:
    classes: list[ClassData] = metrics_counter.classes

    print("Collected classes:")
    pprint(classes)

    config: dict[str, Any] = read_config(config_path)
    for metric in config["metrics"]:
        recommended_value = metric["value"]
        method: str = metric["method"]
        print(f"\n{metric['label']}")
        print("-" * len(metric["label"]))
        for cclass in classes:
            class_method: Callable = getattr(cclass, method)
            class_value = class_method()
            print(
                f"{cclass.name}: {class_value} ≤ {recommended_value} "
                f"— {class_value <= recommended_value}"
            )


def save_metrics(
    metrics_counter: MetricsCounter,
    *,
    config_path: Path,
    output_path: Path,
) -> None:
    classes: list[ClassData] = metrics_counter.classes
    config: dict[str, Any] = read_config(config_path)
    output = {}

    for cclass in classes:
        output[cclass.name] = [{} for _ in range(len(config["metrics"]))]
        for index, metric in enumerate(config["metrics"]):
            recommended_value = metric["value"]
            method: str = metric["method"]
            class_method: Callable = getattr(cclass, method)
            class_value = class_method()

            output[cclass.name][index]["label"] = metric["label"]
            output[cclass.name][index]["value"] = {}
            output[cclass.name][index]["value"]["expect"] = recommended_value
            output[cclass.name][index]["value"]["actual"] = class_value

    with open(output_path, "w", encoding="utf-8") as output_file:
        dump(output, output_file)
