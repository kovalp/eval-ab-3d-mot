"""."""

import csv

from typing import List, Union

import numpy as np


CLASS_NAMES = ['?', 'Pedestrian', 'Car', 'Cyclist']


def get_kitti_tracking(track: np.ndarray) -> List[Union[int, float, str]]:
    assert track.shape == (1, 16)
    kitti_det = track[0, 0:7]
    track_id = int(track[0, 7])
    _frame_num = int(track[0, 8])
    class_name = CLASS_NAMES[int(track[0, 9])]
    truncation, occlusion, alpha = -1, -2, -3
    bbox = track[0, 10:14].tolist()
    # xxx 14 and 15 are not used?
    header = [track_id, class_name, truncation, occlusion, alpha] + bbox
    return header + kitti_det.tolist()


def write_ab_3d_mot_tracking(result: List[List[np.ndarray]], file_name: str) -> None:
    """."""
    with open(file_name, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for step, tracks_at_time_step in enumerate(result):
            step_ls = [step]
            if len(tracks_at_time_step) > 0:
                for track in tracks_at_time_step:
                    line_ls = step_ls + get_kitti_tracking(track)
                    writer.writerow(line_ls)
