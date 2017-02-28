import os
import glob
import argparse
from tqdm import tqdm


parser = argparse.ArgumentParser(description='train-file-creator')
parser.add_argument('train_folder', help='path for the folder containing the train images')
parser.add_argument('train_file', help='output folder for the train.txt file')
args = parser.parse_args()


# Check if argument is a folder
if not os.path.isdir(args.train_folder) or not os.path.isdir(args.train_file):
    parser.print_help()
    sys.exit()


# Start renaming
file_filter = '*.jpg'
train_files = glob.glob(os.path.join(args.train_folder, file_filter))


# Get relative path form train_file to train_folder
relative_path = os.path.relpath(args.train_folder, args.train_file)


# Open train.txt file
filename = os.path.join(args.train_file, 'train.txt')
train_file = open(filename, 'w')


# For each image on train folder
for image_file in tqdm(train_files):
    # Write on train.txt the filename relative to ./darknet
    filename = os.path.basename(image_file)
    path = os.path.join(relative_path, filename)
    train_file.write(path + "\n")
