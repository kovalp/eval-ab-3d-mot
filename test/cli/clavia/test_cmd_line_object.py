"""."""

from eval_ab_3d_mot.cli.clavia.cmd_line import AUTO, CmdLineRunWithClavIA
from eval_ab_3d_mot.kitti_category import KittiCategory


def test_init(cli: CmdLineRunWithClavIA) -> None:
    assert cli.category_prm == AUTO
    assert cli.category_obj == 'car'


def test_get_annotations(cli: CmdLineRunWithClavIA) -> None:
    assert cli.get_annotations() == ['001.txt', '002.txt']


def test_repr(cli: CmdLineRunWithClavIA) -> None:
    assert repr(cli) == 'CmdLineBatchRunWithClavIA(category-obj car category-prm auto)'


def test_get_object_category(cli: CmdLineRunWithClavIA) -> None:
    assert cli.get_object_category() == KittiCategory.CAR


def test_get_parameter_category(cli: CmdLineRunWithClavIA) -> None:
    assert cli.get_parameter_category() == KittiCategory.CAR


def test_different_get_parameter_category(cli: CmdLineRunWithClavIA) -> None:
    cli.category_prm = 'pedestrian'
    assert cli.get_parameter_category() == KittiCategory.PEDESTRIAN
