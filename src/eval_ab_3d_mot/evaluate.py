"""."""

import os
import sys

from .stat import Stat
from .thresholds import get_thresholds
from .tracking_evaluation import TrackingEvaluation


def evaluate(result_sha, num_hypo, eval_3diou, eval_2diou, thres):
    """
    Entry point for evaluation, will load the data and start evaluation for
    CAR and PEDESTRIAN if available.
    """

    classes = []
    # for c in ("car", "pedestrian", "cyclist"):
    for c in ('cyclist', 'pedestrian', 'car'):
        e = TrackingEvaluation(
            t_sha=result_sha,
            cls=c,
            eval_3diou=eval_3diou,
            eval_2diou=eval_2diou,
            num_hypo=num_hypo,
            thres=thres,
        )
        # load tracker data and check provided classes
        try:
            if not e.load_data(is_ground_truth=False):
                continue
            print('Loading Results - Success')
            print('Evaluate Object Class: %s' % c.upper())
            classes.append(c)
        except:  # noqa: E722
            print('Feel free to contact us (lenz@kit.edu), if you receive this error message:')
            print('   Caught exception while loading result data.')
            break
        # load groundtruth data for this class
        if not e.load_data(is_ground_truth=True):
            raise ValueError('Ground truth not found.')
        print('Loading Groundtruth - Success')
        # sanity checks
        if len(e.groundtruth) != len(e.tracker):
            print(
                'The uploaded data does not provide results for every sequence: %d vs %d'
                % (len(e.groundtruth), len(e.tracker))
            )
            return False
        print('Loaded %d Sequences.' % len(e.groundtruth))
        print('Start Evaluation...')

        if eval_3diou:
            suffix = 'eval3D'
        else:
            suffix = 'eval2D'
        filename = os.path.join(e.t_path, '../summary_%s_average_%s.txt' % (c, suffix))
        dump = open(filename, 'w+')
        stat_meter = Stat(t_sha=result_sha, cls=c, suffix=suffix)
        e.compute3rdPartyMetrics()

        # evaluate the mean average metrics
        best_mota, best_threshold = 0, -10000
        threshold_list, recall_list = get_thresholds(e.scores, e.num_gt)
        for threshold_tmp, recall_tmp in zip(threshold_list, recall_list):
            data_tmp = dict()
            e.reset()
            e.compute3rdPartyMetrics(threshold_tmp, recall_tmp)
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
            e.saveToStats(dump, threshold_tmp, recall_tmp)

        e.reset()
        e.compute3rdPartyMetrics(best_threshold)
        e.saveToStats(dump)

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


def main() -> None:
    # check for correct number of arguments. if user_sha and email are not supplied,
    # no notification email is sent (this option is used for auto-updates)
    if len(sys.argv) != 3 and len(sys.argv) != 4 and len(sys.argv) != 5:
        print(
            'Usage: python3 scripts/KITTI/evaluate.py result_sha num_hypothesis(e.g., 1) dimension(e.g., 2D or 3D) thres(e.g., 0.25)'
        )
        sys.exit(1)

    # get unique sha key of submitted results
    result_sha = sys.argv[1]
    num_hypo = sys.argv[2]
    #
    if len(sys.argv) >= 4:
        if sys.argv[3] == '2D':
            eval_3diou, eval_2diou = False, True  # eval 2d
        elif sys.argv[3] == '3D':
            eval_3diou, eval_2diou = True, False  # eval 3d
        else:
            print(
                'Usage: python3 scripts/KITTI/evaluate.py result_sha num_hypothesis(e.g., 1) dimension(e.g., 2D or 3D) thres(e.g., 0.25)'
            )
            sys.exit(1)
        if len(sys.argv) == 5:
            thres = float(sys.argv[4])
        else:
            thres = None
    else:
        eval_3diou, eval_2diou = True, False  # eval 3d
        thres = None

    evaluate(result_sha, num_hypo, eval_3diou, eval_2diou, thres)
