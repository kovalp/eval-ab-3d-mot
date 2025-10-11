"""."""

from typing import Sequence, Union

import numpy as np

from pure_ab_3d_mot.tracker import Ab3DMot

from .cmd_line import get_cmd_line
from .r_cnn_adaptor import DETS, INFO, read_r_cnn_ab_3d_mot
from .tracking_io import write_ab_3d_mot_tracking


def run(args: Union[Sequence[str], None] = None) -> bool:
    cli = get_cmd_line(args)
    detections = read_r_cnn_ab_3d_mot(cli.det_file_name)
    tracker = Ab3DMot()
    np.set_printoptions(linewidth=200, precision=3)
    result = []
    for step, det_dct in enumerate(detections.detections_3d()):
        tracker.track(det_dct)
        persistent_tracks = tracker.output()
        result.append(persistent_tracks)
        if cli.verbosity > 0:
            print(step, len(det_dct[DETS]), len(persistent_tracks))

    write_ab_3d_mot_tracking(result, cli.trk_file_name)
    print('written', cli.trk_file_name)
    return True


def main() -> None:
    run()  # pragma: no cover
