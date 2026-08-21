# CLI 能力地图

这篇文档是 `ChatModel` CLI 的简明能力地图，用来校对哪些命令已经是一等入口、哪些仍然只是边界或规划。

可导入 Python 函数映射见 [接口树](interface-tree.md)。当前包能力边界见 [能力地图](capability-map.md)。

## 当前 runtime 命令树

顶层 Click group 使用 `chatstyle.add_tree_option()`。`chatmodel --tree` 默认显示命令参数签名：

```text
chatmodel
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chatmodel --tree-brief` 保留命令节点和描述，但省略命令参数签名：

```text
chatmodel
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

当前 `ChatModel` 暂无业务子命令，因此两个真实 readback 都只显示无参数的 root pseudo-options，文本相同；包测试通过临时注册带参数命令验证 full/brief 差异。公共树根固定为唯一 console script 的规范名称 `chatmodel`。

## 基础入口

```text
chatmodel --help           # 验证命令已安装，并查看当前帮助
chatmodel --version        # 验证当前安装版本
chatmodel --tree           # 输出带参数签名的真实 CLI registry
chatmodel --tree-brief     # 输出省略参数签名的简洁 CLI registry
```

## 业务命令状态

当前包还没有业务子命令。新增命令前不要在文档中写模板占位或示例命令作为已实现入口；只有当命令、Python 函数和测试都存在时，才把它写成已实现入口。

## 实现合约

- 每个已实现命令都要能追到 Python 函数、类或 service 层。
- 顶层 CLI tree 统一使用 ChatStyle runtime；默认树保留参数签名，brief 树省略参数签名。
- 如果命令会写远端状态，文档必须说明凭据、权限、dry-run/checkpoint 或确认边界。
- 新增命令时，同步更新 README、接口树、能力地图、测试和相关 Flow 页面。
