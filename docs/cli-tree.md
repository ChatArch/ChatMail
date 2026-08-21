# CLI 树

`ChatMail` 当前是 root-only CLI，并使用共享的 `chatstyle.add_tree_option()` 从真实注册的 Click command surface 生成命令树：

- `chatmail --tree` 显示参数签名，适合接口审查。
- `chatmail --tree-brief` 保留同一组节点和说明，但省略参数签名。

当前没有业务命令参数，因此完整和简洁视图相同。这个页面不能手写未来命令。

可导入 Python 函数映射见 [接口树](interface-tree.md)。当前包能力边界见 [能力地图](capability-map.md)。

## 完整命令树

```text
chatmail
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## 简洁命令树

```text
chatmail
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## 基础入口

```text
chatmail --help           # 验证命令已安装，并查看当前命令树
chatmail --version        # 验证当前安装版本
chatmail --tree           # 显示带参数签名的真实注册树
chatmail --tree-brief     # 显示省略参数签名的同一注册树
```

`--help`、`--version`、`--tree` 和 `--tree-brief` 是当前可验证入口。新增业务命令后，应把命令组单独展开，并给每个命令写一行说明。

## 当前状态

| 入口 | 状态 | 说明 |
| --- | --- | --- |
| `chatmail --help` | 已实现 | 显示根命令帮助。 |
| `chatmail --version` | 已实现 | 显示已安装包版本。 |
| `chatmail --tree` | 已实现 | 显示包含参数签名的真实注册树。 |
| `chatmail --tree-brief` | 已实现 | 显示省略参数签名的同一注册树。 |
| Mail tooling 子命令 | 尚未实现 | 未来有真实 mail tooling 能力后再加入 CLI。 |

## 实现合约

- 每个已实现命令都要能追到 Python 函数、类或 service 层。
- 如果命令会写远端状态，文档必须说明凭据、权限、dry-run/checkpoint 或确认边界。
- 新增命令时，先更新 Click 注册面和测试，再运行 `chatmail --tree` 与 `chatmail --tree-brief` 回填 README、本页、接口树和能力地图。
