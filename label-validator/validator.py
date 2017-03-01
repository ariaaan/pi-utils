import os
import cv2
import glob
import json
import argparse
from tqdm import tqdm


def get_config(path):
    with open(path) as config_file:
        config = json.load(config_file)
        return config


def convert_to_absolute(size, box):
    class_id = box[0]

    x1 = box[1] * size[0]
    y1 = box[2] * size[1]
    width = box[3] * size[0]
    height = box[4] * size[1]

    x1 = x1 - width / 2
    y1 = y1 - height / 2

    x2 = x1 + width
    y2 = y1 + height

    return [class_id, x1, y1, x2, y2]


def create_bb(image_path, label_path, output_path, relative=False):
    config = get_config('config.json')
    color = (60, 0, 255)

    image = cv2.imread(image_path)
    label = open(label_path, 'r')
    height, width, _ = image.shape

    lines = label.read().strip().split('\n')

    bounding_boxes = []

    for line in lines:
        bb_points = line.strip().split()

        if relative:
            bb_points = list(map(float, bb_points))
            bb_points = convert_to_absolute((width, height), bb_points)

        bb_points = list(map(int, bb_points))
        bounding_boxes.append(bb_points)

    for box in bounding_boxes:
        cv2.rectangle(image, (box[1], box[2]), (box[3], box[4]), color, thickness=3)

        label = config[str(box[0])]['name']
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_color = (255,255,255)
        scale = 0.5
        thickness = 1

        size = cv2.getTextSize(label, font, scale, thickness)
        width = size[0][0]
        height = size[0][1]

        cv2.rectangle(image, (int(box[1] - width / 2), box[2] - height),
                      (int(box[1] + width / 2) + 5, box[2] + 5),
                      color,
                      thickness=cv2.FILLED)

        cv2.putText(image, label, (int(box[1] - width / 2), box[2]), font,
                    scale, font_color, thickness=thickness)

    cv2.imwrite(output_path, image)


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description='label-validator')

    parser.add_argument('image_folder', help='path for the folder containing the images')
    parser.add_argument('label_folder', help='path for the folder containing the labels')
    parser.add_argument('output_folder', help='path for the output folder')

    parser.add_argument('--relative', '-r', action='store_true', help='label in relative format' )

    args = parser.parse_args()

    # Check if argument is a folder
    if not os.path.isdir(args.image_folder) or not os.path.isdir(args.label_folder) or not os.path.isdir(args.output_folder):
        parser.print_help()
        sys.exit()

    # Start creating bounding boxes
    file_filter = '*.jpg'
    image_files = glob.glob(os.path.join(args.image_folder, file_filter))

    for image_file in tqdm(image_files):
        image_path = image_file
        label_path = os.path.join(args.label_folder, os.path.basename(image_file)[:-4] + ".txt")
        output_path = os.path.join(args.output_folder, os.path.basename(image_file))

        create_bb(image_path, label_path, output_path, relative=args.relative)
