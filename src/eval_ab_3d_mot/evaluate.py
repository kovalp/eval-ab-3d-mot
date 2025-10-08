"""."""

import os

from typing import Dict, Sequence, Union

from eval_ab_3d_mot.core.tracking_evaluation import TrackingEvaluation

from .raise_if_sick import raise_if_sick
from .stat import Stat
from .thresholds import get_thresholds


def evaluate(
    result_sha: str,
    eval_3diou: bool,
    eval_2diou: bool,
    threshold: Union[float, None],
    ann_root: str,
    res_root: str,
    seq_lengths_name: Dict[str, int],
    target_classes: Sequence[str],
) -> bool:
    """
    Entry point for evaluation, will load the data and start evaluation for
    CAR and PEDESTRIAN if available.
    """

    classes = []
    for c in target_classes:
        e = TrackingEvaluation(
            result_sha,
            seq_lengths_name,
            ann_root=ann_root,
            res_root=res_root,
            cls=c,
            eval_3diou=eval_3diou,
            eval_2diou=eval_2diou,
            thres=threshold,
        )
        # load tracker data and check provided classes
        try:
            e.load_data(is_ground_truth=False)
            print('Loading Results - Success')
            print('Evaluate Object Class: %s' % c.upper())
            classes.append(c)
        except IOError as exception:  # noqa: E722
            print('Feel free to contact us (lenz@kit.edu), if you receive this error message:')
            print('   Caught exception while loading result data.')
            print(exception)
            break
        e.load_data(is_ground_truth=True)  # load ground-truth data for this class
        # sanity checks
        raise_if_sick(len(e.ground_truth), len(e.tracker))
        print('Loaded %d Sequences.' % len(e.ground_truth))
        print('Start Evaluation...')

        suffix = 'eval_3d' if eval_3diou else 'eval_2d'
        filename = os.path.join(e.t_path, '../summary_%s_average_%s.txt' % (c, suffix))
        dump = open(filename, 'w+')
        stat_meter = Stat(t_sha=result_sha, cls=c)
        e.compute_3rd_party_metrics()

        # evaluate the mean average metrics
        best_mota, best_threshold = 0, -10000
        threshold_list, recall_list = get_thresholds(e.scores, e.num_gt)
        for threshold_tmp, recall_tmp in zip(threshold_list, recall_list):
            data_tmp = dict()
            e.reset()
            e.compute_3rd_party_metrics(threshold_tmp, recall_tmp)
            (
                data_tmp['mota'],
                data_tmp['motp'],
                data_tmp['moda'],
                data_tmp['modp'],
                data_tmp['precision'],
                data_tmp['F1'],
                data_tmp['fp'],
                data_tmp['fn'],
                data_tmp['recall'],
                data_tmp['sMOTA'],
            ) = e.MOTA, e.MOTP, e.MODA, e.MODP, e.precision, e.F1, e.fp, e.fn, e.recall, e.sMOTA
            stat_meter.update(data_tmp)
            mota_tmp = e.MOTA
            if mota_tmp > best_mota:
                best_threshold = threshold_tmp
                best_mota = mota_tmp
            e.save_to_stats(dump, threshold_tmp, recall_tmp)

        e.reset()
        e.compute_3rd_party_metrics(best_threshold)
        e.save_to_stats(dump)

        stat_meter.output()
        summary = stat_meter.get_summary()
        print(summary)  # mail or print the summary.
        dump.close()

    # finish
    if len(classes) == 0:
        print('The uploaded results could not be evaluated. Check for format errors.')
        return False
    print('Thank you for participating in our benchmark!')
    return True
