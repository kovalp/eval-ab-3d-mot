"""."""

import pytest

from pure_ab_3d_mot.dist_metrics import MetricKind
from pure_ab_3d_mot.matching import MatchingAlgorithm

from eval_ab_3d_mot.cli.clavia.cmd_line_factory import CmdLineRunWithClavIA
from eval_ab_3d_mot.cli.clavia.tracker_factory import get_tracker


def test_overwrite_algorithm(cli: CmdLineRunWithClavIA) -> None:
    cli.algorithm = 'greedy'
    tracker = get_tracker(cli)
    assert tracker.algorithm == MatchingAlgorithm.GREEDY


def test_overwrite_metric(cli: CmdLineRunWithClavIA) -> None:
    cli.metric = 'm_dis'
    tracker = get_tracker(cli)
    assert tracker.metric == MetricKind.MAHALANOBIS_DIST


def test_overwrite_max_age(cli: CmdLineRunWithClavIA) -> None:
    cli.max_age = 123
    tracker = get_tracker(cli)
    assert tracker.max_age == 123


def test_overwrite_threshold(cli: CmdLineRunWithClavIA) -> None:
    cli.threshold = -1.234
    tracker = get_tracker(cli)
    assert tracker.threshold == pytest.approx(-1.234)
