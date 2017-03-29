import os
import sys
import glob
import argparse
from tqdm import tqdm


# Parse arguments
parser = argparse.ArgumentParser(description='label-validator')

parser.add_argument('input_folder', help='path of the label folder')
parser.add_argument('output_folder', help='path of the ouput fodler')

parser.add_argument("-c", "--classes", type=int, default=11, help="number of classes in dataset")

args = parser.parse_args()


# Check if arguments are folders
if not os.path.isdir(args.input_folder) or not os.path.isdir(args.output_folder):
    parser.print_help()
    sys.exit()


# Start creating ssd labels
file_filter = '*.txt'
label_files = glob.glob(os.path.join(args.input_folder, file_filter))

for label_file in label_files:
    label = open(label_file, 'r').read().strip()

    objects = label.split('\n')

    for obj in objects:
        try:
            class_id, xmin, ymin, xmax, ymax = obj.split()
            new_label = ''
        except:
            pass
