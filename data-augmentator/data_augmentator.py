import os
import cv2
import glob
import argparse
import numpy as np
from shutil import copyfile


def copy_label(original_image_path, modified_image_path):
    original_label_path = original_image_path[:-4] + ".txt"
    modified_label_path = modified_image_path[:-4] + ".txt"

    if os.path.isfile(original_label_path):
        copyfile(original_label_path, modified_label_path)


def mirror_horizontal(image_path, output_folder):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = image.copy()

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".mh.jpg")

    for row in range(height):
        new_image[row, :] = image[(height - 1) - row, :]

    cv2.imwrite(output_path, new_image)


def mirror_vertical(image_path, output_folder):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = image.copy()

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".mv.jpg")

    for col in range(width):
        new_image[:, col] = image[:, (width - 1) - col, ]

    cv2.imwrite(output_path, new_image)

    labels = open(image_path[:-4] + '.txt').read().strip().split('\n')

    new_label = ''

    for label in labels:
        label = label.split()
        label[1] = str(1 - float(label[1]))

        label = ' '.join(label)
        new_label += label
        new_label += '\n'

    output_label_path = output_path[:-4] + '.txt'
    output_label_file = open(output_label_path, 'w')
    output_label_file.write(new_label)


def rotate_90(image_path, output_folder):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = np.rot90(image, 3)

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".r90.jpg")

    cv2.imwrite(output_path, new_image)


def rotate_180(image_path, output_folder):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = np.rot90(image, 2)

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".r180.jpg")

    cv2.imwrite(output_path, new_image)


def rotate_270(image_path, output_folder):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = np.rot90(image, 1)

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".r270.jpg")

    cv2.imwrite(output_path, new_image)


def saturation(image_path, output_folder, saturation):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = image.copy()
    new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2HSV).astype("float32")

    (h, s, v) = cv2.split(new_image)
    s = s * saturation
    s = np.clip(s, 0, 255)

    new_image = cv2.merge([h, s, v])

    new_image = cv2.cvtColor(new_image.astype("uint8"), cv2.COLOR_HSV2BGR)

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".sat.jpg")

    cv2.imwrite(output_path, new_image)


def saturation(image_path, output_folder, saturation):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = image.copy()
    new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2HSV).astype("float32")

    (h, s, v) = cv2.split(new_image)
    s = s * saturation
    s = np.clip(s, 0, 255)

    new_image = cv2.merge([h, s, v])

    new_image = cv2.cvtColor(new_image.astype("uint8"), cv2.COLOR_HSV2BGR)

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + ".sat.jpg")

    cv2.imwrite(output_path, new_image)


def brightness(image_path, output_folder, level, name="bri"):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    new_image = image.copy()
    new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2HSV).astype("float32")

    (h, s, v) = cv2.split(new_image)
    v = v * level
    v = np.clip(v, 0, 255)

    new_image = cv2.merge([h, s, v])

    new_image = cv2.cvtColor(new_image.astype("uint8"), cv2.COLOR_HSV2BGR)

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, filename[:-4] + "." + name +".jpg")

    cv2.imwrite(output_path, new_image)

    copy_label(image_path, output_path)


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description='data-augmentator')

    parser.add_argument('input_folder', help='path for the input folder')
    parser.add_argument('output_folder', help='path for the output folder')

    parser.add_argument('-mv', '--mirror-vertical', action='store_true', help='mirror vertical')
    parser.add_argument('-mh', '--mirror-horizontal', action='store_true', help='mirror horizontal')
    parser.add_argument('-r90', '--rotate-90', action='store_true', help='rotate 90 degrees')
    parser.add_argument('-r180', '--rotate-180', action='store_true', help='rotate 180 degrees')
    parser.add_argument('-r270', '--rotate-270', action='store_true', help='rotate 270 degrees')
    parser.add_argument('-b', '--brighten', action='store_true', help='brighten')
    parser.add_argument('-d', '--darken', action='store_true', help='darken')

    args = parser.parse_args()

    # Augmentate the data in the input folder
    file_filter = '*.jpg'
    image_files = glob.glob(os.path.join(args.input_folder, file_filter))

    for image_file in image_files:

        if args.mirror_vertical:
            mirror_vertical(image_file, args.output_folder)

        if args.mirror_horizontal:
            mirror_horizontal(image_file, args.output_folder)

        if args.rotate_90:
            rotate_90(image_file, args.output_folder)

        if args.rotate_180:
            rotate_180(image_file, args.output_folder)

        if args.rotate_270:
            rotate_270(image_file, args.output_folder)

        if args.brighten:
            brightness(image_file, args.output_folder, 2.0, name="bri")

        if args.darken:
            brightness(image_file, args.output_folder, 0.5, name="dark")
