"""."""

from eval_ab_3d_mot.track_data import TrackData


def test_track_data() -> None:
    """."""
    t_data = TrackData()
    ref = """x: -1000
y: -1000
z: -1000
h: -1
w: -1
l: -1
ry: -10
s: -1000
frame: -1
track_id: -1
obj_type: unset
truncation: -1
occlusion: -1
obs_angle: -10
x1: -1
y1: -1
x2: -1
y2: -1
ignored: False
valid: False
tracker: -1
distance: 0.0"""
    assert str(t_data) == ref


def test_track_data_repr() -> None:
    """."""
    t_data = TrackData(track_id=123, frame=456, x=1, y=2, z=3)
    assert t_data.__repr__() == 'Track(id 123 frame 456 x 1 y 2 z 3)'
