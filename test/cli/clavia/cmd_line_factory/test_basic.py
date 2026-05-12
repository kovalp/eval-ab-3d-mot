"""."""

import pytest

from eval_ab_3d_mot.cli.clavia.cmd_line_factory import AUTO, get_cmd_line
from eval_ab_3d_mot.kitti_category import KittiCategory


def test_no_args() -> None:
    with pytest.raises(SystemExit):
        get_cmd_line([])


def test_no_options(capsys: pytest.CaptureFixture) -> None:
    cli = get_cmd_line(['2.txt', '1.txt'])
    assert cli.category_prm == AUTO
    assert cli.category_obj == 'car'
    assert repr(cli) not in capsys.readouterr().out
    meta = cli.meta
    assert meta.algorithm == AUTO
    assert meta.metric == AUTO
    assert meta.max_age == -1
    assert meta.threshold == pytest.approx(1000.0)
    assert meta.proc_vel_std_dev == pytest.approx(0.1)
    assert meta.proc_std_dev == pytest.approx(1.0)
    assert meta.measurement_std_dev == pytest.approx(1.0)


def test_obj_category_option() -> None:
    cli = get_cmd_line(['2.txt', '1.txt', '-c', 'pedestrian'])
    assert cli.get_object_category() == KittiCategory.PEDESTRIAN
    assert cli.get_parameter_category() == KittiCategory.PEDESTRIAN


def test_both_category_options() -> None:
    cli = get_cmd_line(['2.txt', '1.txt', '-c', 'pedestrian', '-p', 'car'])
    assert cli.get_object_category() == KittiCategory.PEDESTRIAN
    assert cli.get_parameter_category() == KittiCategory.CAR


def test_if_verbose(capsys: pytest.CaptureFixture) -> None:
    cli = get_cmd_line(['2.txt', '1.txt', '-v'])
    assert repr(cli) in capsys.readouterr().out


def test_kf_cov() -> None:
    args = [
        'car/0001.txt',
        '--measurement-std-dev',
        '1.23',
        '--proc-std-dev',
        '4.56',
        '--proc-vel-std-dev',
        '7.89',
    ]
    meta = get_cmd_line(args).meta
    assert meta.measurement_std_dev == pytest.approx(1.23)
    assert meta.proc_std_dev == pytest.approx(4.56)
    assert meta.proc_vel_std_dev == pytest.approx(7.89)
