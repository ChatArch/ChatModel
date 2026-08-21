import click
from click.testing import CliRunner

from chatmodel import __version__
from chatmodel.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatmodel, version {__version__}" in result.output


def test_help_lists_tree_options_without_fake_commands():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output
    assert "--tree-brief" in result.output
    assert "hello" not in result.output.lower()
    assert "<group>" not in result.output


def test_tree_option_renders_registered_empty_command_surface():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0, result.output
    assert result.output.splitlines()[0] == "chatmodel"
    assert "├── --help  # Show this message and exit." in result.output
    assert "├── --version  # Show the version and exit." in result.output
    assert "├── --tree  # Print the registered CLI tree and exit." in result.output
    assert "└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit." in result.output
    assert "hello" not in result.output.lower()
    assert "<group>" not in result.output


def test_tree_defaults_to_signatures_and_brief_omits_them():
    @click.command(name="inspect", help="Inspect a model.")
    @click.argument("model")
    @click.option("--format", "output")
    def inspect(model: str, output: str | None) -> None:
        pass

    main.add_command(inspect)
    try:
        full = CliRunner().invoke(main, ["--tree"])
        brief = CliRunner().invoke(main, ["--tree-brief"])
    finally:
        main.commands.pop("inspect")

    assert full.exit_code == 0, full.output
    assert brief.exit_code == 0, brief.output
    assert "inspect <MODEL> [--format OUTPUT]  # Inspect a model." in full.output
    assert "inspect  # Inspect a model." in brief.output
    assert "<MODEL>" not in brief.output
    assert "[--format OUTPUT]" not in brief.output
