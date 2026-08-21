"""CLI entrypoint for chatmodel."""

import click
from chatstyle import add_tree_option

from chatmodel import __version__


@click.group(name="chatmodel")
@click.version_option(__version__, prog_name="chatmodel")
@add_tree_option(renderer_options={"root_name": "chatmodel"})
def main() -> None:
    """chatmodel command line interface."""
    # Add package-specific commands here. Prefer ChatStyle helpers for
    # interactive input when a command needs recoverable user input.


if __name__ == "__main__":
    main()
