<div align="center">
    <a href="https://pypi.python.org/pypi/ChatMail">
        <img src="https://img.shields.io/pypi/v/ChatMail.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatMail/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatMail/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatMail/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md)
</div>

# ChatMail

ChatArch mail tooling package.


Documentation entry: <https://arch.gh.wzhecnu.cn/ChatMail/en/>

Choose documentation by scenario:

| Scenario | Document |
| --- | --- |
| Install the package, run the CLI, and confirm it works | `docs/cli-tree.en.md` |
| Check first-class capabilities and current boundaries | `docs/capability-map.en.md` |
| Call package behavior directly from Python | `docs/interface-tree.md` |

## Quick Start

```bash
pip install -e ".[dev]"
chatmail --help
chatmail --version
chatmail --tree
chatmail --tree-brief
python -m pytest -q
python -m build
```

## Current CLI Tree

ChatMail uses the shared `chatstyle.add_tree_option()` runtime to render full and brief trees from the registered Click command surface. The CLI is currently root-only, so both views contain the same nodes.

```text
chatmail
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## CLI Contract

ChatMail currently keeps a root-only CLI plus a typed ChatEnv configuration discovery entry point. The CLI requires `chatstyle>=0.2.0,<0.3.0`; configuration uses `chatenv>=0.2.10,<0.3.0` and ChatEnv-managed storage paths. When real interactive commands are added, use ChatStyle's `CommandSchema` / `CommandField`, `add_interactive_option()`, and `resolve_command_inputs()`; until then, do not expose scaffold/demo subcommands.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first
- `docs/`: long-lived project docs built by mkdocs

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
