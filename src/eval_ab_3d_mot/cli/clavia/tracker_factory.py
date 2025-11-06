"""."""

from pure_ab_3d_mot.dist_metrics import MetricKind
from pure_ab_3d_mot.matching import MatchingAlgorithm
from pure_ab_3d_mot.tracker import Ab3DMot

from eval_ab_3d_mot.cli.common.ab_3d_mot_parameters import (
    fill_r_cnn_opt_param,
    report_tracker_parameters,
)

from .cmd_line_factory import AUTO, CmdLineRunWithClavIA


def get_tracker(cli: CmdLineRunWithClavIA) -> Ab3DMot:
    tracker = Ab3DMot()
    fill_r_cnn_opt_param(cli.get_parameter_category(), tracker)
    if cli.threshold < 999.0:
        tracker.threshold = cli.threshold
    if cli.max_age > 0:
        tracker.max_age = cli.max_age
    if cli.algorithm != AUTO:
        tracker.algorithm = MatchingAlgorithm(cli.algorithm)
    if cli.metric != AUTO:
        tracker.metric = MetricKind(cli.metric)

    if cli.verbosity > 1:
        print(report_tracker_parameters(tracker))
        print()

    return tracker
