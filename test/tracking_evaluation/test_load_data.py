"""."""

from pytest_mock import MockerFixture

from eval_ab_3d_mot.tracking_evaluation import TrackingEvaluation


def test_load_data_gt(te: TrackingEvaluation, mocker: MockerFixture) -> None:
    """."""
    mock_load_data = mocker.patch.object(te, '_load_data')
    assert te.load_data(is_ground_truth=True)
    gt_path_ref = 'kitti-root/label'
    mock_load_data.assert_called_once_with(gt_path_ref, cls='car', is_ground_truth=True)


def test_load_data_tracking(te: TrackingEvaluation, mocker: MockerFixture) -> None:
    """."""
    mock_load_data = mocker.patch.object(te, '_load_data')
    assert te.load_data()
    t_path_ref = './results/KITTI/my-sha/data_0'
    mock_load_data.assert_called_once_with(t_path_ref, cls='car', is_ground_truth=False)


def test_load_data_io_error(te: TrackingEvaluation, mocker: MockerFixture) -> None:
    """."""
    mocker.patch.object(te, '_load_data', side_effect=IOError)
    assert not te.load_data()
