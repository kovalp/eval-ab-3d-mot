"""."""

from argparse import ArgumentParser
from pathlib import Path
from typing import List, Sequence

from rich_argparse import RawTextRichHelpFormatter

from eval_ab_3d_mot.cli.common.get_hlp import get_hlp
from eval_ab_3d_mot.kitti_category import KittiCategory


PROG = 'batch-run-ab-3d-mot'
HLP_OUT = 'Directory to store tracking results.'
HLP_CATEGORY = 'Category of the detected objects.'
AUTO_CATEGORY = 'derived-from-dir-name'
CATEGORIES = tuple(c.value for c in KittiCategory) + (AUTO_CATEGORY,)


class CmdLineBatchRunAb3dMot:
    def __init__(self) -> None:
        self.verbosity = 0
        self.detections: List[str] = []
        self.trk_dir = 'tracking-kitti'
        self.category = AUTO_CATEGORY

    def get_category(self) -> KittiCategory:
        cls_opt = self.category
        first_path = Path(self.detections[0])
        return KittiCategory(first_path.parent.name if cls_opt == AUTO_CATEGORY else cls_opt)

    def get_detections(self) -> List[str]:
        if len(set(Path(d).parent for d in self.detections)) > 1:
            raise ValueError('I expect the detection files to be in the same directory.')
        return sorted(self.detections)


def get_cmd_line(args: Sequence[str]) -> CmdLineBatchRunAb3dMot:
    cli = CmdLineBatchRunAb3dMot()
    parser = ArgumentParser(PROG, f'{PROG} [OPTIONS]', formatter_class=RawTextRichHelpFormatter)
    parser.add_argument('detections', nargs='+', help='Detection files.')
    parser.add_argument('--trk-dir', '-o', help=get_hlp(HLP_OUT, cli.trk_dir))
    parser.add_argument(
        '--category', '-c', choices=CATEGORIES, help=get_hlp(HLP_CATEGORY, cli.category)
    )
    parser.add_argument('--verbosity', '-v', action='count', help='Script verbosity.')
    parser.parse_args(args, namespace=cli)
    return cli
