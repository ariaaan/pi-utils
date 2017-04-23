import os
import sys
import glob
import argparse
from tqdm import tqdm
from shutil import copy


# Argument parser
parser = argparse.ArgumentParser(description='organize-video-data')
parser.add_argument('data_path', help='path for the folder containing images and labels')
parser.add_argument('output_path', help='output path for the organized data')
args = parser.parse_args()


# Variables
OUTPUT_FOLDER = 'all/'


# Check if argument is a folder
if not os.path.isdir(args.data_path) or not os.path.isdir(args.output_path):
    parser.print_help()
    sys.exit()


# Get the labels file list
file_filter = '*.txt'
label_files = glob.glob(os.path.join(args.data_path, file_filter))


# Output folder for all images
output_folder = os.path.join(args.output_path, OUTPUT_FOLDER)


# For each file in label_files
for label_file in tqdm(label_files):
    image_file = label_file[:-4] + '.jpg'

    # Read label file
    labels = open(label_file, 'r').read()

    if labels is not '':
        labels = labels.strip().split('\n')

        # Copy image and label to common folder (<output_path>/all/)
        if not os.path.isdir(output_folder):
            os.makedirs(output_folder)

        copy(image_file, output_folder)
        copy(label_file, output_folder)

        for label in labels:
            # Copy image and label to class folder (<output_path>/<class_id>/)
            class_id = label.split()[0]
            class_folder = os.path.join(args.output_path, class_id)

            if not os.path.isdir(class_folder):
                os.makedirs(class_folder)

            copy(image_file, class_folder)
            copy(label_file, class_folder)
