import os
import cv2
import uuid
import glob
import argparse
import numpy as np
from tqdm import tqdm


def convert_to_absolute(size, box):
    x1 = box[0] * size[0]
    y1 = box[1] * size[1]
    width = box[2] * size[0]
    height = box[3] * size[1]

    x1 = x1 - width / 2
    y1 = y1 - height / 2

    x2 = x1 + width
    y2 = y1 + height

    return [int(x) for x in [x1, y1, x2, y2]]


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description='label-to-crops')

    parser.add_argument('input_folder', help='path for the input folder')
    parser.add_argument('output_folder', help='path for the output folder')

    args = parser.parse_args()


    # Crop objects from images and labels
    file_filter = '*.jpg'
    image_files = glob.glob(os.path.join(args.input_folder, file_filter))

    for image_file in tqdm(image_files):
        label_file = image_file[:-4] + '.txt'
        label_text = open(label_file).read().strip()
        label_lines = label_text.split('\n')

        image = cv2.imread(image_file)
        height, width, _ = image.shape

        for object_label in label_lines:
            object_data = object_label.split()
            class_id = object_data[0]
            object_data = [float(x) for x in object_data[1:]]

            x1, y1, x2, y2 = convert_to_absolute((width, height), object_data)

            crop =  image[y1:y2, x1:x2, :]
            crop_filename = str(uuid.uuid4()) + '.jpg'
            cv2.imwrite(os.path.join(args.output_folder, crop_filename), crop)
