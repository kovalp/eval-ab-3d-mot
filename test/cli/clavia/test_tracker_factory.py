"""."""

import pytest

from pure_ab_3d_mot.dist_metrics import MetricKind
from pure_ab_3d_mot.matching import MatchingAlgorithm
from pure_ab_3d_mot.tracker import Ab3DMot

from eval_ab_3d_mot.cli.clavia.cmd_line import CmdLineRunWithClavIA
from eval_ab_3d_mot.cli.clavia.tracker_factory import get_tracker


def test_get_silently(cli: CmdLineRunWithClavIA) -> None:
    tracker = get_tracker(cli)
    assert isinstance(tracker, Ab3DMot)
    assert tracker.algorithm == MatchingAlgorithm.HUNGARIAN
    assert tracker.metric == MetricKind.GIOU_3D


def test_get_with_report(cli: CmdLineRunWithClavIA, capsys: pytest.CaptureFixture) -> None:
    cli.verbosity = 2
    tracker = get_tracker(cli)
    assert isinstance(tracker, Ab3DMot)
    ref = """Ab3DMot (AB3DMOT) parameters
    algorithm MatchingAlgorithm.HUNGARIAN
       metric MetricKind.GIOU_3D
    threshold -0.2
     min_hits 3
      max_age 2

"""
    assert ref == capsys.readouterr().out
