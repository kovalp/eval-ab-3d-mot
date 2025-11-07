"""."""

import pytest

from eval_ab_3d_mot.cli.batch_ab_3d_mot.cmd_line_object import CmdLineBatchRunAb3dMot
from eval_ab_3d_mot.kitti_category import KittiCategory


@pytest.fixture()
def cli() -> CmdLineBatchRunAb3dMot:
    cli = CmdLineBatchRunAb3dMot()
    cli.detections = ['car/002.txt', 'car/001.txt']
    return cli


def test_get_detections(cli: CmdLineBatchRunAb3dMot) -> None:
    assert cli.get_detections() == ['car/001.txt', 'car/002.txt']
    cli.detections = ['car/002.txt', 'pedestrian/001.txt']
    with pytest.raises(ValueError):
        cli.get_detections()


def test_get_object_category(cli: CmdLineBatchRunAb3dMot) -> None:
    assert cli.get_object_category() == KittiCategory.CAR


def test_get_parameter_category(cli: CmdLineBatchRunAb3dMot) -> None:
    assert cli.get_parameter_category() == KittiCategory.CAR
    cli.category_prm = 'cyclist'
    assert cli.get_parameter_category() == KittiCategory.CYCLIST
