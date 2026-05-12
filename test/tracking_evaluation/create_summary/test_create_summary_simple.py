"""."""

from eval_ab_3d_mot.core.tracking_evaluation import TrackingEvaluation


def test_create_summary_simple(te_sum: TrackingEvaluation) -> None:
    """."""
    summary = te_sum.create_summary_simple(2.0, 0.234)
    ref = """=========evaluation with confidence threshold 2.000000, recall 0.234000=========
 sMOTA     MOTA     MOTP      MT       ML       IDS  FRAG    F1     Prec    Recall    FAR       TP    FP    FN
0.100000 0.200000 0.300000 45.000000 34.000000   123   432 0.600000 0.800000 0.900000 0.700000   456   126   789
================================================================================"""
    assert summary == ref
