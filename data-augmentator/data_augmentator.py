import os
import cv2
import glob
import argparse
import numpy as np


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


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description='data-augmentator')

    parser.add_argument('input_folder', help='path for the input folder')
    parser.add_argument('output_folder', help='path for the output folder')

    args = parser.parse_args()

    # Augmentate the data in the input folder
    file_filter = '*.jpg'
    image_files = glob.glob(os.path.join(args.input_folder, file_filter))

    for image_file in image_files:
        mirror_horizontal(image_file, args.output_folder)
        mirror_vertical(image_file, args.output_folder)
        rotate_90(image_file, args.output_folder)
        rotate_180(image_file, args.output_folder)
        rotate_270(image_file, args.output_folder)
