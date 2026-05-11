import pytest

from eval_ab_3d_mot.cli.common.tracker_meta import AUTO, TrackerMeta


def test_init(meta: TrackerMeta) -> None:
    assert meta.threshold == pytest.approx(1000.0)
    assert meta.max_age == -1
    assert meta.metric == AUTO
    assert meta.algorithm == AUTO
    assert meta.measurement_std_dev == pytest.approx(1.0)
    assert meta.proc_std_dev == pytest.approx(1.0)
    assert meta.proc_vel_std_dev == pytest.approx(0.1)
