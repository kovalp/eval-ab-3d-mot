"""."""

from pathlib import Path

import pytest

from eval_ab_3d_mot.tracking_evaluation import TrackingEvaluation


@pytest.fixture
def te(files_dir: Path) -> TrackingEvaluation:
    tracking_evaluation = TrackingEvaluation('my-sha', gt_path='kitti-root')
    tracking_evaluation.t_path = str(files_dir / 'kitti/tracking/training')
    return tracking_evaluation
