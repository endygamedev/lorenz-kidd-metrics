from pathlib import Path

from .counter import MetricsCounter
from .output import print_metrics, save_metrics


def main() -> None:
    package = Path("./tests")
    metrics_counter = MetricsCounter(package)

    config: Path = Path("./config/metics.yml")
    print_metrics(metrics_counter, config_path=config)

    output: Path = Path("./out/metrics.yml")
    save_metrics(metrics_counter, config_path=config, output_path=output)
