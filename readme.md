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
nuitka --onefile --plugin-enable=pyside6 .\src\main.py
```

结果为

> **注意**
>
> * 在mac平台打包成 *.app 文件。
> * 在windows平台打包成 *.exe 文件。
