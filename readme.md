# 说明

这是一个简单的使用qt6进行将文本分句的小程序。

## 转换qt 的 UI文件

### windows

```shell
pyside6-uic.exe .\src\convert.ui -o .\src\convert.py
```

### mac

```shell
pyside6-uic .\src\convert.ui -o .\src\convert.py
```

## 打包成EXE文件

参考QT官网的打包工具列表：<https://doc.qt.io/qtforpython/deployment.html#deployment-guides>

以及 nuitka3： <https://doc.qt.io/qtforpython/deployment-nuitka.html>

我的打包命令:

```shell
# win 平台
nuitka.bat --onefile --plugin-enable=pyside6 .\src\main.py
# mac 平台

# 用这行包含包的数据目录，否则打包不成功。
nuitka3 --onefile --plugin-enable=pyside6 --include-package-data=thulac ./src/main.py
```

结果为

> **注意**
>
> * 在mac平台打包成 *.app 文件。
> * 在windows平台打包成 *.exe 文件。

## nuitka3 简介

官方文档：<https://nuitka.net/>

官方程序分发简介: <https://nuitka.net/doc/user-manual.html#use-case-4-program-distribution>

中文详细参考: <https://blog.csdn.net/qq_17328759/article/details/120230311>
