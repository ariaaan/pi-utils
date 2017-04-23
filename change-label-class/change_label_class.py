import os
import glob
import argparse
from tqdm import tqdm

# Parse arguments
parser = argparse.ArgumentParser(description='change-label-class')

parser.add_argument('input_folder', help='path for the input folder')
parser.add_argument('source_class', type=int, help='source class_id')
parser.add_argument('dest_class', type=int, help='destination class_id')

args = parser.parse_args()

# Change label of images in the input folder
file_filter = '*.jpg'
image_files = glob.glob(os.path.join(args.input_folder, file_filter))

for image in tqdm(image_files):
    label_file = image[:-4] + '.txt'

    labels = open(label_file, 'r')
    labels = labels.read().strip().split('\n')

    new_label = ''

    for label in labels:
        label = label.split()

        try:
            if int(label[0]) == args.source_class:
                label[0] = str(args.dest_class)
        except Exception as e:
            print(e)

        new_label += ' '.join(label)

    labels = open(label_file, 'w')
    labels.write(new_label)
