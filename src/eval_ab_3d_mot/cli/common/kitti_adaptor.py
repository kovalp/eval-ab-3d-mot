"""."""

from typing import Dict, Iterable

import numpy as np

from pure_ab_3d_mot.str_const import ANN_IDS, DETS, INFO

from eval_ab_3d_mot.kitti_category import KittiCategory


def get_category_mask(category_l: np.ndarray, category: KittiCategory) -> np.ndarray:
    kitti_labels = category.get_kitti_labels()
    category_mask = np.equal(category_l, kitti_labels[0])
    if len(kitti_labels) == 2:
        category_mask |= np.equal(category_l, kitti_labels[1])
    return category_mask


class KittiAdaptor:
    def __init__(
        self,
        stamps_l: np.ndarray,
        ids_l: np.ndarray,
        category_l: np.ndarray,
        detections_l: np.ndarray,
        category: KittiCategory,
    ) -> None:
        self.last_time_stamp = np.max(stamps_l)
        category_mask = get_category_mask(category_l, category)
        self.time_stamps = stamps_l[category_mask]
        self.ann_ids = ids_l[category_mask]
        self.detections = detections_l[category_mask]
        self.stamp_mask_buf = np.zeros(len(self.ann_ids), bool)

    def detections_3d(self) -> Iterable[Dict[str, np.ndarray]]:
        for ts in range(self.last_time_stamp + 1):
            np.equal(self.time_stamps, ts, out=self.stamp_mask_buf)
            hwl_xyz_ry = self.detections[self.stamp_mask_buf]
            info = np.zeros((hwl_xyz_ry.shape[0], 8))
            ids_r = self.ann_ids[self.stamp_mask_buf]
            yield {DETS: hwl_xyz_ry, INFO: info, ANN_IDS: ids_r}


def read_kitti_ab_3d_mot(file_name: str, category: KittiCategory) -> KittiAdaptor:
    stamps_l, ids_l = np.genfromtxt(file_name, delimiter=' ', usecols=(0, 1), dtype=int).T
    category_l = np.genfromtxt(file_name, delimiter=' ', usecols=(2,), dtype=str)
    detections_l = np.genfromtxt(file_name, delimiter=' ')[:, 10:]
    return KittiAdaptor(stamps_l, ids_l, category_l, detections_l, category)
