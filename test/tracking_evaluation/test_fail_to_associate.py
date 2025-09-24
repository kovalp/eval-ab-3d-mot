"""."""
import pytest

from eval_ab_3d_mot.tracking_evaluation import TrackingEvaluation

def test_fail_to_associate(te_fail_associate: TrackingEvaluation) -> None:
    """."""
    assert te_fail_associate.compute_3rd_party_metrics()
    assert te_fail_associate.fn == 1
    assert te_fail_associate.tp == 1
    assert te_fail_associate.MOTP == pytest.approx(1.0)
    assert te_fail_associate.F1 == pytest.approx(0.5)
    assert te_fail_associate.recall == pytest.approx(0.5)
    assert te_fail_associate.precision == pytest.approx(0.5)
