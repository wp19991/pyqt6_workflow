# pyqt6_workflow

Welcome to the pyqt6_workflow repository! This project aims to provide a streamlined workflow for quickly starting a new
program using PyQt6.

**[中文版本](README_zh.md)**

## Installation

To get started, simply run the following command to install the required dependencies:

```bash
pip install pyqt6 pyqt6-tools pyside6
```

## QtDesigner

QtDesigner is a powerful tool that allows you to create layouts by dragging and dropping components, eliminating the
need for manual code-based layout control. However, it requires a few additional steps involving `uic`
and `pyside6-rcc`. Don't worry, we've got you covered with the following instructions:

1. Make the workflow script executable by running the following command:
    - On Linux: `chmod +x workflow.sh`
    - For Windows users, please search for the equivalent steps.

**Pro Tip:** You can directly run the workflow script by opening this README.md file in PyCharm and clicking the green
button next to it.

```bash
chmod +x workflow.sh
./workflow.sh
```

### Usage

- **designer**
  Launch QtDesigner using the following command:

  ```bash
  pyqt6-tools designer
  ```

- **pyuic6**
  The `pyuic6` tool allows you to convert designer files to Python files, making it easier to write code logic. If you
  don't have `uic` installed, you can execute `pyqt6-tools installuic` to install it. Additionally, the `-x` flag
  generates a standalone executable window, and the `echo -e '' > file` command appends content to the end of a file (
  the `-e` flag enables recognition of `\n`).

  **Note:** Remember to <font color=#008000>**modify**</font> the file names in the commands below for each individual
  file you want to convert.

  ```bash
  pyuic6 -x ui/MainWindow.ui -o ui/MainWindow.py && echo -e "\nfrom res import resource_rc" >> ui/MainWindow.py
  ```

- **pyside6-rcc**
  This tool converts resource files to Python files, making them easier to package and use with QtDesigner. The command
  also includes a `sed` command to replace `PySide6` with `PyQt6`, ensuring compatibility.

  **Note:** Remember to <font color=#008000>**modify**</font> the file names in the commands below for each individual
  file you want to convert.

  ```bash
  pyside6-rcc -g python ./res/resource.qrc | sed '0,/PySide6/s//PyQt6/' > ./res/resource_rc.py
  ```

Feel free to explore and make the most of the pyqt6_workflow repository. Happy coding!