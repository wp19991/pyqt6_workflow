#!/bin/bash

echo "执行pyqt6_workflow脚本，请确保在pyqt6的环境下"

# 扫描res目录下所有的*.qrc文件，转换为py文件
find res -name "*.qrc" -exec pyside6-rcc -g python {} \; \
  | sed '0,/PySide6/s//PyQt6/' > res/resource_rc.py
echo "资源文件转换完成"

# 扫描ui目录下所有的*.ui文件，转换为py文件
find ui -name "*.ui" -exec sh -c '
  file="$1"
  py_file="${file%.ui}.py"
  pyuic6 -x "$file" -o "$py_file"
  echo "\nfrom res import resource_rc" >> "$py_file"
' sh {} \;
echo "UI文件转换完成"

# 对每个转换后的UI文件进行QtWidgets.QOpenGLWidget替换为QtOpenGLWidgets.QOpenGLWidget
find ui -name "*.py" -exec sh -c '
  file="$1"
  pattern="QtWidgets.QOpenGLWidget"
  if grep -q "$pattern" "$file"; then
    sed -i "1i from PyQt6 import QtOpenGLWidgets" "$file"
    sed -i "s/QtWidgets.QOpenGLWidget/QtOpenGLWidgets.QOpenGLWidget/g" "$file"
    echo "成功修改含有OpenGLWidget的文件 $file"
  fi' sh {} \;

echo "pyqt6_workflow执行完成"
