"""."""

from pathlib import Path

from eval_ab_3d_mot.cli.clavia.clavia_main import run


def test_run(files_dir: Path) -> None:
    summary_car = run([str(files_dir / 'kitti/annotations/training/0001.txt'), '-c', 'pedestrian'])
    ref = """Confusion matrix TP 112 TN 9 FP 0 FN 0
     accuracy 1.000000
    precision 1.0000
       recall 1.0000
     f1-score 1.0000"""
    assert summary_car == ref
