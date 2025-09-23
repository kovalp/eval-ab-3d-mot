"""."""

from typing import Tuple, List

import numpy as np

from eval_ab_3d_mot.stat import NUM_SAMPLE_POINTS


def get_thresholds(scores: List[float],
                   num_gt: int,
                   num_sample_pts=NUM_SAMPLE_POINTS
                   ) -> Tuple[List[float], List[float]]:
    # based on score of true positive to discretize the recall
    # not necessarily have data on all points due to not fully recall the results, all the results point has zero precision
    # compute the recall based on the gt positives

    # scores: the list of scores of the matched true positives

    scores = np.array(scores)
    scores.sort()
    scores = scores[::-1]
    current_recall = 0
    thresholds = []
    recalls = []
    for i, score in enumerate(scores):
        l_recall = (i + 1) / float(num_gt)
        if i < (len(scores) - 1):
            r_recall = (i + 2) / float(num_gt)
        else:
            r_recall = l_recall
        if ((r_recall - current_recall) < (current_recall - l_recall)) and (
                i < (len(scores) - 1)
        ):
            continue

        thresholds.append(score)
        recalls.append(current_recall)
        current_recall += 1 / (num_sample_pts - 1.0)

    return thresholds[1:], recalls[1:]  # throw the first one with 0 recall
