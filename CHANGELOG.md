# Changelog

## 2026-08-21

### Added

- 新增顶层 `chatmodel --tree-brief`，保留命令节点与描述并省略参数签名。

### Changed

- 将包版本提升到 `0.1.2`，顶层 `--tree` 迁移到 ChatStyle 共享 Click tree runtime；默认输出参数签名。
- 将依赖窗口更新为 `chatstyle>=0.2.0,<0.3.0` 和 `chatenv>=0.2.10,<0.3.0`。
- 移除本地 CLI tree renderer，并固定公共树根名为规范命令名 `chatmodel`。

## 2026-08-11

### Added

- 发布 `ChatModel` patch `0.1.1`，新增真实 Click registry 生成的顶层 `chatmodel --tree`。
- CLI 树文档现在记录当前真实空业务命令面，只展示 root pseudo-options，不再保留模板占位。

### Changed

- 将 ChatEnv 依赖下界提升到已发布 rollout 基线 `>=0.2.4,<0.3.0`。
- 将 MkDocs Material 文档依赖收紧到当前 strict-build 验证窗口。

## 2026-08-06

### Added

- 发布 `ChatModel` 首个 ChatArch Python 包验证版本 `0.1.0`。
- 包含基础 CLI、ChatEnv provider、测试、MkDocs 文档站 scaffold 与 PyPI Trusted Publisher tag-driven 发布工作流。

### Changed

- 将发布工作流固定为 tag-only，并要求 tag 与包版本一致。

### Fixed

- N/A
