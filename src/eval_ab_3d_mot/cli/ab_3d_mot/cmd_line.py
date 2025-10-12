"""."""

from argparse import ArgumentParser
from typing import Sequence

from rich_argparse import RawTextRichHelpFormatter

from eval_ab_3d_mot.cli.common.get_hlp import get_hlp


PROG = 'run-ab-3d-mot'
HLP_OUT = 'File name to store tracking results.'


class CmdLineRunAb3dMot:
    def __init__(self) -> None:
        self.verbosity = 0
        self.det_file_name = ''
        self.trk_file_name = 'tracking-kitti.txt'


def get_cmd_line(args: Sequence[str]) -> CmdLineRunAb3dMot:
    cli = CmdLineRunAb3dMot()
    parser = ArgumentParser(PROG, f'{PROG} [OPTIONS]', formatter_class=RawTextRichHelpFormatter)
    parser.add_argument('det_file_name', help='File name with detections.')
    parser.add_argument('--verbosity', '-v', action='count', help='Script verbosity.')
    parser.add_argument('--trk-file-name', '-o', help=get_hlp(HLP_OUT, cli.trk_file_name))
    parser.parse_args(args, namespace=cli)
    return cli
