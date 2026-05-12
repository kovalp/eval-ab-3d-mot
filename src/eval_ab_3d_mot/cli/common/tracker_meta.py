"""."""

from argparse import ArgumentParser

from pure_ab_3d_mot.dist_metrics import MetricKind
from pure_ab_3d_mot.matching import MatchingAlgorithm
from pydantic import BaseModel

from .get_hlp import get_hlp


AUTO = 'auto'

HLP_THR = 'Association threshold.'
HLP_ALG = 'Association algorithm.'
HLP_MET = 'Association metric.'
HLP_MAX = 'Maximal number of steps without association.'
HLP_R_STD_DEV = 'Measurement standard deviation.'
HLP_Q_STD_DEV = 'Process-noise standard deviation.'
HLP_QV_STD_DEV = 'Velocity part standard deviation in process noise.'
DEF_POLICY = 'If not given the category-dependent optimal will be used.'


class TrackerMeta(BaseModel):
    threshold: float = 1000.0
    max_age: int = -1
    metric: str = AUTO
    algorithm: str = AUTO
    measurement_std_dev: float = 1.0
    proc_std_dev: float = 1.0
    proc_vel_std_dev: float = 0.1


def add_args(parser: ArgumentParser) -> None:
    parser.add_argument('--threshold', '-t', type=float, help=get_hlp(HLP_THR, DEF_POLICY))
    parser.add_argument('--max-age', '-x', type=int, help=get_hlp(HLP_MAX, DEF_POLICY))
    aa = (MatchingAlgorithm.HUNGARIAN.value, MatchingAlgorithm.GREEDY.value) + (AUTO,)
    parser.add_argument('--algorithm', '-a', choices=aa, help=get_hlp(HLP_ALG, DEF_POLICY))
    mm = tuple(c.value for c in MetricKind if c != MetricKind.UNKNOWN) + (AUTO,)
    parser.add_argument('--metric', '-m', choices=mm, help=get_hlp(HLP_MET, DEF_POLICY))
    parser.add_argument('--measurement-std-dev', type=float, help=get_hlp(HLP_R_STD_DEV, 1.0))
    parser.add_argument('--proc-std-dev', type=float, help=get_hlp(HLP_Q_STD_DEV, 1.0))
    parser.add_argument('--proc-vel-std-dev', type=float, help=get_hlp(HLP_QV_STD_DEV, 0.1))
