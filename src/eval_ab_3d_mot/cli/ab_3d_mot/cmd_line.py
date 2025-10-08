"""."""

import argparse

from typing import Sequence


PROG = 'run-ab-3d-mot'


class CmdLineRunAb3dMot:
    def __init__(self) -> None: ...


def get_cmd_line(args: Sequence[str]) -> CmdLineRunAb3dMot:
    cli = CmdLineRunAb3dMot()
    parser = argparse.ArgumentParser(PROG, f'{PROG} [OPTIONS]')
    parser.parse_args(args, namespace=cli)
    return cli
