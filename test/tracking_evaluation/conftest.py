"""."""

import pytest

from eval_ab_3d_mot.tracking_evaluation import TrackingEvaluation


@pytest.fixture
def te() -> TrackingEvaluation:
    return TrackingEvaluation('my-sha', gt_path='kitti-root')
