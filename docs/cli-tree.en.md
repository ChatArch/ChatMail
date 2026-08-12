# CLI Tree

`ChatMail` is currently a root-only CLI. This page must stay synchronized from the real `chatmail --tree` output and must not invent future commands.

Importable Python functions are mapped in [Interface Tree](interface-tree.md). Current package boundaries are tracked in [Capability Map](capability-map.md).

## Top-Level Commands

```text
chatmail  # ChatArch mail tooling entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## Base Entries

```text
chatmail --help           # Verify the command is installed and inspect the current command tree
chatmail --version        # Verify the installed version
chatmail --tree           # Show the real CLI tree
```

`--help`, `--version`, and `--tree` are the current verification entries. After adding business commands, follow the ChatTea CLI tree pattern: split command groups into their own sections and annotate every command line.

## Current Status

| Entry | Status | Notes |
| --- | --- | --- |
| `chatmail --help` | Implemented | Shows root command help. |
| `chatmail --version` | Implemented | Shows the installed package version. |
| `chatmail --tree` | Implemented | Shows the current real CLI tree. |
| Mail tooling subcommands | Not implemented | Add them only after real mail tooling capability exists. |

## Implementation Contract

- Every implemented command must map back to a Python function, class, or service layer.
- If a command writes remote state, document credentials, permissions, dry-run/checkpoint behavior, or confirmation boundaries.
- When adding a command, update README, the interface tree, capability map, tests, and related flow pages together.
