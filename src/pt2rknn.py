import argparse
import numpy as np
import cv2
from rknn.api import RKNN
import torchvision.models as models
import torch
import os

def convert(srcFileName, dstFilename, sizes):
    model = srcFileName

    input_size_list = [[1, 3, *sizes]]

    # Create RKNN object
    rknn = RKNN(verbose=True)

    # Pre-process config
    print('--> Config model')
    #rknn.config(mean_values=[123.675, 116.28, 103.53], std_values=[58.395, 58.395, 58.395])
    rknn.config(mean_values=[0, 0, 0], std_values=[255, 255, 255], target_platform='rk3588')
    print('config done')

    # Load model
    print('--> Loading model')
    ret = rknn.load_pytorch(model=model, input_size_list=input_size_list)
    if ret != 0:
        print('Load model failed!')
        return ret
    print('load done')

    # Build model
    print('--> Building model')
    ret = rknn.build(do_quantization=True, dataset=(os.path.dirname(os.path.realpath(__file__))+'/model/dataset.txt'))
    if ret != 0:
        print('Build model failed!')
        return ret
    print('build done')

    # Export rknn model
    print('--> Export rknn model')
    ret = rknn.export_rknn(dstFilename)
    if ret != 0:
        print('Export rknn model failed!')
        return ret

    print('export done')

    rknn.release()

def main():

    parser = argparse.ArgumentParser(description='transform to rknn model')
    parser.add_argument('source_file')
    parser.add_argument('description_file')
    args = parser.parse_args()

    convert(args.source_file, args.description_file, [640, 640])

if __name__ == '__main__':
    main()
