"""."""
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Sequence, Union

import numpy as np

from .cmd_line import get_cmd_line
from eval_ab_3d_mot.core.tracking_evaluation import TrackingEvaluation
from eval_ab_3d_mot.stat import Stat


def run(args: Union[Sequence[str], None] = None) -> bool:
    cli = get_cmd_line(args)
    ann_path = Path(cli.ann_file_name)
    if ann_path.suffix != '.txt':
        raise ValueError('The suffix (extension) should be .txt')

    seq_name = ann_path.with_suffix('').name
    frame_numbers = np.genfromtxt(ann_path, usecols=[0], dtype=int)
    seq_lengths_name = {seq_name: np.max(frame_numbers) + 1}

    trk_path = Path(cli.trk_file_name)
    category = trk_path.read_text().splitlines()[0].split()[2].lower()
    trk_eval = TrackingEvaluation('single-sequence', seq_lengths_name, cls=category)
    trk_eval.gt_path = str(ann_path.parent)
    trk_eval.load_data(True)

    with TemporaryDirectory(delete=False) as tmpdir:
        tmp_file_path = (Path(tmpdir) / seq_name).with_suffix('.txt')
        shutil.copy(trk_path, tmp_file_path)
        trk_eval.t_path = str(tmp_file_path.parent)
        trk_eval.load_data(False)

    trk_eval.compute_3rd_party_metrics()

    # evaluate the mean average metrics
    best_mota, best_threshold = 0, -10000
    threshold_list, recall_list = get_thresholds(trk_eval.scores, trk_eval.num_gt)
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
    stat_meter = Stat(t_sha='single-sequence', cls=category)

    return True


def main() -> None:
    run()  # pragma: no cover
