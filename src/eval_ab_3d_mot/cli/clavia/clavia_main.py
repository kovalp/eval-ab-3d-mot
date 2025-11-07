"""."""

from typing import Sequence, Union

from association_quality_clavia import AssociationQuality
from binary_classification_ratios import BinaryClassificationRatios
from pure_ab_3d_mot.tracker import ANN_IDS

from eval_ab_3d_mot.cli.common.kitti_adaptor import read_kitti_ab_3d_mot

from .cmd_line_factory import get_cmd_line
from .pry_ab_3d_mot_association import pry_association
from .tracker_factory import get_tracker


def run(args: Union[Sequence[str], None] = None) -> str:
    cli = get_cmd_line(args)
    association_quality = AssociationQuality()
    for ann_file_name in cli.get_annotations():
        adaptor = read_kitti_ab_3d_mot(ann_file_name, cli.get_object_category())
        adaptor.check_and_shout_eventually(ann_file_name, cli.verbosity)
        tracker = get_tracker(cli.get_parameter_category(), cli.meta, cli.verbosity)
        for dct in adaptor.detections_3d():
            tracker.track(dct)
            pry_association(tracker.trackers, dct[ANN_IDS], association_quality)
    ratios = BinaryClassificationRatios(**association_quality.get_confusion_matrix())
    txt_summary = ratios.get_summary()
    print(txt_summary)
    return txt_summary


def main() -> None:
    run()  # pragma: no cover
