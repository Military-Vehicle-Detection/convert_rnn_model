#!/bin/bash

SRC_FILENAME=$1
DST_FILENAME=$2
DIR_NAME=$(dirname $SRC_FILENAME)
BASE_NAME=$(basename -- $SRC_FILENAME)
EXT_NAME="${BASE_NAME##*.}"
PURE_NAME="${BASE_NAME%.*}"
CONTAINER_NAME="sandbox"

TEMP_FILE_NAME="$DIR_NAME/$PURE_NAME.torchscript"
PT_TEMP_FILE_NAME="$TEMP_FILE_NAME.$EXT_NAME"

source $CONTAINER_NAME/bin/activate

python3 packages/yolov5/export.py --weights $SRC_FILENAME --img 640 --batch 1
mv $TEMP_FILE_NAME $PT_TEMP_FILE_NAME
python3 src/pt2rknn.py $PT_TEMP_FILE_NAME $DST_FILENAME
rm $PT_TEMP_FILE_NAME