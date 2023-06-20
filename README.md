# pyqt6_workflow

> 使用pyqt6的工作流，可以很快的开始一个新的程序的编写

- 安装：`pip install pyqt6 pyqt6-tools pyside6`

## QtDesigner

> 使用QtDesigner，可以实现拖拽布局，不需要手动代码控制布局
> - 代价就是需要进行下面的uic，pyside6-rcc的步骤
> - 可以写一个脚本文件，每次修改后只需要运行以下即可
>   - 变为可执行文件：`chmod +x workflow.sh`
> - 下面的命令是linux的环境下，windows需要自己搜索

> PS：下面的命令在PyCharm中打开README.md可以点击旁边的绿色按钮直接运行

```bash
chmod +x workflow.sh
./workflow.sh
```

- designer

```bash
pyqt6-tools designer
```

- pyuic6
    - 将designer的文件转为py文件，方便编写代码逻辑
    - 没有uic可以执行：`pyqt6-tools installuic`
    - `-x`表示生成可单文件执行的窗口
    - `echo -e '' > file`表示追加到文件结尾
      - 里面的`-e`表示使用斜杠的符号，可以识别`\n`
    - 增加的时候需要<font color=#008000 >**修改**</font>下面的文件名称，每个单独的文件都需要写一行

```bash
pyuic6 -x ui/MainWindow.ui -o ui/MainWindow.py && echo -e "\nfrom res import resource_rc" >> ui/MainWindow.py
```

- pyside6-rcc
    - 使用这个将资源文件改为py文件，方便打包和designer使用资源
    - `sed`是将PySide6改为PyQt6，不然无法正常使用
    - 增加的时候需要<font color=#008000 >**修改**</font>下面的文件名称

```bash
pyside6-rcc -g python ./res/resource.qrc | sed '0,/PySide6/s//PyQt6/' > ./res/resource_rc.py
```wo