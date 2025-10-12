"""."""

import numpy as np
import pytest

from eval_ab_3d_mot.cli.common.r_cnn_adaptor import DETS, RCnnAdaptor


def test_r_cnn_adaptor() -> None:
    """."""
    raw_data = np.linspace(1, 15 * 6, num=90).reshape(6, 15)
    raw_data[:, 0] = (1, 3, 3, 5, 5, 5)
    adaptor = RCnnAdaptor(raw_data)
    all_det = []
    for ts, det_dct in enumerate(adaptor.detections_3d()):
        all_det.append(det_dct)

    assert len(all_det) == 6
    assert len(all_det[0][DETS]) == 0
    assert all_det[1][DETS] == pytest.approx(np.array([[8, 9, 10, 11, 12, 13, 14]]))
    assert len(all_det[2][DETS]) == 0
    assert all_det[3][DETS] == pytest.approx(
        np.array([[23, 24, 25, 26, 27, 28, 29], [38, 39, 40, 41, 42, 43, 44]])
    )
    assert len(all_det[4][DETS]) == 0
    assert all_det[5][DETS] == pytest.approx(
        np.array(
            [
                [53, 54, 55, 56, 57, 58, 59],
                [68, 69, 70, 71, 72, 73, 74],
                [83, 84, 85, 86, 87, 88, 89],
            ]
        )
    )
