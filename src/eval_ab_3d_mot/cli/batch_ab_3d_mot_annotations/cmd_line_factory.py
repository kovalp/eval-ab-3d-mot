"""."""

from argparse import ArgumentParser
from typing import Sequence

from rich_argparse import RawTextRichHelpFormatter

from eval_ab_3d_mot.cli.common.get_hlp import get_hlp
from eval_ab_3d_mot.cli.common.init_coinciding_attrs import init_coinciding_attrs
from eval_ab_3d_mot.cli.common.tracker_meta import AUTO, add_args
from eval_ab_3d_mot.kitti_category import KittiCategory

from .cmd_line_object import CmdLineBatchRunAb3dMotAnnotations


PROG = 'batch-run-ab-3d-mot-annotations'
HLP_OUT = 'Directory to store tracking results.'
DEF_POLICY = 'If not given the category-dependent optimal will be used.'
HLP_CAT_OBJ = 'Category of the objects selected for tracking.'
HLP_CAT_PRM = 'Category of to selected tracker parameters.'


def get_cmd_line(args: Sequence[str]) -> CmdLineBatchRunAb3dMotAnnotations:
    cli = CmdLineBatchRunAb3dMotAnnotations()
    parser = ArgumentParser(
        PROG, f'{PROG} <annotations+> [OPTIONS]', formatter_class=RawTextRichHelpFormatter
    )
    parser.add_argument('annotations', nargs='+', help='KITTI annotation files.')
    parser.add_argument('--trk-dir', '-o', help=get_hlp(HLP_OUT, cli.trk_dir))
    cc_oo = tuple(c.value for c in KittiCategory)
    hlp_c_obj = get_hlp(HLP_CAT_OBJ, cli.category_obj)
    parser.add_argument('--category-obj', '-c', choices=cc_oo, help=hlp_c_obj)
    hlp_c_prm = get_hlp(HLP_CAT_PRM, cli.category_prm + ' 🛈 objects category')
    cc_pp = tuple(c.value for c in KittiCategory) + (AUTO,)
    parser.add_argument('--category-prm', '-p', choices=cc_pp, help=hlp_c_prm)
    parser.add_argument('--verbosity', '-v', action='count', help='Script verbosity.')
    add_args(parser)
    ns = parser.parse_args(args)
    init_coinciding_attrs(ns, cli)
    init_coinciding_attrs(ns, cli.meta)
    if cli.verbosity > 0:
        print(cli)

    return cli
