"""."""

import pytest

from binary_classification_ratios import BinaryClassificationRatios
from pure_ab_3d_mot.clavia_conventions import UPD_ID_LOOSE

from eval_ab_3d_mot.association_quality import AssociationQuality


@pytest.fixture
def aq() -> AssociationQuality:
    """."""
    return AssociationQuality()


def test_reset(aq: AssociationQuality) -> None:
    """."""
    aq.num_tp = 1
    aq.num_fp = 2
    aq.num_fn = 3
    aq.num_tn = 4
    aq.reset()
    assert repr(aq) == 'AssociationQuality(TP 0 TN 0 FP 0 FN 0)'


def test_classify_case1234(aq: AssociationQuality) -> None:
    """."""
    aq.classify(0, 0, True)
    assert repr(aq) == 'AssociationQuality(TP 1 TN 0 FP 0 FN 0)'
    aq.classify(0, 1, True)
    assert repr(aq) == 'AssociationQuality(TP 1 TN 0 FP 0 FN 1)'
    aq.classify(0, -1, True)
    assert repr(aq) == 'AssociationQuality(TP 1 TN 0 FP 0 FN 2)'
    aq.classify(0, UPD_ID_LOOSE, True)
    assert repr(aq) == 'AssociationQuality(TP 1 TN 0 FP 0 FN 3)'
    with pytest.raises(RuntimeError):
        aq.classify(0, -2, True)
    with pytest.raises(RuntimeError):
        aq.classify(1, -2, True)


def test_classify_case5678(aq: AssociationQuality) -> None:
    """."""
    with pytest.raises(RuntimeError):
        aq.classify(1, 1, False)
    aq.classify(1, 2, False)
    assert repr(aq) == 'AssociationQuality(TP 0 TN 0 FP 1 FN 0)'
    aq.classify(1, -1, False)
    assert repr(aq) == 'AssociationQuality(TP 0 TN 0 FP 2 FN 0)'
    aq.classify(1, UPD_ID_LOOSE, False)
    assert repr(aq) == 'AssociationQuality(TP 0 TN 1 FP 2 FN 0)'


def test_classify_case9_10_11_12(aq: AssociationQuality) -> None:
    """."""
    aq.classify(-1, 1, False)
    assert repr(aq) == 'AssociationQuality(TP 0 TN 0 FP 1 FN 0)'
    aq.classify(-1, -1, False)
    assert repr(aq) == 'AssociationQuality(TP 0 TN 1 FP 1 FN 0)'
    aq.classify(-1, UPD_ID_LOOSE, False)
    assert repr(aq) == 'AssociationQuality(TP 0 TN 2 FP 1 FN 0)'
    with pytest.raises(RuntimeError):
        aq.classify(-1, -2, False)


def test_classify_exception5(aq: AssociationQuality) -> None:
    """."""
    with pytest.raises(RuntimeError):
        aq.classify(-2, 0, False)


def test_classify_exception3(aq: AssociationQuality) -> None:
    """."""
    with pytest.raises(RuntimeError):
        aq.classify(2, -567, False)


def test_get_classification_ratios(aq: AssociationQuality) -> None:
    """."""
    ratios = aq.get_classification_ratios()
    assert isinstance(ratios, BinaryClassificationRatios)
