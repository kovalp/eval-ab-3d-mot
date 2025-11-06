"""."""

from pathlib import Path
from typing import Sequence, Union

from association_quality_clavia import AssociationQuality
from binary_classification_ratios import BinaryClassificationRatios
from pure_ab_3d_mot.str_const import ANN_IDS
from pure_ab_3d_mot.tracker import Ab3DMot

from eval_ab_3d_mot.cli.common.kitti_adaptor import read_kitti_ab_3d_mot
from eval_ab_3d_mot.cli.common.opt_param import fill_r_cnn_opt_param

from .cmd_line import get_cmd_line


def run(args: Union[Sequence[str], None] = None) -> bool:
    cli = get_cmd_line(args)
    category = cli.get_category()
    print('Tracking of', category)
    result_root = Path(cli.trk_dir) / category.value
    result_root.mkdir(exist_ok=True, parents=True)
    annotations = cli.get_annotations()
    association_quality = AssociationQuality()
    for ann_file_name in annotations:
        print('Tracking in', ann_file_name)
        adaptor = read_kitti_ab_3d_mot(ann_file_name, cli.get_category())
        tracker = Ab3DMot()
        fill_r_cnn_opt_param(category, tracker)
        for ts, dct in enumerate(adaptor.detections_3d()):
            print('    ', ts)
            tracker.track(dct)
            for target in tracker.trackers:
                is_supplied = True in dct[ANN_IDS]
                association_quality.classify(target.ann_id, target.upd_id, is_supplied)
    confusion_matrix = association_quality.get_confusion_matrix()
    ratios = BinaryClassificationRatios(**confusion_matrix)
    print(ratios.get_summary())
    return True


def main() -> None:
    run()  # pragma: no cover
