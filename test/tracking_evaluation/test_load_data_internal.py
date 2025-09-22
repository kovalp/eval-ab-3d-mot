"""."""

from pathlib import Path

import pytest

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
    assert te.groundtruth[0][0][0].track_id == 0


def test_tracking_17_items_in_1_obj_1_frame(te: TrackingEvaluation) -> None:
    """."""
    te.sequence_name = ['0012-17']
    te.n_frames = [3]
    assert te._load_data(te.t_path, 'car')
    assert len(te.tracker) == 1
    assert len(te.tracker[0]) == 3
    assert len(te.tracker[0][0]) == 3
    assert isinstance(te.tracker[0][0][0], TrackData)
    assert te.tracker[0][0][0].score == pytest.approx(-1.0)


def test_tracking_18_items_in_1_obj_1_frame(te: TrackingEvaluation) -> None:
    """."""
    te.sequence_name = ['0012-18']
    te.n_frames = [3]
    assert te._load_data(te.t_path, 'car')
    assert len(te.tracker) == 1
    assert len(te.tracker[0]) == 3
    assert len(te.tracker[0][0]) == 3
    assert isinstance(te.tracker[0][0][0], TrackData)
    assert te.tracker[0][0][0].score == pytest.approx(0.0)


def test_tracking_19_items_in_1_obj_1_frame(te: TrackingEvaluation) -> None:
    """."""
    te.sequence_name = ['0012-19']
    te.n_frames = [3]
    assert not te._load_data(te.t_path, 'car')


def test_track_id_negative_and_car(te: TrackingEvaluation) -> None:
    """."""
    te.sequence_name = ['0012-id-ne0-car']
    te.n_frames = [3]
    assert te._load_data(te.t_path, 'car')
    assert len(te.tracker) == 1
    assert len(te.tracker[0]) == 3
    assert len(te.tracker[0][0]) == 2
    assert isinstance(te.tracker[0][0][0], TrackData)
    assert te.tracker[0][0][0].score == pytest.approx(0.0)


def test_dynamic_extension(te: TrackingEvaluation, files_dir: Path) -> None:
    """."""
    te.sequence_name = ['0012']
    te.n_frames = [70]
    te.n_sequences = 1
    te.gt_path = str(files_dir / 'kitti/annotations/training')
    assert te._load_data(te.gt_path, 'car', is_ground_truth=True)
    assert len(te.groundtruth) == 1
    assert len(te.groundtruth[0]) == 570


def test_tracking_not_unique_ids(te: TrackingEvaluation) -> None:
    """."""
    te.sequence_name = ['0012-not-unique-ids']
    assert not te._load_data(te.t_path, 'car')


def test_trigger_no_2d(te: TrackingEvaluation) -> None:
    """."""
    te.sequence_name = ['0012-no-2d']
    assert te._load_data(te.t_path, 'car')
    assert not te.eval_2d


def test_trigger_no_3d(te: TrackingEvaluation) -> None:
    """."""
    te.sequence_name = ['0012-no-3d']
    assert te._load_data(te.t_path, 'car')
    assert not te.eval_3d


def test_trigger_no_trajectories(te: TrackingEvaluation) -> None:
    """."""
    te.sequence_name = ['0012-17']
    assert not te._load_data(te.t_path, 'bogus-class')
