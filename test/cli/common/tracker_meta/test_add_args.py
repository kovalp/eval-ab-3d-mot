from argparse import ArgumentParser

from eval_ab_3d_mot.cli.common.tracker_meta import add_args


def test_add_args() -> None:
    parser = ArgumentParser()
    add_args(parser)
    actions = {action.option_strings[0]: action for action in parser._actions}
    assert actions['--threshold'].type is float
    assert actions['--measurement-std-dev'].type is float
    assert actions['--measurement-std-dev'].default is None
    assert actions['--proc-std-dev'].type is float
    assert actions['--proc-std-dev'].default is None
    assert actions['--proc-vel-std-dev'].type is float
    assert actions['--proc-vel-std-dev'].default is None
