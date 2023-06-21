# pyqt6_workflow

Welcome to the pyqt6_workflow repository! This project aims to provide a simplified workflow for quickly starting new programs using PyQt6.

**[中文版本](README_zh.md)**

## Installation

To get started, run the following command to install the required dependencies:

```bash
pip install pyqt6 pyqt6-tools pyside6
```

## QtDesigner

QtDesigner is a powerful tool for creating layouts by dragging and dropping components, without the need for manually writing layout control code. However, it requires some additional steps involving `uic` and `pyside6-rcc`. Don't worry, we provide the following instructions, and now we have automated the process of searching and converting files in the `workflow.sh` script, so there's no need to manually modify the script.

1. Run the following command to make the workflow script executable:
    - On Linux: `chmod +x workflow.sh`
    - For Windows users, please search for the appropriate steps.

**Pro Tip:** You can open this README.md file in PyCharm and click the adjacent green button to run the workflow script directly.

```bash
chmod +x workflow.sh
./workflow.sh
```

### Usage

- **designer**
  Start QtDesigner using the following command:

  ```bash
  pyqt6-tools designer
  ```

- **pyuic6**
  The `pyuic6` tool allows you to convert design files to Python files, making it more convenient to write code logic. If you don't have `uic` installed, you can run `pyqt6-tools installuic` to install it. Additionally, the `-x` flag generates a standalone executable window, and the `echo -e '' > file` command appends content to the end of a file (the `-e` flag enables recognition of `\n`).

  **Note:** We have now automated the process of searching and converting files in the `workflow.sh` script, so there's no need to manually modify the script.

  ```bash
  pyuic6 -x ui/MainWindow.ui -o ui/MainWindow.py && echo -e "\nfrom res import resource_rc" >> ui/MainWindow.py
  ```

- **pyside6-rcc**
  This tool converts resource files to Python files for easy packaging and use in QtDesigner. The `sed` command in the command replaces `PySide6` with `PyQt6` to ensure compatibility.

  **Note:** We have now automated the process of searching and converting files in the `workflow.sh` script, so there's no need to manually modify the script.

  ```bash
  pyside6-rcc -g python ./res/resource.qrc | sed '0,/PySide6/s//PyQt6/' > ./res/resource_rc.py
  ```

Feel free to explore and make the most of the pyqt6_workflow repository. Happy coding!