# Arabic Learning

当前版本 0.2.0。这是手机优先的阿拉伯语学习软件，完整内置教材、经典故事、词本、真实配音及阿英词典。

在本目录 `npm ci`、`npm start` 后打开 http://localhost:4173 。网页也可直接 `node scripts/serve.mjs` 运行。

已内置 12 课第一册、194 词《渔夫与精灵》、完整配套词本/语法/音频与阿英后备词典，无需导入。章节定位使用真实服务词边界；词典不包含音频。

- [使用说明](使用说明.md)
- [项目具体设计](项目具体设计.md)
- [通用设计规范](语言学习网页设计规范.md)
- [材料包协议](材料包格式.md)
- [交付配置](material-delivery.config.json)
- [最新进度](项目进度与讨论.md)
- [Android 打包准备](Android打包准备.md)
- [资源来源与许可](app/THIRD-PARTY-NOTICES.md)

`npm run check` 执行逻辑检查；`python scripts/package-mobile.py` 重建手机网页包；`npm run android:sync` 准备并同步 Android 资源，不编译 APK。尚未完成真机与后台播放验收、原生导出适配确认及专用手机进度导出。


## 2026-11-14 APK 最新状态

已生成 releases/Arabic-Learning-v0.2.0.apk（正式签名 release，15,930,613 字节），v2/v3 签名和内置资源检查通过；隔离 API 37 模拟器安装、启动及蓝色图标切换/重启通过。此前“未编译 APK”等表述属于历史准备阶段。发布流程见 APK打包与发布.md。公开源码上传范围仅软件工程；GitHub 发布待 Fankikotan 账号授权。
