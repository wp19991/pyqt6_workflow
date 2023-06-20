# pyqt6_workflow

欢迎来到 pyqt6_workflow 仓库！该项目旨在提供使用 PyQt6 快速启动新程序的简化工作流程。

## 安装

要开始使用，请运行以下命令安装所需依赖项：

```bash
pip install pyqt6 pyqt6-tools pyside6
```

## QtDesigner

QtDesigner 是一个强大的工具，可以通过拖放组件来创建布局，无需手动编写布局控制代码。然而，它需要执行一些额外的步骤，涉及 `uic`
和 `pyside6-rcc`。别担心，我们提供了以下说明：

1. 运行以下命令将工作流脚本设置为可执行：
    - 在 Linux 上：`chmod +x workflow.sh`
    - 对于 Windows 用户，请自行搜索相应的步骤。

**专业提示：** 你可以在 PyCharm 中打开此 README.md 文件，并点击旁边的绿色按钮直接运行工作流脚本。

```bash
chmod +x workflow.sh
./workflow.sh
```

### 使用方法

- **designer**
  使用以下命令启动 QtDesigner：

  ```bash
  pyqt6-tools designer
  ```

- **pyuic6**
  `pyuic6` 工具允许你将设计文件转换为 Python 文件，使得编写代码逻辑更加便捷。如果你没有安装 `uic`
  ，可以执行 `pyqt6-tools installuic` 进行安装。另外，`-x` 标志生成独立的可执行窗口，`echo -e '' > file`
  命令将内容追加到文件末尾（`-e` 标志启用对 `\n` 的识别）。

  **注意：** 每次添加新文件时，请<font color=#008000>**修改**</font>下面命令中的文件名。

  ```bash
  pyuic6 -x ui/MainWindow.ui -o ui/MainWindow.py && echo -e "\nfrom res import resource_rc" >> ui/MainWindow.py
  ```

- **pyside6-rcc**
  此工具将资源文件转换为 Python 文件，方便打包和在 QtDesigner 中使用。命令中的 `sed` 命令将 `PySide6` 替换为 `PyQt6`
  ，以确保兼容性。

  **注意：** 每次添加新文件时，请<font color=#008000>**修改**</font>下面命令中的文件名。

  ```bash
  pyside6-rcc -g python ./res/resource.qrc | sed '0,/PySide6/s//PyQt6/' > ./res/resource_rc.py
  ```

随意探索并充分利用 pyqt6_workflow 仓库。祝你编码愉快！