"""CLI entrypoint for chatmail."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatmail import __version__


@click.group(name="chatmail", invoke_without_command=True)
@click.version_option(__version__, prog_name="chatmail")
@add_tree_option(renderer_options={"root_name": "chatmail"})
@click.pass_context
def main(ctx: click.Context) -> None:
    """ChatArch mail tooling entrypoint."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


if __name__ == "__main__":
    main()
