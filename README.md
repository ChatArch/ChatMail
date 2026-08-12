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

[英文版](README.en.md) | [简体中文](README.md)
</div>

# ChatMail

ChatArch mail tooling package.


文档入口：<https://arch.gh.wzhecnu.cn/ChatMail/>

按场景选择文档：

| 场景 | 文档 |
| --- | --- |
| 第一次安装、运行命令行、确认包可用 | [CLI 树](docs/cli-tree.md) |
| 校对当前包有哪些一等能力和边界 | [能力地图](docs/capability-map.md) |
| 从 Python 代码调用包能力 | [接口树](docs/interface-tree.md) |

## 快速开始

```bash
pip install -e ".[dev]"
chatmail --help
chatmail --version
chatmail --tree
python -m pytest -q
python -m build
```

## 当前 CLI 树

```text
chatmail  # ChatArch mail tooling entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## 命令行规范

ChatMail 当前保留 root-only CLI 和 ChatEnv 配置发现入口。新增交互式命令时，应重新引入并使用 ChatStyle 的 `CommandSchema` / `CommandField`、`add_interactive_option()` 与 `resolve_command_inputs()`；没有真实交互命令前，不暴露 scaffold/demo 子命令。

## 目录结构

- `src/`：包源码
- `tests/code-tests/`：代码测试和历史测试迁移
- `tests/cli-tests/`：真实 CLI 测试，doc-first
- `tests/mock-cli-tests/`：mock/fake CLI 测试，doc-first
- `docs/`：长期维护文档，由 mkdocs 构建

## 开发说明

扩展脚手架前，先阅读 `DEVELOP.md` 和 `AGENTS.md`。
