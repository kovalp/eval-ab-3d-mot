"""."""

from pure_ab_3d_mot.tracker import Ab3DMot

from eval_ab_3d_mot.cli.common.ab_3d_mot_parameters import (
    fill_r_cnn_opt_param,
    report_tracker_parameters,
)

from .cmd_line import CmdLineRunWithClavIA


def get_tracker(cli: CmdLineRunWithClavIA) -> Ab3DMot:
    tracker = Ab3DMot()
    fill_r_cnn_opt_param(cli.get_parameter_category(), tracker)
    if cli.verbosity > 1:
        print(report_tracker_parameters(tracker))
        print()

    return tracker
