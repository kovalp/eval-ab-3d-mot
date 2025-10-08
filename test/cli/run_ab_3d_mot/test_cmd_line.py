"""."""

from eval_ab_3d_mot.cli.ab_3d_mot.cmd_line import CmdLineRunAb3dMot, get_cmd_line


def test_get_cmd_line() -> None:
    """."""
    # fmt: off
    args = []
    # fmt: on
    cli = get_cmd_line(args)
    assert isinstance(cli, CmdLineRunAb3dMot)
