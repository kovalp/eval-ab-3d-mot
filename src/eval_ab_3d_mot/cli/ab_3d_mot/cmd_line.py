"""."""

from argparse import ArgumentParser
from typing import Sequence

from rich_argparse import RawTextRichHelpFormatter


PROG = 'run-ab-3d-mot'


class CmdLineRunAb3dMot:
    def __init__(self) -> None:
        self.verbosity = 0
        self.det_file_name = ''
        self.trk_file_name = 'tracking-kitti-info.txt'


def get_cmd_line(args: Sequence[str]) -> CmdLineRunAb3dMot:
    cli = CmdLineRunAb3dMot()
    parser = ArgumentParser(PROG, f'{PROG} [OPTIONS]', formatter_class=RawTextRichHelpFormatter)
    parser.add_argument('det_file_name', help='File name with detections.')
    parser.add_argument('--verbosity', '-v', action='count', help='Script verbosity.')
    parser.add_argument('--trk-file-name', '-o', help='File name to store tracking results.')
    parser.parse_args(args, namespace=cli)
    return cli
