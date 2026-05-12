"""."""

from eval_ab_3d_mot.core.tracking_evaluation import TrackingEvaluation
from eval_ab_3d_mot.evaluate_and_report import evaluate_and_report


def test_evaluate_and_report(te: TrackingEvaluation) -> None:
    evaluate_and_report(te, 't-sha', 'filename', True)
