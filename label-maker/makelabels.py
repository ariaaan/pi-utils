import os
import sys
import argparse
from functions import label_images

# Argument Parser
parser = argparse.ArgumentParser(description='label-maker')

parser.add_argument('images_folder', help='path for the images folder')
parser.add_argument('crop_folder', help='path for the cropped images folder')
parser.add_argument('label_folder', help='path for the labels folder')

parser.add_argument('--relative', '-r', action='store_true', help='label in relative format' )

args = parser.parse_args()


# Check if arguments are folders
if not os.path.isdir(args.images_folder) or not os.path.isdir(args.crop_folder) or not os.path.isdir(args.label_folder):
    parser.print_help()
    sys.exit()


# Start labeling
label_images(args.images_folder, args.crop_folder, args.label_folder, relative=args.relative)
