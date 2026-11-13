# Android APK 打包准备

更新：2026-11-13。按用户要求，本轮只做准备，不构建 APK。

## 已准备

- Capacitor core/android/cli 8.6.2，版本解析结果保存在 package-lock.json。
- capacitor.config.json：com.stusta.arabiclearning，Arabic Learning，webDir=www。
- android/ 原生工程已创建，完整内置资源已同步。
- www/ 从 app/ 复制运行资源，不含原始词典、测试页面、缓存或凭据。
- 未设置远程 server.url；正式应用从包内读取正文、音频和词典。

## 环境

当前 CLI 要求 Node.js >=22；生成工程要求 Java 21、Android SDK Platform 36，minSdk 为 24。当前环境 PATH 未检测到 java/adb，常见 Android SDK 目录也未检测到。安装 Android Studio 后应按官方说明配置 JDK/SDK，不在仓库提交 local.properties。

参考：https://capacitorjs.com/docs/android 、https://capacitorjs.com/docs/getting-started 。以项目锁文件与生成的 Gradle 配置为准。

## 更新网页后的准备命令

在 Arabic_Learning 目录：

```powershell
npm ci
npm run check
npm run android:sync
npm run android:open
```

android/ 已存在，不要重复 android:add。若从不含 android/ 的工程开始才运行该命令。

## 正式构建前检查

- 真机断网打开两份内置材料，封面、词典、章节与单词音频可用。
- 词本按课筛选、点击定位、长按查词、词卡滑动、评分与恢复正常。
- WebView 中文件选择与备份导出实测；若浏览器下载方式不兼容，补原生 Filesystem/Share 适配后再交付。
- 后台/锁屏音频及定时停止的限制实测，必要时补媒体服务。
- 应用名/图标/启动页确认；当前使用默认 Android 图标，尚无品牌图标定稿。
- 正式签名密钥由用户保管，不写入 GitHub；debug 包与 release 包分开标识。
- 浏览器数据不会自动进入 APK；需要备份迁移。变更 appId 或清应用数据会影响现有记录。
- 词典 CC BY-SA 归属保留；合成语音和封面等资源的公开分发条件单独记录。

当前没有 APK、签名密钥或已完成的原生真机验收。


## 五色桌面图标准备

已增加 AppIconPlugin.java、MainActivity 注册、五组启动器 activity-alias 和对应矢量/自适应图标。使用本地 Capacitor JS 运行时；源代码和 XML 校验通过，未执行 Java/Gradle 编译。绿色为默认唯一启用入口，其他入口初始禁用。

待真机确认：切换后启动器刷新延迟、只保留一个图标、再次启动正常、各支持 Android 版本表现。网页不能直接改变桌面图标。先前默认图标待确认的描述现由本段五色书籍图标方案更新，正式交付仍需用户确认。


## 2026-11-14 APK 最新状态

已生成 releases/Arabic-Learning-v0.2.0.apk（正式签名 release，15,930,613 字节），v2/v3 签名和内置资源检查通过；隔离 API 37 模拟器安装、启动及蓝色图标切换/重启通过。此前“未编译 APK”等表述属于历史准备阶段。发布流程见 APK打包与发布.md。公开源码上传范围仅软件工程；GitHub 发布待 Fankikotan 账号授权。
