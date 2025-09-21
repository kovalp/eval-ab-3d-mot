"""."""

from pathlib import Path

from eval_ab_3d_mot.track_data import TrackData
from eval_ab_3d_mot.tracking_evaluation import TrackingEvaluation


def test_ground_truth(te: TrackingEvaluation, files_dir: Path) -> None:
    """."""
    te.sequence_name = ['0001', '0012']
    te.n_frames = [448, 79]
    te.n_sequences = 1
    te.gt_path = str(files_dir / 'kitti/annotations/training')
    assert te._load_data(te.gt_path, 'car', is_ground_truth=True)
    assert len(te.groundtruth) == 2
    assert len(te.groundtruth[0]) == 448
    assert len(te.groundtruth[0][0]) == 7
    assert isinstance(te.groundtruth[0][0][0], TrackData)
