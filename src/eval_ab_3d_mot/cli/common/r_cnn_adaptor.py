"""."""

from typing import Dict, Iterable

import numpy as np


DETS = 'dets'
INFO = 'info'


class RCnnAdaptor:
    def __init__(self, raw_data: np.ndarray) -> None:
        assert raw_data.ndim == 2
        assert raw_data.shape[1] == 15
        self.raw_data: np.ndarray = raw_data
        self.time_stamps = np.array(raw_data[:, 0], int)
        self.unique_tss = np.unique(self.time_stamps)
        self.last_time_stamp = np.max(self.unique_tss)

    def detections_3d(self) -> Iterable[Dict[str, np.ndarray]]:
        for ts in range(self.last_time_stamp + 1):
            ts_data = self.raw_data[self.time_stamps == ts, :]
            hwl_xyz_ry = ts_data[:, 7:14]
            info = np.zeros((ts_data.shape[0], 8))
            info[:, :7] = ts_data[:, :7]
            info[:, 7] = ts_data[:, -1]
            yield {DETS: hwl_xyz_ry, INFO: info}


def read_r_cnn_ab_3d_mot(file_name: str) -> RCnnAdaptor:
    data = np.loadtxt(file_name, delimiter=',')
    return RCnnAdaptor(data)
