"""."""

import pytest

from eval_ab_3d_mot.cli.batch_ab_3d_mot_annotations.cmd_line_factory import AUTO, get_cmd_line
from eval_ab_3d_mot.cli.batch_ab_3d_mot_annotations.cmd_line_object import (
    CmdLineBatchRunAb3dMotAnnotations,
)


def test_category_and_tracking_dir() -> None:
    args = ['car/0001.txt', 'car/0002.txt', '-v', '-c', 'cyclist', '-o', 'my-dir']
    cli = get_cmd_line(args)
    assert isinstance(cli, CmdLineBatchRunAb3dMotAnnotations)
    assert cli.verbosity == 1
    assert cli.category_obj == 'cyclist'
    assert cli.category_prm == AUTO
    assert cli.trk_dir == 'my-dir'
    assert cli.annotations == ['car/0001.txt', 'car/0002.txt']
    meta = cli.meta
    assert meta.metric == AUTO
    assert meta.algorithm == AUTO
    assert meta.threshold == pytest.approx(1000.0)
    assert meta.max_age == -1
    assert meta.measurement_std_dev == pytest.approx(1.0)
    assert meta.proc_std_dev == pytest.approx(1.0)
    assert meta.proc_vel_std_dev == pytest.approx(0.1)


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


def test_at_least_one_detection_file_expected() -> None:
    with pytest.raises(SystemExit):
        get_cmd_line([])
