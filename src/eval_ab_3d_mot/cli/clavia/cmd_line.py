"""."""

from argparse import ArgumentParser
from typing import List, Sequence

from rich_argparse import RawTextRichHelpFormatter

from eval_ab_3d_mot.cli.common.get_hlp import get_hlp
from eval_ab_3d_mot.cli.common.kitti_category import CATEGORIES, HLP_CATEGORY, AUTO_CATEGORY
from eval_ab_3d_mot.kitti_category import KittiCategory


PROG = 'batch-run-ab-3d-mot-with-clavia'
HLP_OUT = 'Directory to store tracking results.'
HLP_ANN = 'Annotations (ground-truth) directory.'


class CmdLineBatchRunWithClavIA:
    def __init__(self) -> None:
        self.verbosity = 0
        self.annotations: List[str] = []
        self.trk_dir = 'clavia-kitti'
        self.category = KittiCategory.CAR.value

    def get_category(self) -> KittiCategory:
        if self.category == AUTO_CATEGORY:
            raise ValueError('I cannot determine the category automatically.')
        return KittiCategory(self.category)

    def get_annotations(self) -> List[str]:
        return sorted(self.annotations)


def get_cmd_line(args: Sequence[str]) -> CmdLineBatchRunWithClavIA:
    cli = CmdLineBatchRunWithClavIA()
    parser = ArgumentParser(PROG, f'{PROG} <annotations> [OPTIONS]',
                            formatter_class=RawTextRichHelpFormatter)
    parser.add_argument('annotations', nargs='+', help='Annotation files.')
    parser.add_argument('--trk-dir', '-o', help=get_hlp(HLP_OUT, cli.trk_dir))
    hlp_category = get_hlp(HLP_CATEGORY, cli.category)
    parser.add_argument('--category', '-c', choices=CATEGORIES, help=hlp_category)
    parser.add_argument('--verbosity', '-v', action='count', help='Script verbosity.')
    parser.parse_args(args, namespace=cli)
    return cli
