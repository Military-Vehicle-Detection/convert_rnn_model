#!/bin/bash
CONTAINER_NAME="sandbox"
git clone https://github.com/ultralytics/yolov5.git packages/yolov5
git clone https://github.com/rockchip-linux/rknn-toolkit2.git packages/toolkit
rm -R $CONTAINER_NAME
python3 -m venv $CONTAINER_NAME
source $CONTAINER_NAME/bin/activate

pip3 install -r requirements.txt
pip3 install packages/toolkit/packages/rknn_toolkit2-1.4.0_22dcfef4-cp38-cp38-linux_x86_64.whl
