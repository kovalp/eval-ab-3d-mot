import sys

from eval_ab_3d_mot.evaluate import evaluate


def main() -> None:
    # check for correct number of arguments. if user_sha and email are not supplied,
    # no notification email is sent (this option is used for auto-updates)
    if len(sys.argv) != 3 and len(sys.argv) != 4 and len(sys.argv) != 5:
        print(
            'Usage: python3 scripts/KITTI/evaluate.py result_sha num_hypothesis(e.g., 1) dimension(e.g., 2D or 3D) thres(e.g., 0.25)'
        )
        sys.exit(1)

    # get unique sha key of submitted results
    result_sha = sys.argv[1]
    #
    if len(sys.argv) >= 4:
        if sys.argv[3] == '2D':
            eval_3diou, eval_2diou = False, True  # eval 2d
        elif sys.argv[3] == '3D':
            eval_3diou, eval_2diou = True, False  # eval 3d
        else:
            print(
                'Usage: python3 scripts/KITTI/evaluate.py result_sha num_hypothesis(e.g., 1) dimension(e.g., 2D or 3D) thres(e.g., 0.25)'
            )
            sys.exit(1)
        if len(sys.argv) == 5:
            thres = float(sys.argv[4])
        else:
            thres = None
    else:
        eval_3diou, eval_2diou = True, False  # eval 3d
        thres = None

    evaluate(result_sha, eval_3diou, eval_2diou, thres)
