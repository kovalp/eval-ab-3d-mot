"""."""

from eval_ab_3d_mot.track_data import TrackData


def test_track_data() -> None:
    """."""
    t_data = TrackData()
    ref = """frame: -1
track_id: -1
obj_type: unset
truncation: -1
occlusion: -1
obs_angle: -10
x1: -1
y1: -1
x2: -1
y2: -1
w: -1
h: -1
l: -1
x: -1000
y: -1000
z: -1000
ry: -10
score: -1000
ignored: False
valid: False
tracker: -1"""
    assert str(t_data) == ref
