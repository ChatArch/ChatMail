# Changelog

## 0.1.2 - 2026-08-22

### Added

- Added `chatmail --tree-brief`, which renders the same registered command surface without parameter signatures.
- Added full/brief tree contract tests and installed console-script plus wheel CI readbacks across Python 3.10-3.12.

### Changed

- Replaced the package-local tree renderer with ChatStyle `add_tree_option()` and made the public `chatmail` root name explicit.
- Aligned runtime dependencies to `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.10,<0.3.0`.
- Synchronized bilingual CLI documentation with the registered runtime output and bounded supported Click/MkDocs Material versions.

## 0.1.1 - 2026-08-12

### Added

- Added real root-only `chatmail --tree` generated from the Click command surface.
- Added CLI and workflow/docs contract tests for the tree, docs, and tag-only OIDC publish path.

### Changed

- Removed unused ChatStyle runtime dependency while preserving the ChatEnv provider entry point.
- Enabled MkDocs Material emoji renderer gate and broadened the Material docs upper bound to `<10.0`.
- Hardened tag-only OIDC publish workflow guard.

## 0.1.0 - 2026-07-05

### Added

- Publish the first formal ChatMail package release with the ChatArch CLI scaffold.

## YYYY-MM-DD

### Added

### Changed

### Fixed
