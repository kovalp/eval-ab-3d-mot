"""."""

from pathlib import Path

from eval_ab_3d_mot.cli.ab_3d_mot.ab_3d_mot_main import run


def test_cli_run_3d(files_dir: Path) -> None:
    """."""
    # fmt: off
    args = []
    # fmt: on
    assert run(args)
