import os
import sys
import glob
import pickle
import argparse
import numpy as np
from tqdm import tqdm


NUM_CLASSES = 11


def one_hot_encode(i, num_classes=NUM_CLASSES):
    one_hot = np.zeros(num_classes, 'uint8')
    one_hot[i] = 1
    return one_hot


# Parse arguments
parser = argparse.ArgumentParser(description='make-ssd-pickle')

parser.add_argument('input_folder', help='path of the label folder')

parser.add_argument("-c", "--classes", type=int, default=NUM_CLASSES, help="number of classes in dataset")

args = parser.parse_args()


# Check if arguments are folders
if not os.path.isdir(args.input_folder):
    parser.print_help()
    sys.exit()


# Start creating ssd labels
file_filter = '*.txt'
label_files = glob.glob(os.path.join(args.input_folder, file_filter))

data_gt = {}

for label_file in label_files:
    label = open(label_file, 'r').read().strip()

    key = os.path.basename(label_file)[:-4] + '.jpg'
    data_gt[key] = []

    objects = label.split('\n')

    for obj in objects:
        try:
            class_id, xmin, ymin, xmax, ymax = obj.split()

            class_id = int(class_id)
            xmin = float(xmin)
            ymin = float(ymin)
            xmax = float(xmax)
            ymax = float(ymax)

            class_encoded = one_hot_encode(class_id, num_classes=args.classes)

            object_label = [xmin, ymin, xmax, ymax]
            object_label.extend(class_encoded)

            object_label = np.asarray(object_label, dtype='float64')
            data_gt[key].append(object_label)

        except:
            pass

    data_gt[key] = np.asarray(data_gt[key])

pickle_file = open('data_gt.pkl', 'wb')
pickle.dump(data_gt, pickle_file)
