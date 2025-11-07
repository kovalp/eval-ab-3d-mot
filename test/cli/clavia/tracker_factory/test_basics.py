"""."""

import pytest

from pure_ab_3d_mot.dist_metrics import MetricKind
from pure_ab_3d_mot.matching import MatchingAlgorithm
from pure_ab_3d_mot.tracker import Ab3DMot

from eval_ab_3d_mot.cli.common.tracker_factory import get_tracker
from eval_ab_3d_mot.cli.common.tracker_meta import TrackerMeta
from eval_ab_3d_mot.kitti_category import KittiCategory


def test_get_silently(category: KittiCategory, meta: TrackerMeta) -> None:
    tracker = get_tracker(category, meta)
    assert isinstance(tracker, Ab3DMot)
    assert tracker.algorithm == MatchingAlgorithm.HUNGARIAN
    assert tracker.metric == MetricKind.GIOU_3D


def test_get_with_report(
    category: KittiCategory, meta: TrackerMeta, capsys: pytest.CaptureFixture
) -> None:
    tracker = get_tracker(category, meta, 2)
    assert isinstance(tracker, Ab3DMot)
    ref = """Ab3DMot (AB3DMOT) parameters
    algorithm MatchingAlgorithm.HUNGARIAN
       metric MetricKind.GIOU_3D
    threshold -0.2
     min_hits 3
      max_age 2

"""
    assert ref == capsys.readouterr().out
