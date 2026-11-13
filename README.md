# Arabic Learning

[下载 Android APK](https://github.com/Fankikotan/Arabic_Learning_App/releases/download/v0.2.2/Arabic-Learning-v0.2.2.apk) · [Release 与校验文件](https://github.com/Fankikotan/Arabic_Learning_App/releases/tag/v0.2.2)

手机优先的阿拉伯语学习软件。已内置 12 课入门教材、194 词《渔夫与精灵》、配套词本、章节语法、翻译、385 段真实音频和阿英词典，无需额外导入。

## Android 安装

下载上方 APK，在 Android 7.0+ 设备允许当前来源安装后打开。正式签名 release v0.2.2，约 15.9MB。校验和与公开签名摘要随 Release 提供。已通过 API 37 模拟器安装、启动与蓝色桌面图标切换检查；不同实体机、后台音频与文件导出仍需实机确认。

## 运行源码

需要 Node.js 22+：

```powershell
npm ci
npm start
```

打开 http://localhost:4173 。仅运行网页也可 `node scripts/serve.mjs`，无需 Android 工具。

## 开发与构建

```powershell
npm run check
npm run android:sync
npm run android:open
```

Android 使用 Java 21、SDK 36；本机 SDK 路径不提交。正式签名密钥由项目所有者保管，不在仓库中。完整网页包可由 `python scripts/package-mobile.py` 生成。

## 文档

- [使用说明](使用说明.md)
- [打包与发布流程](APK打包与发布.md)
- [项目具体设计](项目具体设计.md)
- [通用设计规范](语言学习网页设计规范.md)
- [材料包格式](材料包格式.md)
- [交付配置](material-delivery.config.json)
- [项目进度](项目进度与讨论.md)
- [Android 准备记录](Android打包准备.md)
- [词典及依赖来源与许可](app/THIRD-PARTY-NOTICES.md)

词典文本来自 Wiktionary / Kaikki，按 CC BY-SA 4.0 保留归属与修改说明。其他代码和资源许可分别说明。仓库不含个人学习档案、独立技能、签名密钥或本机运行缓存。Release 中的源码 ZIP 为构建时快照；最新文档以 main 分支为准。


## v0.2.2：例句显示控制

词汇页右上角打开“通用词汇显示设置”：例句原文通过独立勾选项控制；例句翻译可选择默认显示、点击显示或不显示。设置同时适用于条目和卡片、词本/最近接触/收藏/我的学习。关闭原文不再强制关闭翻译，关闭翻译也不隐藏原文。

v0.2.2 使用 versionCode 2 与原有签名密钥，可覆盖安装 v0.2.0；旧版 Release 保留。浏览器已检查原文开关与翻译三种模式的全部六种组合。


## v0.2.2：连续播放与返回操作

课文播放器增加播放时长设置，章节结束自动播放下一章。播放列表首页折叠为列表入口，详情页支持按顺序连播、定时停止和通过章节右侧加号添加到稍后播放队列。卡片设置增加切换后自动读词选项，默认关闭。Android 返回手势优先关闭弹窗、退出阅读器或词本详情、返回首页，仅首页退出应用。

沿用原签名，versionCode 3，可覆盖升级。后台定时受系统调度影响，具体手机仍需实机确认。
