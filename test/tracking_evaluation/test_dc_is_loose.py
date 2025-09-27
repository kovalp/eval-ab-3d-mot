"""."""

from pathlib import Path

import pytest

from eval_ab_3d_mot.tracking_evaluation import TrackingEvaluation


@pytest.fixture
def te_dc_is_loose(files_dir: Path) -> TrackingEvaluation:
    te = TrackingEvaluation('my-sha', gt_path='kitti-root')
    te.sequence_name = ['dc-is-loose']
    te.n_frames = [1]
    te.n_sequences = 1
    te.t_path = str(files_dir / 'kitti/tracking/training')
    assert te.load_data(False), 'some file does not exist?'

    te.gt_path = str(files_dir / 'kitti/annotations/training')
    assert te.load_data(True), 'some file does not exist?'
    return te


def test_dc_is_loose(te_dc_is_loose: TrackingEvaluation) -> None:
    """."""
    assert te_dc_is_loose.compute_3rd_party_metrics()
    assert te_dc_is_loose.fn == 1
    assert te_dc_is_loose.tp == 1
    assert te_dc_is_loose.MOTP == pytest.approx(1.0)
    assert te_dc_is_loose.F1 == pytest.approx(0.666666666666666)
    assert te_dc_is_loose.recall == pytest.approx(0.5)
    assert te_dc_is_loose.precision == pytest.approx(1.0)
