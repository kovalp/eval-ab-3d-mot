"""."""

from eval_ab_3d_mot.core.tracking_evaluation import TrackingEvaluation
from eval_ab_3d_mot.raise_if_sick import raise_if_sick
from eval_ab_3d_mot.stat import Stat
from eval_ab_3d_mot.thresholds import get_thresholds


def evaluate_and_report(e: TrackingEvaluation, c: str, result_sha: str, filename: str) -> None:
    # sanity checks
    raise_if_sick(len(e.ground_truth), len(e.tracker))
    print('Loaded %d Sequences.' % len(e.ground_truth))
    print('Start Evaluation...')

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
