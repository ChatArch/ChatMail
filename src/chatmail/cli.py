"""CLI entrypoint for chatmail."""

import click

from chatmail import __version__


@click.group()
@click.version_option(__version__, prog_name="chatmail")
def main() -> None:
    """chatmail command line interface."""
    # Add package-specific commands here. Prefer ChatStyle helpers for
    # interactive input when a command needs recoverable user input.


if __name__ == "__main__":
    main()
