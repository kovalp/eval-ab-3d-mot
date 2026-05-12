"""."""

from pathlib import Path

import pytest

from eval_ab_3d_mot.core.tracking_evaluation import SEQ_LENGTHS_NAME, TrackingEvaluation


@pytest.fixture
def te(files_dir: Path) -> TrackingEvaluation:
    tracking_evaluation = TrackingEvaluation('my-sha', SEQ_LENGTHS_NAME, ann_root='kitti-root')
    tracking_evaluation.t_path = str(files_dir / 'kitti/tracking/training')
    return tracking_evaluation
