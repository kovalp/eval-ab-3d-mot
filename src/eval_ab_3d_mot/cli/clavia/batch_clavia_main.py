"""."""

from pathlib import Path
from typing import Sequence, Union

from rich.progress import Progress

from eval_ab_3d_mot.cli.common.kitti_adaptor import read_kitti_ab_3d_mot

from .cmd_line import get_cmd_line


def run(args: Union[Sequence[str], None] = None) -> bool:
    cli = get_cmd_line(args)
    category = cli.get_category()
    print(category)
    result_root = Path(cli.trk_dir) / category.value
    result_root.mkdir(exist_ok=True, parents=True)
    with Progress() as progress:
        annotations = cli.get_annotations()
        task = progress.add_task('[cyan]Working...', total=len(annotations))
        for ann_file_name in annotations:
            adaptor = read_kitti_ab_3d_mot(ann_file_name, cli.get_category())
            for ts, dct in enumerate(adaptor.detections_3d()):
                print(ts)
                print(dct)

            progress.update(task, advance=1)

    return True


def main() -> None:
    run()  # pragma: no cover
