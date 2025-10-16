"""."""

from pathlib import Path

import numpy as np

from eval_ab_3d_mot.cli.common.tracking_io import write_ab_3d_mot_tracking


def test_write_ab_3d_mot_tracking(tmp_path: Path) -> None:
    """."""
    out_file = tmp_path / 'out.txt'
    # fmt: off
    result = [
        [np.array([[1.5, .5, 1.8, 2.5, 5.5, 6.5, .57, 1, 0, 2, 100, 200, 300, 400, 7, 8]]),
         np.array([[1.5, .5, 1.8, 2.5, 5.5, 6.5, .57, 5, 0, 2, 100, 200, 300, 400, 7, 8]]),
        ],
        [],
        [
        np.array([[1.5, .5, 1.8, 2.5, 5.5, 6.5, .57, 6, 3, 2, 100, 200, 300, 400, 7, 8]]),
        np.array([[1.5, .5, 1.8, 2.5, 5.5, 6.5, .57, 7, 3, 2, 100, 200, 300, 400, 7, 8]]),
        np.array([[1.5, .5, 1.8, 2.5, 5.5, 6.5, .57, 8, 3, 2, 100, 200, 300, 400, 7, 8]]),
        ],
        [],
        [],
    ]
    # fmt: on
    write_ab_3d_mot_tracking(result, str(out_file))
    assert out_file.exists()
    ref = """0 1 Car 0 0 8.0 100.0 200.0 300.0 400.0 1.5 0.5 1.8 2.5 5.5 6.5 0.57 7.0
0 5 Car 0 0 8.0 100.0 200.0 300.0 400.0 1.5 0.5 1.8 2.5 5.5 6.5 0.57 7.0
2 6 Car 0 0 8.0 100.0 200.0 300.0 400.0 1.5 0.5 1.8 2.5 5.5 6.5 0.57 7.0
2 7 Car 0 0 8.0 100.0 200.0 300.0 400.0 1.5 0.5 1.8 2.5 5.5 6.5 0.57 7.0
2 8 Car 0 0 8.0 100.0 200.0 300.0 400.0 1.5 0.5 1.8 2.5 5.5 6.5 0.57 7.0
"""
    assert out_file.read_text() == ref
