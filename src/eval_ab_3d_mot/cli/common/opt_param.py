"""."""

from pure_ab_3d_mot.dist_metrics import MetricKind
from pure_ab_3d_mot.matching import MatchingAlgorithm
from pure_ab_3d_mot.tracker import Ab3DMot
from eval_ab_3d_mot.kitti_category import KittiCategory


def fill_r_cnn_opt_param(category: KittiCategory, tracker: Ab3DMot) -> None:
    if category == category.CAR:
        tracker.algorithm = MatchingAlgorithm.HUNGARIAN
        tracker.metric = MetricKind.GIOU_3D
        tracker.threshold = -0.2
        tracker.min_hits = 3
        tracker.max_age = 2
    elif category == category.PEDESTRIAN:
        tracker.algorithm = MatchingAlgorithm.GREEDY
        tracker.metric = MetricKind.GIOU_3D
        tracker.threshold = -0.4
        tracker.min_hits = 1
        tracker.max_age = 4
    elif category == category.CYCLIST:
        tracker.algorithm = MatchingAlgorithm.HUNGARIAN
        tracker.metric = MetricKind.DIST_3D
        tracker.threshold = -2.0
        tracker.min_hits = 3
        tracker.max_age = 4
