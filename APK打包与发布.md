# APK 打包与发布

更新：2026-11-14。已编译正式签名的 release APK，保存在 releases/Arabic-Learning-v0.2.0.apk。它不是 debug 安装包。

## 本次执行流程

1. 修正界面拼写为 Remember Me，并运行 npm run check。
2. npm run android:sync，将网页、内置教材、故事、385 个 MP3 和词典同步到 Android 工程。
3. 使用 Java 21、Android SDK 36 与 Gradle 8.14.3，运行 assembleRelease。
4. 对 unsigned APK 执行 zipalign，再用本地 RSA 3072 位密钥通过 apksigner 签名。
5. 验证 v2/v3 签名、ZIP 完整性、包名、版本、内置材料和音频。
6. 在隔离 Android API 37 模拟器中安装启动，并验证桌面图标切换至蓝色后仍可启动。
7. 将软件工程上传到 Fankikotan/Arabic_Learning_App，APK 作为 GitHub Release 附件发布。已使用 Fankikotan 完成授权，源码与 APK Release 均已发布。

## 用 Android Studio 再次打包

1. 启动 Android Studio，打开本项目 android/ 目录。
2. Gradle JDK 选择 Java 21；SDK 路径按本机配置，不把 local.properties 提交到 Git。
3. 等待 Gradle 同步完成；修改网页后先在项目目录运行 npm run android:sync。
4. 菜单 Build → Generate Signed App Bundle or APK → APK。
5. 选择现有 keystore、别名和密码，选择 release 后构建。
6. 使用相同签名密钥才能覆盖升级已有安装。密钥与密码应单独备份，不公开上传。

本次使用独立安装的 Microsoft OpenJDK 21，没有改系统的 Android Studio Java 25 配置。SDK 编译组件按官方包校验和校验。

## 本地签名材料

签名密钥和密码只保存在学习室 .runtime/signing/，受 .gitignore 排除；不放入软件公开源码或 Release。该目录须由项目所有者妥善备份。

公开仓库只包含 Arabic_Learning 软件工程与内置资源，不包含个人学习进度、独立技能、运行缓存或本地 SDK 路径。

## 安装与验证边界

最低 Android 7.0（API 24），目标 API 36，版本 0.2.0。APK 下载后需允许当前下载来源安装应用。校验和见 releases/SHA256SUMS.txt，签名公开证书摘要见 signature-verification.txt。

已完成模拟器安装/启动和蓝色桌面图标切换/重启。实体手机上的后台播放、文件导入导出兼容性及不同启动器行为仍需验证；不将模拟器冒烟检查描述为所有 Android 机型验收。


## v0.2.1：例句显示控制

词汇页右上角打开“通用词汇显示设置”：例句原文通过独立勾选项控制；例句翻译可选择默认显示、点击显示或不显示。设置同时适用于条目和卡片、词本/最近接触/收藏/我的学习。关闭原文不再强制关闭翻译，关闭翻译也不隐藏原文。

v0.2.1 使用 versionCode 2 与原有签名密钥，可覆盖安装 v0.2.0；旧版 Release 保留。浏览器已检查原文开关与翻译三种模式的全部六种组合。


v0.2.1 已正式发布：https://github.com/Fankikotan/Arabic_Learning_App/releases/tag/v0.2.1 。覆盖安装/启动及公开 APK 下载校验和验证通过，v0.2.0 保留。


## 2026-11-14 v0.2.2

新增课文连续播放及播放器定时入口、卡片切换自动读词选项、Android 应用内返回、播放列表详情与连播、稍后播放队列。versionCode 3，沿用原签名。
