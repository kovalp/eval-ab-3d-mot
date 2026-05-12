import pytest

from eval_ab_3d_mot.cli.common.tracker_meta import TrackerMeta


@pytest.fixture
def meta() -> TrackerMeta:
    return TrackerMeta()
