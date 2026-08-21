# CLI Tree

`ChatMail` is currently a root-only CLI and uses the shared `chatstyle.add_tree_option()` runtime to render the registered Click command surface:

- `chatmail --tree` includes parameter signatures for interface review.
- `chatmail --tree-brief` preserves the same nodes and descriptions without parameter signatures.

There are no business-command parameters yet, so the full and brief views are identical. This page must not invent future commands.

Importable Python functions are mapped in [Interface Tree](interface-tree.md). Current package boundaries are tracked in [Capability Map](capability-map.md).

## Full Command Tree

```text
chatmail
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## Brief Command Tree

```text
chatmail
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## Base Entries

```text
chatmail --help           # Verify the command is installed and inspect the current command tree
chatmail --version        # Verify the installed version
chatmail --tree           # Show the registered tree with parameter signatures
chatmail --tree-brief     # Show the same registered tree without parameter signatures
```

`--help`, `--version`, `--tree`, and `--tree-brief` are the current verification entries. After adding business commands, split command groups into their own sections and give every command a one-line description.

## Current Status

| Entry | Status | Notes |
| --- | --- | --- |
| `chatmail --help` | Implemented | Shows root command help. |
| `chatmail --version` | Implemented | Shows the installed package version. |
| `chatmail --tree` | Implemented | Shows the registered tree with parameter signatures. |
| `chatmail --tree-brief` | Implemented | Shows the same registered tree without parameter signatures. |
| Mail tooling subcommands | Not implemented | Add them only after real mail tooling capability exists. |

## Implementation Contract

- Every implemented command must map back to a Python function, class, or service layer.
- If a command writes remote state, document credentials, permissions, dry-run/checkpoint behavior, or confirmation boundaries.
- When adding a command, update the Click registry and tests first, then run `chatmail --tree` and `chatmail --tree-brief` to refresh README, this page, the interface tree, and capability map.
