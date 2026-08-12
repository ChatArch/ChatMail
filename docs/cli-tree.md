# CLI 树

`ChatMail` 当前是 root-only CLI。这个页面必须从真实 `chatmail --tree` 输出同步，不能手写未来命令。

可导入 Python 函数映射见 [接口树](interface-tree.md)。当前包能力边界见 [能力地图](capability-map.md)。

## 顶层命令

```text
chatmail  # ChatArch mail tooling entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## 基础入口

```text
chatmail --help           # 验证命令已安装，并查看当前命令树
chatmail --version        # 验证当前安装版本
chatmail --tree           # 显示真实 CLI 树
```

`--help`、`--version` 和 `--tree` 是当前可验证入口。新增业务命令后，应像 ChatTea 的 CLI 树一样，把命令组单独展开，并给每个命令写一行注释。

## 当前状态

| 入口 | 状态 | 说明 |
| --- | --- | --- |
| `chatmail --help` | 已实现 | 显示根命令帮助。 |
| `chatmail --version` | 已实现 | 显示已安装包版本。 |
| `chatmail --tree` | 已实现 | 显示当前真实 CLI 树。 |
| Mail tooling 子命令 | 尚未实现 | 未来有真实 mail tooling 能力后再加入 CLI。 |

## 实现合约

- 每个已实现命令都要能追到 Python 函数、类或 service 层。
- 如果命令会写远端状态，文档必须说明凭据、权限、dry-run/checkpoint 或确认边界。
- 新增命令时，同步更新 README、接口树、能力地图、测试和相关 Flow 页面。
