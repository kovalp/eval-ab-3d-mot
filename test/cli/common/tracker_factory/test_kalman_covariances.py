"""."""

import pytest

from eval_ab_3d_mot.cli.common.tracker_factory import get_tracker
from eval_ab_3d_mot.cli.common.tracker_meta import TrackerMeta
from eval_ab_3d_mot.kitti_category import KittiCategory


def test_default_std_dev(category: KittiCategory, meta: TrackerMeta) -> None:
    tracker = get_tracker(category, meta)
    assert tracker.measurement_std_dev == pytest.approx(1.0)
    assert tracker.proc_std_dev == pytest.approx(1.0)
    assert tracker.proc_vel_std_dev == pytest.approx(0.1)


def test_measurement_std_dev(category: KittiCategory, meta: TrackerMeta) -> None:
    meta.measurement_std_dev = 2.0
    tracker = get_tracker(category, meta)
    assert tracker.measurement_std_dev == pytest.approx(2.0)
    assert tracker.proc_std_dev == pytest.approx(1.0)
    assert tracker.proc_vel_std_dev == pytest.approx(0.1)


def test_proc_std_dev(category: KittiCategory, meta: TrackerMeta) -> None:
    meta.proc_std_dev = 2.0
    tracker = get_tracker(category, meta)
    assert tracker.measurement_std_dev == pytest.approx(1.0)
    assert tracker.proc_std_dev == pytest.approx(2.0)
    assert tracker.proc_vel_std_dev == pytest.approx(0.1)


def test_proc_vel_std_dev(category: KittiCategory, meta: TrackerMeta) -> None:
    meta.proc_vel_std_dev = 0.2
    tracker = get_tracker(category, meta)
    assert tracker.measurement_std_dev == pytest.approx(1.0)
    assert tracker.proc_std_dev == pytest.approx(1.0)
    assert tracker.proc_vel_std_dev == pytest.approx(0.2)
