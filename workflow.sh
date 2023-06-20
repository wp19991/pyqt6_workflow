echo "执行pyqt6_workflow脚本，请确保在pyqt6的环境下"
echo "将资源文件转换为py文件"
pyside6-rcc -g python ./res/resource.qrc | sed '0,/PySide6/s//PyQt6/' >./res/resource_rc.py

echo "将ui文件转换为py文件"
pyuic6 -x ui/MainWindow.ui -o ui/MainWindow.py && echo -e "\nfrom res import resource_rc" >>ui/MainWindow.py

echo "pyqt6_workflow执行完成"
