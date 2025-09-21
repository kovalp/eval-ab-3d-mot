"""."""
import pytest

from eval_ab_3d_mot.box_overlap import box_overlap, Box2DAligned


@pytest.fixture
def a() -> Box2DAligned:
    return Box2DAligned(20, 30, 40, 50)


def test_box_overlap_union(a: Box2DAligned) -> None:
    assert box_overlap(a, a) == pytest.approx(1.)
    assert box_overlap(a, Box2DAligned(20, 30, 80, 90)) == pytest.approx(0.1111111111111)


def test_box_overlap_a(a: Box2DAligned) -> None:
    assert box_overlap(a, a, criterion='a') == pytest.approx(1.)
    assert box_overlap(a, Box2DAligned(20, 30, 80, 90), criterion='a') == pytest.approx(1.)


def test_unknown_criterion(a: Box2DAligned) -> None:
    with pytest.raises(TypeError):
        box_overlap(a, a, criterion='bogus')


def test_no_overlap_condition() -> None:
    a = Box2DAligned(20, 30, 20, 50)
    assert box_overlap(a, a) == pytest.approx(0.)
    a = Box2DAligned(20, 30, 40, 30)
    assert box_overlap(a, a) == pytest.approx(0.)
    assert box_overlap(a, Box2DAligned(60, 70, 80, 90)) == pytest.approx(0.)
