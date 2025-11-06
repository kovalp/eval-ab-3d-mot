"""."""

from typing import List

from eval_ab_3d_mot.kitti_category import KittiCategory


AUTO = 'auto'


class CmdLineRunWithClavIA:
    def __init__(self) -> None:
        self.verbosity = 0
        self.annotations: List[str] = []
        self.category_obj = KittiCategory.CAR.value
        self.category_prm = AUTO
        self.threshold = 1000.0
        self.max_age = -1
        self.metric = AUTO
        self.algorithm = AUTO

    def __repr__(self) -> str:
        return (
            'CmdLineBatchRunWithClavIA('
            f'category-obj {self.category_obj} '
            f'category-prm {self.category_prm})'
        )

    def get_object_category(self) -> KittiCategory:
        return KittiCategory(self.category_obj)

    def get_parameter_category(self) -> KittiCategory:
        if self.category_prm == AUTO:
            result = KittiCategory(self.category_obj)
        else:
            result = KittiCategory(self.category_prm)
        return result

    def get_annotations(self) -> List[str]:
        return sorted(self.annotations)
