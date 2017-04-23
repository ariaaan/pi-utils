import os
import sys
import cv2
import glob
import argparse
from tqdm import tqdm


# Parse arguments
parser = argparse.ArgumentParser(description='rename-frames')
parser.add_argument('input_path', help='input path')
args = parser.parse_args()


# Main
file_filter = '*.jpg'
image_list = glob.glob(os.path.join(args.input_path, file_filter))


for image in tqdm(image_list):
    image_basename = os.path.basename(image)
    video_filename = os.path.basename(os.path.normpath(os.path.dirname(image)))
    new_name = os.path.join(args.input_path, video_filename + '-' + image_basename)

    os.rename(image, new_name)

    label = image[:-4] + '.txt'
    new_name = os.path.join(args.input_path, video_filename + '-' + image_basename[:-4] + '.txt')

    try:
        os.rename(label, new_name)
    except:
        pass
