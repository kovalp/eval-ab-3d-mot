"""."""

from typing import List

import numpy as np

from pure_ab_3d_mot.tracker import Ab3DMot
from eval_ab_3d_mot.cli.common.r_cnn_adaptor import RCnnAdaptor, DETS


def get_tracking_result(adaptor: RCnnAdaptor, tracker: Ab3DMot, verbosity: int) -> List[List[np.ndarray]]:
    result = []
    for step, det_dct in enumerate(adaptor.detections_3d()):
        tracker.track(det_dct)
        persistent_tracks = tracker.output()
        result.append(persistent_tracks)
        if verbosity > 0:
            print(step, len(det_dct[DETS]), len(persistent_tracks))
    return result
