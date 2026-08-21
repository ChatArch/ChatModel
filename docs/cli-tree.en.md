# CLI Capability Map

This page is the compact capability map for the `ChatModel` CLI. Use it to review which commands are first-class entries and which are still boundary or planned slots.

Importable Python functions are mapped in [Interface Tree](interface-tree.md). Current package boundaries are tracked in [Capability Map](capability-map.md).

## Current Runtime Command Tree

The top-level Click group uses `chatstyle.add_tree_option()`. `chatmodel --tree` includes command parameter signatures by default:

```text
chatmodel
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chatmodel --tree-brief` keeps command nodes and descriptions but omits command parameter signatures:

```text
chatmodel
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`ChatModel` currently has no business subcommands, so both real readbacks contain only parameterless root pseudo-options and are textually identical. Package tests temporarily register a parameterized command to verify the full/brief difference. The public root is fixed to `chatmodel`, the canonical name of the sole console script.

## Base Entries

```text
chatmodel --help           # Verify the command is installed and inspect current help
chatmodel --version        # Verify the installed version
chatmodel --tree           # Print the real CLI registry with parameter signatures
chatmodel --tree-brief     # Print the concise CLI registry without parameter signatures
```

## Business Command Status

This package currently has no business subcommands. Do not document template placeholders or sample commands as available entries. Only document a command as implemented after the command, Python function, and tests exist.

## Implementation Contract

- Every implemented command must map back to a Python function, class, or service layer.
- Use the shared ChatStyle runtime for the top-level CLI tree; keep signatures in the default tree and omit them in the brief tree.
- If a command writes remote state, document credentials, permissions, dry-run/checkpoint behavior, or confirmation boundaries.
- When adding a command, update README, the interface tree, capability map, tests, and related flow pages together.
