"""."""

from typing import Sequence, Union
import numpy as np

from .cmd_line import get_cmd_line


def run(args: Union[Sequence[str], None] = None) -> bool:
    cli = get_cmd_line(args)

    return True


def main() -> None:
    run()  # pragma: no cover
